# src/main.py

from job_api import search_jobs
from filters import filter_by_keywords, filter_by_location, filter_by_min_salary
from dotenv import load_dotenv
import os
from llm_agent import summarize_jobs

load_dotenv()

print("Environment works!")
print("JOB_API_KEY:", os.getenv("JOB_API_KEY"))

# Fetch jobs without country restriction
jobs = search_jobs(query="Data", location="", num_jobs=50)

print(f"\n>> Jobs found before filtering: {len(jobs)}")

# Define filters
keywords = ["ai", "analyst", "data", "ml", "machine learning"]
allowed_locations = ["israel", "il", "isr", "remote", "hybrid", "tel aviv", "jerusalem", "middle east"]
min_salary = 15000

# Debugging before filtering
for job in jobs:
    print("Job location:", job.get('location'))

# Apply filters
jobs = filter_by_keywords(jobs, keywords)
jobs = filter_by_location(jobs, allowed_locations)
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
