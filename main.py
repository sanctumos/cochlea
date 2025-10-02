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
import time

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

def validate_cartesia_config():
    """Validate Cartesia configuration and return configuration dict with warnings."""
    config = {}
    warnings = []
    
    # Voice ID validation
    voice_id = os.getenv('CARTESIA_VOICE_ID')
    if voice_id:
        if not voice_id.strip():
            warnings.append("Empty CARTESIA_VOICE_ID, using default voice")
        else:
            config['voice'] = {'id': voice_id}
    
    # Model validation
    model = os.getenv('CARTESIA_MODEL', 'sonic-2')
    if model not in ['sonic-2', 'sonic']:
        warnings.append(f"Unknown model {model}, using default sonic-2")
        model = 'sonic-2'
    config['model'] = model
    
    # Language validation
    language = os.getenv('CARTESIA_LANGUAGE', 'en')
    config['language'] = language
    
    # Sample rate validation
    try:
        sample_rate = int(os.getenv('CARTESIA_SAMPLE_RATE', '44100'))
        if sample_rate not in [22050, 44100, 48000]:
            warnings.append(f"Unusual sample rate {sample_rate}Hz. Supported: 22050, 44100, 48000")
    except ValueError:
        warnings.append("Invalid CARTESIA_SAMPLE_RATE, using default 44100Hz")
        sample_rate = 44100
    
    # Encoding validation
    encoding = os.getenv('CARTESIA_ENCODING', 'pcm_f32le')
    if encoding not in ['pcm_f32le', 'pcm_s16le']:
        warnings.append(f"Unusual encoding {encoding}, using default pcm_f32le")
        encoding = 'pcm_f32le'
    
    config['output_format'] = {
        'container': 'raw',
        'sample_rate': sample_rate,
        'encoding': encoding,
    }
    
    return config, warnings

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
    
    # Configure VAD with extremely conservative settings to prevent TTS interruption
    vad.min_silence_duration_ms = 5000  # Very long silence detection to prevent TTS feedback
    vad.speaking_probability_threshold = 0.98  # Very high threshold to reduce false triggers
    vad.min_speaking_duration_ms = 3000  # Require very long sustained speech to avoid TTS interruption
    
    # Configure STT with balanced settings
    stt = deepgram.STT(
        model="nova-2",  # Use the latest model
        language="en-US",
        interim_results=True,  # Enable interim results
        endpointing_ms=1500,  # Wait 1.5s of silence before considering speech complete
    )
    
    # Configure TTS with fallback options
    cartesia_api_key = os.getenv('CARTESIA_API_KEY')
    openai_api_key = os.getenv('OPENAI_API_KEY')
    
    if cartesia_api_key and cartesia_api_key != 'your_cartesia_api_key':
        try:
            # Validate Cartesia configuration
            tts_config, warnings = validate_cartesia_config()
            
            # Print warnings if any
            for warning in warnings:
                print(f"⚠️ Warning: {warning}")
            
            # Print configuration details
            voice_id = os.getenv('CARTESIA_VOICE_ID')
            if voice_id and voice_id.strip():
                print(f"✅ Using Cartesia TTS with voice ID: {voice_id}")
            else:
                print("✅ Using Cartesia TTS with default voice")
            
            print(f"   - Model: {tts_config['model']}")
            print(f"   - Language: {tts_config['language']}")
            print(f"   - Sample Rate: {tts_config['output_format']['sample_rate']}Hz")
            print(f"   - Encoding: {tts_config['output_format']['encoding']}")
            
            # Initialize Cartesia TTS with configuration
            tts = cartesia.TTS(**tts_config)
            
        except Exception as e:
            print(f"⚠️ Cartesia TTS failed: {e}")
            if openai_api_key and openai_api_key != 'your_openai_api_key':
                print("🔄 Falling back to OpenAI TTS...")
                tts = openai.TTS()
            else:
                print("❌ No valid TTS API keys found. Please check your .env file.")
                raise
    elif openai_api_key and openai_api_key != 'your_openai_api_key':
        print("🔄 Using OpenAI TTS (Cartesia not configured)")
        tts = openai.TTS()
    else:
        print("❌ No valid TTS API keys found. Please configure Cartesia or OpenAI in your .env file.")
        raise ValueError("No TTS provider configured")
    
    # Try without VAD entirely to prevent interruption
    session = AgentSession(
        llm=llm,
        stt=stt,
        tts=tts,
        # vad=vad,  # Disable VAD entirely to prevent TTS interruption
    )

    # Advanced audio feedback prevention system without VAD
    class AudioFeedbackPrevention:
        def __init__(self):
            self.is_tts_playing = False
            self.last_tts_time = 0
            
            # Configurable via environment variables
            self.feedback_cooldown = float(os.getenv('AUDIO_FEEDBACK_COOLDOWN', '1.0'))
            self.consecutive_feedback_attempts = 0
            self.max_feedback_attempts = int(os.getenv('AUDIO_MAX_FEEDBACK_ATTEMPTS', '3'))
            self.adaptive_cooldown = os.getenv('AUDIO_ADAPTIVE_COOLDOWN', 'true').lower() == 'true'
            
            # Smart duration estimation settings
            self.words_per_minute = float(os.getenv('TTS_WORDS_PER_MINUTE', '140'))
            self.safety_multiplier = float(os.getenv('TTS_SAFETY_MULTIPLIER', '1.5'))
            self.min_mute_duration = float(os.getenv('TTS_MIN_MUTE_DURATION', '0.5'))
            self.max_mute_duration = float(os.getenv('TTS_MAX_MUTE_DURATION', '15.0'))
            self.last_tts_text = ""
            
        def estimate_tts_duration(self, text):
            """Estimate TTS duration based on text length with enhanced safety"""
            # Count words in the text
            word_count = len(text.split())
            
            # Count punctuation marks that might slow down speech
            punctuation_count = text.count('.') + text.count('!') + text.count('?') + text.count(',') + text.count(';') + text.count(':')
            
            # Count emojis and special characters that might add pause
            emoji_count = len([c for c in text if ord(c) > 127])
            
            # Calculate base duration based on words per minute
            duration_minutes = word_count / self.words_per_minute
            duration_seconds = duration_minutes * 60
            
            # Add extra time for punctuation pauses (0.2s per punctuation mark)
            punctuation_pause = punctuation_count * 0.2
            
            # Add extra time for emojis and special characters (0.1s each)
            emoji_pause = emoji_count * 0.1
            
            # Apply safety multiplier and add pauses
            estimated_duration = (duration_seconds + punctuation_pause + emoji_pause) * self.safety_multiplier
            estimated_duration = max(estimated_duration, self.min_mute_duration)
            estimated_duration = min(estimated_duration, self.max_mute_duration)
            
            return estimated_duration
            
        def on_tts_start(self, text=""):
            """Called when TTS starts playing"""
            self.is_tts_playing = True
            self.last_tts_time = time.time()
            self.last_tts_text = text  # Store text for duration estimation
            
            # Estimate duration if text is provided
            if text:
                estimated_duration = self.estimate_tts_duration(text)
                word_count = len(text.split())
                punctuation_count = text.count('.') + text.count('!') + text.count('?') + text.count(',') + text.count(';') + text.count(':')
                emoji_count = len([c for c in text if ord(c) > 127])
                print(f"🔇 TTS started - NO VAD active, estimated duration ~{estimated_duration:.1f}s (estimated from {word_count} words, {punctuation_count} punctuation, {emoji_count} emojis)")
            else:
                print("🔇 TTS started - NO VAD active for feedback prevention")
            
        def on_tts_end(self):
            """Called when TTS stops playing"""
            self.is_tts_playing = False
            print("🎤 TTS ended - NO VAD system active")
            
        def should_process_audio(self, audio_data=None):
            """Determine if audio should be processed to prevent feedback"""
            current_time = time.time()
            
            # Always block during TTS
            if self.is_tts_playing:
                return False
                
            # Smart duration-based blocking using stored text
            if self.last_tts_text:
                estimated_duration = self.estimate_tts_duration(self.last_tts_text)
                if current_time - self.last_tts_time < estimated_duration:
                    return False
            else:
                # Fallback to cooldown period if no text available
                if current_time - self.last_tts_time < self.feedback_cooldown:
                    return False
                
            # Reset feedback counter if enough time has passed
            if current_time - self.last_tts_time > 10.0:
                self.consecutive_feedback_attempts = 0
                
            return True
            
        def on_feedback_detected(self):
            """Handle detected feedback"""
            self.consecutive_feedback_attempts += 1
            print(f"⚠️ Audio feedback detected (attempt {self.consecutive_feedback_attempts})")
            
            if self.consecutive_feedback_attempts >= self.max_feedback_attempts and self.adaptive_cooldown:
                print("🚨 Maximum feedback attempts reached - extending cooldown")
                self.feedback_cooldown = min(self.feedback_cooldown * 1.5, 10.0)  # Cap at 10s
                self.consecutive_feedback_attempts = 0
    
    feedback_prevention = AudioFeedbackPrevention()
    
    # Enhanced audio feedback prevention
    print("🔇 NO VAD audio feedback prevention enabled")
    print(f"   - VAD COMPLETELY DISABLED to prevent TTS interruption")
    print(f"   - Balanced STT endpointing (1.5s silence detection)")
    print(f"   - Enhanced TTS duration estimation ({feedback_prevention.words_per_minute} WPM, {feedback_prevention.safety_multiplier}x safety + punctuation/emoji pauses)")
    print(f"   - Fallback cooldown period ({feedback_prevention.feedback_cooldown}s after TTS completion)")
    print(f"   - Mute duration range: {feedback_prevention.min_mute_duration}s - {feedback_prevention.max_mute_duration}s")
    print(f"   - Feedback detection and adaptive cooldown: {feedback_prevention.adaptive_cooldown}")
    print(f"   - Max feedback attempts: {feedback_prevention.max_feedback_attempts}")
    print("🎯 NO VAD = NO INTERRUPTION - TTS should play completely uninterrupted")

    # Start the session with the room and agent
    await session.start(
        room=ctx.room,
        agent=Agent(instructions=""), # instructions should be set in the Letta agent
    )

    # Enhanced say method with smart duration-based feedback prevention
    async def say_with_feedback_prevention(text):
        """Say text with smart duration-based feedback prevention"""
        feedback_prevention.on_tts_start(text)  # Pass text for duration estimation
        try:
            await session.say(text)
        finally:
            feedback_prevention.on_tts_end()

    await say_with_feedback_prevention("Hi, what's your name?")
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