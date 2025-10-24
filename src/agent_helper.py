from typing import List
from dotenv import load_dotenv
import json

from agents import (
    Agent,
    FileSearchTool,
    ModelSettings,
    Tool,
    WebSearchTool,
    function_tool,
)

from agents.result import RunResultBase
from openai.types.responses import ResponseTextDeltaEvent
from agents import Runner


# print response from API as tokens are streamed
async def run_and_print_agent_streamed(agent: Agent, prompt: str, previous_response_id: str | None) -> RunResultBase:
    response = Runner.run_streamed(
        agent, prompt, previous_response_id=previous_response_id
    )
    async for event in response.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            print(event.data.delta, end="", flush=True)
    print()
    return response


# make new agent from a config path and function tools
def get_and_configure_agent(config_path: str, function_tools: List[function_tool]) -> Agent:
    load_dotenv()
    with open(config_path, "r") as acf:
        agent_config = json.load(acf)

    tools = _configure_tools(agent_config, function_tools)

    settings = ModelSettings(
        temperature=agent_config["temperature"],
        max_tokens=agent_config["max_tokens"],
        truncation="auto",
    )

    return Agent(
        name=agent_config["name"],
        instructions=agent_config["instructions"],
        model=agent_config["model"],
        tools=tools,
        model_settings=settings,
    )


# add tool capabilites to agent
def _configure_tools(agent_config: str, function_tools: List[function_tool]) -> List[Tool]:
    tools = []
    file_search_config = agent_config["tools"]["file_search"]
    if file_search_config["enabled"]:
        tools.append(
            FileSearchTool(
                file_search_config["vector_store_ids"],
                file_search_config["max_num_results"],
                file_search_config["include_search_results"],
            )
        )

    web_search_config = agent_config["tools"]["web_search"]
    if web_search_config["enabled"]:
        tools.append(WebSearchTool())

    tools.extend(function_tools)

    return tools
