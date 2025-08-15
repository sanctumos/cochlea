import os

from dotenv import load_dotenv
from letta_client import Letta, VoiceSleeptimeManagerUpdate


from livekit import agents
from livekit.agents import AgentSession, Agent, AutoSubscribe
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
)
load_dotenv()

async def entrypoint(ctx: agents.JobContext):
    agent_id = os.environ.get('LETTA_AGENT_ID')
    print(f"Agent id: {agent_id}")
    
    # Build Letta configuration dynamically from environment
    letta_config = {'agent_id': agent_id}
    
    # Add base_url if specified (for self-hosted instances)
    base_url = os.getenv('LETTA_BASE_URL')
    if base_url:
        letta_config['base_url'] = base_url
        print(f"Connecting to self-hosted Letta at: {base_url}")
    else:
        print("Connecting to Letta Cloud")
    
    session = AgentSession(
        llm=openai.LLM.with_letta(**letta_config),
        stt=deepgram.STT(),
        tts=cartesia.TTS(),
    )

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