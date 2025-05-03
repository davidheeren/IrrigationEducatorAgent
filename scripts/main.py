from dotenv import load_dotenv
import json
from agents import Agent, Runner

# Load environment variables from .env file
load_dotenv()

with open("config/agent_config.json", "r") as acf:
    agent_config = json.load(acf)

agent = Agent(
    name=agent_config["name"],
    instructions=agent_config["instructions"],
    model=agent_config["model"],
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
