# src/llm_agent.py

from dotenv import load_dotenv
import os
from langchain_anthropic import ChatAnthropic

load_dotenv()

# Load Claude (Anthropic) API key
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

# Initialize Claude
llm = ChatAnthropic(api_key=anthropic_key, model_name="claude-3-5-sonnet-20240620")

def summarize_jobs(jobs):
    """
    Use Claude to summarize and rank job postings.
    """
    if not jobs:
        return "No jobs available to summarize."

    # Build a prompt for Claude
    job_list_text = "\n".join(
        [f"{i+1}. {job['title']} at {job['company']} ({job['location']})" for i, job in enumerate(jobs)]
    )
    prompt = f"""
    You are an expert career assistant. Here are some job postings:

    {job_list_text}

    Please:
    1. Summarize the jobs in 3-4 sentences.
    2. Highlight which ones are most relevant for someone with AI/Data experience.
    3. Suggest the top 2 jobs to apply for first.
    """

    response = llm.invoke(prompt)
    return response.content
