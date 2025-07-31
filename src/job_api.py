import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("JOB_API_KEY")
BASE_URL = "https://jsearch.p.rapidapi.com/search"

headers = {
    "x-rapidapi-host": "jsearch.p.rapidapi.com",
    "x-rapidapi-key": API_KEY
}

def search_jobs(query="Data", location="Israel", num_jobs=100):
    """
    Fetch multiple pages of jobs from JSearch API until we reach num_jobs or run out of results.
    """
    all_jobs = []
    page = 1
    jobs_per_page = 10  # API default

    while len(all_jobs) < num_jobs:
        params = {
            "query": query,
            "country": "il",  # use Israel country code
            "page": page,
            "num_pages": 1  # only one page at a time
        }

        response = requests.get(BASE_URL, headers=headers, params=params)
        if response.status_code != 200:
            print("Error:", response.status_code, response.text)
            break

        data = response.json()
        jobs = data.get("data", [])
        if not jobs:
            break  # No more jobs available

        all_jobs.extend(jobs)
        page += 1

    # Trim the list to requested number
    all_jobs = all_jobs[:num_jobs]

    # Map jobs to a clean dictionary
    return [
        {
            "title": job.get("job_title", ""),
            "company": job.get("employer_name", ""),
            "location": job.get("job_city") or job.get("job_country", "Remote"),
            "url": job.get("job_apply_link", ""),
            "salary": str(job.get("job_max_salary", ""))
        }
        for job in all_jobs
    ]
