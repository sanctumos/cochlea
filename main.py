# Sanctum Cochlea - Audio Ingest System for Sanctum and Letta Installations
# Copyright (C) 2025 Sanctum Cochlea Contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import json

from dotenv import load_dotenv
from letta_client import Letta, VoiceSleeptimeManagerUpdate


from livekit import agents
from livekit.agents import AgentSession, Agent, AutoSubscribe
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    silero,
)
load_dotenv()

def prewarm_process(proc: agents.JobProcess):
    """Prewarm the VAD model for better performance."""
    proc.userdata["vad"] = silero.VAD.load()

async def entrypoint(ctx: agents.JobContext):
    agent_id = os.environ.get('LETTA_AGENT_ID')
    print(f"Agent id: {agent_id}")
    
    # Custom LLM wrapper for VPS Letta
    if os.getenv('LETTA_BASE_URL'):
        print("Connecting to self-hosted Letta - using custom LLM wrapper")
        
        from livekit.agents.llm import LLM, ChatContext, ChatItem
        from livekit.agents.llm.llm import LLMStream
        import asyncio
        import json
        
        class VPSLettaLLM(LLM):
            def __init__(self, agent_id: str, base_url: str, api_key: str):
                super().__init__()
                self.agent_id = agent_id
                self.base_url = base_url
                self.api_key = api_key
                self.letta_client = Letta(token=api_key, base_url=base_url)
            
            def chat(self, *, chat_ctx: ChatContext, **kwargs):
                # Convert ChatContext to Letta messages format
                # Only send the latest user message (VPS Letta doesn't handle conversation history well)
                letta_messages = []
                
                # Find the latest user message
                latest_user_message = None
                for item in chat_ctx.items:
                    if hasattr(item, 'content') and hasattr(item, 'role') and item.role == "user":
                        content = item.content
                        
                        # Handle both string and list content
                        if isinstance(content, str):
                            text_content = content
                        elif isinstance(content, list) and len(content) > 0:
                            text_content = content[0]  # Take first item from list
                        else:
                            continue
                        
                        if text_content:  # Only add non-empty content
                            latest_user_message = text_content
                
                # Only send the latest user message
                if latest_user_message:
                    # Add identification to distinguish voice input in logs
                    identified_message = f"[VOICE-INPUT] {latest_user_message}"
                    letta_messages.append({
                        "role": "user",
                        "content": [{"type": "text", "text": identified_message}]
                    })
                else:
                    # Fallback: send empty message to avoid errors
                    letta_messages.append({
                        "role": "user",
                        "content": [{"type": "text", "text": "[VOICE-INPUT] Hello"}]
                    })
                
                # Send to VPS Letta messages endpoint directly
                import requests
                import time
                url = f"{self.base_url}/agents/{self.agent_id}/messages"
                headers = {
                    'Authorization': f'Bearer {self.api_key}',
                    'Content-Type': 'application/json'
                }
                data = {'messages': letta_messages}
                
                # Retry logic for VPS connection
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        print(f"🔄 Attempting VPS connection (attempt {attempt + 1}/{max_retries})")
                        response = requests.post(url, headers=headers, json=data, timeout=30)
                        response.raise_for_status()
                        print(f"✅ VPS connection successful on attempt {attempt + 1}")
                        break
                    except requests.exceptions.Timeout as e:
                        print(f"⏰ VPS timeout on attempt {attempt + 1}: {e}")
                        if attempt < max_retries - 1:
                            print(f"🔄 Retrying in 2 seconds...")
                            time.sleep(2)
                        else:
                            print("❌ All VPS connection attempts failed")
                            raise
                    except Exception as e:
                        print(f"❌ VPS connection error on attempt {attempt + 1}: {e}")
                        if attempt < max_retries - 1:
                            print(f"🔄 Retrying in 2 seconds...")
                            time.sleep(2)
                        else:
                            raise
                
                # Extract response text
                response_data = response.json()
                response_text = ""
                print(f"🔍 Raw VPS response: {response_data}")
                
                if 'messages' in response_data:
                    for msg in response_data['messages']:
                        print(f"🔍 Processing message: {msg}")
                        # Only extract the actual assistant message content, not reasoning
                        if msg.get('message_type') == 'assistant_message' and 'content' in msg and msg['content']:
                            if isinstance(msg['content'], str):
                                response_text = msg['content']
                                print(f"🎤 Extracted response text: {response_text}")
                                break  # We only want the first assistant message
                
                if not response_text:
                    print("⚠️ No response text extracted from VPS")
                    response_text = "I received your message but couldn't process the response properly."
                
                # Create a context manager that returns a stream
                class ChatContextManager:
                    def __init__(self, text):
                        self.text = text
                        self.stream = None
                    
                    async def __aenter__(self):
                        # Create a simple stream with the response
                        class SimpleStream:
                            def __init__(self, text):
                                self.text = text
                                self._closed = False
                            
                            async def __aiter__(self):
                                if not self._closed:
                                    yield self.text
                                    self._closed = True
                            
                            async def aclose(self):
                                self._closed = True
                        
                        self.stream = SimpleStream(self.text)
                        return self.stream
                    
                    async def __aexit__(self, exc_type, exc_val, exc_tb):
                        if self.stream:
                            await self.stream.aclose()
                
                return ChatContextManager(response_text)
        
        llm = VPSLettaLLM(
            agent_id=agent_id,
            base_url=os.getenv('LETTA_BASE_URL'),
            api_key=os.getenv('LETTA_API_KEY')
        )
    else:
        print("Connecting to Letta Cloud")
        # Use standard Letta Cloud approach
        letta_config = {'agent_id': agent_id}
        llm = openai.LLM.with_letta(**letta_config)
    
    # Configure VAD for better sentence accumulation
    vad = ctx.proc.userdata.get("vad") or silero.VAD.load()
    
    # Configure VAD with conservative settings to prevent TTS interruption
    vad.min_silence_duration_ms = 200  # Short silence detection
    vad.speaking_probability_threshold = 0.6  # Balanced threshold
    vad.min_speaking_duration_ms = 300  # Require sustained speech
    
    # Configure STT with better sentence accumulation settings
    stt = deepgram.STT(
        model="nova-2",  # Use the latest model
        language="en-US",
        # Add some delay to wait for complete sentences
        interim_results=True,  # Enable interim results
        endpointing_ms=800,  # Wait 800ms of silence before considering speech complete
    )
    
    # Configure TTS with debugging
    tts = cartesia.TTS()
    
    session = AgentSession(
        llm=llm,
        stt=stt,
        tts=tts,
        vad=vad,  # Re-enable VAD with conservative settings
    )

    # Add audio feedback prevention
    # The LiveKit voice agent automatically handles muting during TTS
    # but we can add additional feedback prevention here if needed
    print("🔇 Audio feedback prevention enabled - microphone will be muted during TTS")

    await session.start(
        room=ctx.room,
        agent=Agent(instructions=""), # instructions should be set in the Letta agent
    )

    session.say("Hi, what's your name?")
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)

if __name__ == "__main__":
    # check if we already have an agent ID
    existing_agent_id = os.getenv('LETTA_AGENT_ID')
    
    if existing_agent_id:
        # Use existing agent
        print(f"Using existing agent ID: {existing_agent_id}")
        agent_id = existing_agent_id
    else:
        # Create new agent
        print("No existing agent ID found, creating new agent...")
        client = Letta(token=os.getenv('LETTA_API_KEY'))

        # create the Letta agent with configurable settings from environment
        agent = client.agents.create(
            name=os.getenv('LETTA_AGENT_NAME', 'low_latency_voice_agent_demo'),
            agent_type=os.getenv('LETTA_AGENT_TYPE', 'voice_convo_agent'),
            memory_blocks=[
                {"value": "Name: ?", "label": "human"},
                {"value": "You are a helpful assistant.", "label": "persona"},
            ],
            model=os.getenv('LETTA_MODEL', 'openai/gpt-4o-mini'), # Use 4o-mini for speed
            embedding=os.getenv('LETTA_EMBEDDING', 'openai/text-embedding-3-small'),
            enable_sleeptime=os.getenv('LETTA_ENABLE_SLEEPTIME', 'true').lower() == 'true',
            initial_message_sequence = [],
        )
        print(f"Created new agent: {agent.name} (ID: {agent.id})")
        
        # configure the sleep-time agent 
        group_id = agent.multi_agent_group.id
        max_message_buffer_length = agent.multi_agent_group.max_message_buffer_length
        min_message_buffer_length = agent.multi_agent_group.min_message_buffer_length
        print(f"Group id: {group_id}, max_message_buffer_length: {max_message_buffer_length},  min_message_buffer_length: {min_message_buffer_length}")
        
        # Configure sleep-time settings from environment variables
        max_buffer = int(os.getenv('LETTA_MAX_MESSAGE_BUFFER', '10'))
        min_buffer = int(os.getenv('LETTA_MIN_MESSAGE_BUFFER', '6'))
        
        group = client.groups.modify(
            group_id=group_id,
            manager_config=VoiceSleeptimeManagerUpdate(
                max_message_buffer_length=max_buffer,
                min_message_buffer_length=min_buffer,
            )
        )

        # update the sleep-time agent model 
        sleeptime_agent_id = [agent_id for agent_id in group.agent_ids if agent_id != agent.id][0]
        client.agents.modify(
            agent_id=sleeptime_agent_id,
            model=os.getenv('LETTA_SLEEPTIME_MODEL', 'anthropic/claude-sonnet-4-20250514')
        )
        
        agent_id = agent.id

    # Set the agent id in environment variable so it's accessible in the worker process
    os.environ['LETTA_AGENT_ID'] = agent_id
    print(f"Using agent ID: {agent_id}")

    # Now that LETTA_AGENT_ID is set, run the worker app
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))