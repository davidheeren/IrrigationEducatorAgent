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
import src.helper
import asyncio
import geocoder


async def main():
    load_dotenv()
    with open("config/agent_config.json", "r") as acf:
        agent_config = json.load(acf)

    tools = configure_tools(agent_config)

    settings = ModelSettings(
        temperature=agent_config["temperature"],
        max_tokens=agent_config["max_tokens"],
        truncation="auto",
    )

    agent = Agent(
        name=agent_config["name"],
        instructions=agent_config["instructions"],
        model=agent_config["model"],
        tools=tools,
        model_settings=settings,
    )

    await run_agent(agent)


@function_tool
async def get_user_location() -> str:
    print("---GETTING USER LOCATION---")
    g = geocoder.ip("me")
    return str(g)


def configure_tools(agent_config) -> List[Tool]:
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

    tools.append(get_user_location)

    return tools


async def run_agent(agent: Agent):
    seperator = "-" * 50
    print(f"\nWelcome to '{agent.name}', your terminal AI assistant")
    print("Enter 'q' to quit")

    response = None
    while True:
        print(seperator)
        prompt = input("Prompt: ")
        if prompt.strip().lower() == "q":
            break

        prev_id = response.last_response_id if response else None
        print("~\nResponse: ", end="")
        response = await src.helper.run_and_print_agent_streamed(agent, prompt, prev_id)


if __name__ == "__main__":
    asyncio.run(main())
