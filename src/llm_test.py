from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI  # for OpenAI
from langchain_anthropic import ChatAnthropic  # for Anthropic if needed

load_dotenv()  # Load .env keys

openai_key = os.getenv("OPENAI_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

print("OpenAI Key Loaded:", bool(openai_key))
print("Anthropic Key Loaded:", bool(anthropic_key))

# Initialize LangChain LLM of openai
# llm = ChatOpenAI(openai_api_key=openai_key, model="gpt-3.5-turbo")

# Initialize Claude LLM
llm = ChatAnthropic(api_key=anthropic_key, model_name="claude-3-5-sonnet-20240620")

# Test prompt
response = llm.invoke("Write a one-line motivational quote about AI learning.")
print(response.content)
