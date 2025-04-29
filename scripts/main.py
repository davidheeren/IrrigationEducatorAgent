from dotenv import load_dotenv
import os
import openai
import json

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

print("Hello World")
print(f"API: {api_key}")

with open("config/agent_config.json", "r") as acf:
    agent_config = json.load(acf)

# unknown is the default string if the json object does not contain the key
agent_name = agent_config.get("name", "unknown")
print(f"agent name: {agent_name}")
