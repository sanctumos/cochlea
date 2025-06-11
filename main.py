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
    session = AgentSession(
        llm=openai.LLM.with_letta(
            agent_id=agent_id,
        ),
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
    # check that agent exists
    client = Letta(token=os.getenv('LETTA_API_KEY'))

    # create the Letta agent
    agent = client.agents.create(
        name="low_latency_voice_agent_demo",
        agent_type="voice_convo_agent",
        memory_blocks=[
            {"value": "Name: ?", "label": "human"},
            {"value": "You are a helpful assistant.", "label": "persona"},
        ],
        model="openai/gpt-4o-mini", # Use 4o-mini for speed
        embedding="openai/text-embedding-3-small",
        enable_sleeptime=True,
        initial_message_sequence = [],
    )
    print(f"Created agent id {agent.id}")

    # configure the sleep-time agent 
    group_id = agent.multi_agent_group.id
    max_message_buffer_length = agent.multi_agent_group.max_message_buffer_length
    min_message_buffer_length = agent.multi_agent_group.min_message_buffer_length
    print(f"Group id: {group_id}, max_message_buffer_length: {max_message_buffer_length},  min_message_buffer_length: {min_message_buffer_length}")
    # change it to be more frequent
    group = client.groups.modify(
        group_id=group_id,
        manager_config=VoiceSleeptimeManagerUpdate(
            max_message_buffer_length=10,
            min_message_buffer_length=6,
        )
    )

    # update the sleep-time agent model 
    sleeptime_agent_id = [agent_id for agent_id in group.agent_ids if agent_id != agent.id][0]
    client.agents.modify(
        agent_id=sleeptime_agent_id,
        model="anthropic/claude-sonnet-4-20250514"
    )

    # Set the agent id in environment variable so it's accessible in the worker process
    os.environ['LETTA_AGENT_ID'] = agent.id
    print(f"Agent id: {agent.id}")

    # Now that LETTA_AGENT_ID is set, run the worker app
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))