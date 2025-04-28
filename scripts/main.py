from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

print("Hello World")
print(api_key)
