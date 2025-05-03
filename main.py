from typing import List
from dotenv import load_dotenv
import json
from agents import Agent, FileSearchTool, Tool, WebSearchTool
import src.helper
import asyncio


async def main():
    load_dotenv()
    with open("config/agent_config.json", "r") as acf:
        agent_config = json.load(acf)

    tools = configure_tools(agent_config)

    agent = Agent(
        name=agent_config["name"],
        instructions=agent_config["instructions"],
        model=agent_config["model"],
        tools=tools,
    )

    await run_agent(agent)


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
        # response = Runner.run_sync(agent, prompt, previous_response_id=prev_id)
        print("~")
        await src.helper.run_and_print_agent_streamed(agent, prompt, prev_id)


if __name__ == "__main__":
    asyncio.run(main())
