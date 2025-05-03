from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner


async def run_and_print_agent_streamed(
    agent: Agent, prompt: str, previous_response_id: str | None
):
    result = Runner.run_streamed(
        agent, prompt, previous_response_id=previous_response_id
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)
