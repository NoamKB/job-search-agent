# src/main.py

from job_api import search_jobs
from filters import filter_by_keywords, filter_by_location, filter_by_min_salary
from dotenv import load_dotenv
import os
from llm_agent import summarize_jobs

load_dotenv()

print("Environment works!")
print("JOB_API_KEY:", os.getenv("JOB_API_KEY"))

# Fetch jobs with country restriction directly from the API
jobs = search_jobs(query="Data", location="Israel", num_jobs=100)

print(f"\n>> Jobs found before filtering: {len(jobs)}")

# Temporarily disable local filtering to see what the API returns
print("\n--- Raw locations from API ---")
for job in jobs:
    print(f"  - Location: {job.get('location')}")
print("-----------------------------\n")

# Define filters
keywords = ["ai", "analyst", "data", "ml", "machine learning"]
allowed_locations = ["israel", "il", "isr", "tel aviv", "jerusalem", "Tel Aviv-Yafo"]
min_salary = 15000

# Apply filters
jobs = filter_by_keywords(jobs, keywords)
#jobs = filter_by_location(jobs, allowed_locations)
jobs = filter_by_min_salary(jobs, min_salary)

print(f">> Jobs found after filtering: {len(jobs)}\n")

# Print jobs that passed filters
for i, job in enumerate(jobs, 1):
    print(f"{i}. {job['title']} at {job['company']} ({job['location']})")
    print(f"   Apply here: {job['url']}")

# Ask Claude to summarize and rank the jobs
summary = summarize_jobs(jobs)
print("\n--- Claude's Analysis ---")
print(summary)
