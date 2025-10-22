#!/bin/env python

from src import agent_helper, path_helper

import argparse
import asyncio
import geocoder

from agents import (
    Agent,
    function_tool,
)

# TODO:
# try prompt_toolkit for async input that doesnt happen when other async functions run


async def main():
    parser = argparse.ArgumentParser(
        description="Simple CLI irrigation agent")
    parser.add_argument(
        "-c", "--config-path",
        help="The path to the custom config json file",
        dest="config_path"
    )

    args = parser.parse_args()
    path = args.config_path if args.config_path else path_helper.get_config_path(
        __file__, "agent_default.json")

    agent = agent_helper.get_and_configure_agent(path, [get_user_location])
    await run_agent(agent)


@function_tool
async def get_user_location() -> str:
    print("---GETTING USER LOCATION---")
    g = geocoder.ip("me")
    return str(g)


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
        response = await agent_helper.run_and_print_agent_streamed(agent, prompt, prev_id)


if __name__ == "__main__":
    asyncio.run(main())
