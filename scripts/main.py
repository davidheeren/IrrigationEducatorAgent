from dotenv import load_dotenv
import json
from agents import Agent, FileSearchTool, Runner, WebSearchTool

# Load environment variables from .env file
load_dotenv()

with open("config/agent_config.json", "r") as acf:
    agent_config = json.load(acf)

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

agent = Agent(
    name=agent_config["name"],
    instructions=agent_config["instructions"],
    model=agent_config["model"],
    tools=tools,
)

seperator = "-" * 50
print(f"\nWelcome to '{agent.name}', your terminal AI assistant")
print("Enter 'q' to quit")

response = None
while True:
    print(seperator)
    prompt = input("Prompt: ")
    if prompt.strip().lower() == "q":
        break
    if response:
        response = Runner.run_sync(
            agent, prompt, previous_response_id=response.last_response_id
        )
    else:
        response = Runner.run_sync(agent, prompt)
    print(f"~\nResponse: {response.final_output}")
