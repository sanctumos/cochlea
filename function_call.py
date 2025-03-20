import logging
import random
import time
from typing import Annotated

import aiohttp
from dotenv import load_dotenv
from livekit.agents import (
    AutoSubscribe,
    JobContext,
    JobProcess,
    WorkerOptions,
    cli,
    llm,
    metrics,
)
from livekit.agents.pipeline import AgentCallContext, VoicePipelineAgent
from livekit.plugins import deepgram, openai, silero
from livekit.agents.metrics import PipelineLLMMetrics, PipelineTTSMetrics

load_dotenv()

logger = logging.getLogger("weather-demo")
logger.setLevel(logging.INFO)


class LatencyTracker:
    """Tracks and stores latency metrics per invocation."""

    def __init__(self):
        self.current_invocation = {"llm_ttft": None, "tts_ttfb": None}
        self.collected_invocations = []

    def update_metric(self, mtrcs: metrics.AgentMetrics):
        """Updates stored metrics for the current invocation based on metric type."""
        if isinstance(mtrcs, PipelineLLMMetrics) and mtrcs.ttft >= 0:
            self.current_invocation["llm_ttft"] = mtrcs.ttft
        elif isinstance(mtrcs, PipelineTTSMetrics) and mtrcs.ttfb >= 0:
            self.current_invocation["tts_ttfb"] = mtrcs.ttfb

        if all(val is not None for val in self.current_invocation.values()):
            self._store_invocation()

    def _store_invocation(self):
        """Stores completed invocation metrics and resets tracker."""
        total_latency = sum(self.current_invocation.values())
        self.collected_invocations.append(
            {**self.current_invocation, "total_latency": total_latency}
        )
        logger.debug(f"Stored invocation metrics: {self.current_invocation}")

        self.current_invocation = {"llm_ttft": None, "tts_ttfb": None}

    def calculate_summary(self):
        """Returns computed summary statistics from collected invocations."""
        if not self.collected_invocations:
            return None

        count = len(self.collected_invocations)
        total_llm = sum(row["llm_ttft"] for row in self.collected_invocations)
        total_tts = sum(row["tts_ttfb"] for row in self.collected_invocations)
        total_latency = sum(row["total_latency"] for row in self.collected_invocations)

        return {
            "total_invocations": count,
            "avg_llm_ttft": total_llm / count,
            "avg_tts_ttfb": total_tts / count,
            "avg_total_latency": total_latency / count,
        }


class AssistantFnc(llm.FunctionContext):
    """
    The class defines a set of LLM functions that the assistant can execute.
    """

    @llm.ai_callable()
    async def get_weather(
        self,
        location: Annotated[
            str, llm.TypeInfo(description="The location to get the weather for")
        ],
        latitude: Annotated[
            str,
            llm.TypeInfo(description="The latitude of location to get the weather for"),
        ],
        longitude: Annotated[
            str,
            llm.TypeInfo(
                description="The longitude of location to get the weather for"
            ),
        ],
    ):
        """Called when the user asks about the weather."""

        agent = AgentCallContext.get_current().agent

        if (
            not agent.chat_ctx.messages
            or agent.chat_ctx.messages[-1].role != "assistant"
        ):
            message = random.choice(
                [
                    f"Let me check the weather in {location} for you.",
                    f"Let me see what the weather is like in {location} right now.",
                    f"The current weather in {location} is ",
                ]
            )
            logger.info(f"saying filler message: {message}")
            speech_handle = await agent.say(message, add_to_chat_ctx=True)  # noqa: F841

        logger.info(f"getting weather for {latitude}, {longitude}")

        start_time = time.time()
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
        weather_data = {}

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    weather_data = {
                        "temperature": data["current"]["temperature_2m"],
                        "temperature_unit": "Celsius",
                    }
                    logger.info(f"weather data: {weather_data}")
                else:
                    raise Exception(
                        f"Failed to get weather data, status code: {response.status}"
                    )

        duration = time.time() - start_time
        logger.info(f"Weather API call latency: {duration:.2f} seconds")

        return weather_data


def prewarm_process(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = AssistantFnc()
    initial_chat_ctx = llm.ChatContext().append(
        text=(
            "You are a weather assistant created by LiveKit. Your interface with users will be voice. "
            "You will provide weather information for a given location. "
            "do not return any text while calling the function."
        ),
        role="system",
    )
    participant = await ctx.wait_for_participant()
    agent = VoicePipelineAgent(
        vad=ctx.proc.userdata["vad"],
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-4o-mini"),
        tts=openai.TTS(),
        fnc_ctx=fnc_ctx,
        chat_ctx=initial_chat_ctx,
    )

    agent.start(ctx.room, participant)

    usage_collector = metrics.UsageCollector()
    latency_tracker = LatencyTracker()

    @agent.on("metrics_collected")
    def _handle_metrics_collected(mtrcs: metrics.AgentMetrics):
        """Handles metric collection per invocation."""
        metrics.log_metrics(mtrcs)
        usage_collector.collect(mtrcs)
        latency_tracker.update_metric(mtrcs)

    async def _log_usage_summary():
        """Logs collected usage and invocation latency metrics."""
        summary = usage_collector.get_summary()
        logger.info(f"Usage Summary: {summary}")

        latency_summary = latency_tracker.calculate_summary()
        if latency_summary is None:
            logger.info("No invocation metrics were collected.")
            return

        logger.info("Invocation Metrics Summary:")
        logger.info(f"  Total Invocations: {latency_summary['total_invocations']}")
        logger.info(f"  Average LLM TTFT: {latency_summary['avg_llm_ttft']:.2f} seconds")
        logger.info(f"  Average TTS TTFB: {latency_summary['avg_tts_ttfb']:.2f} seconds")
        logger.info(f"  Average Total Latency: {latency_summary['avg_total_latency']:.2f} seconds")

        for idx, row in enumerate(latency_tracker.collected_invocations, start=1):
            logger.info(
                f"Invocation {idx}: "
                f"LLM TTFT = {row['llm_ttft']:.2f}s, "
                f"TTS TTFB = {row['tts_ttfb']:.2f}s, "
                f"Total Latency = {row['total_latency']:.2f}s"
            )

    ctx.add_shutdown_callback(_log_usage_summary)

    await agent.say(
        "Hello from the weather station. Would you like to know the weather? If so, tell me your location."
    )


if __name__ == "__main__":
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            prewarm_fnc=prewarm_process,
        ),
    )
