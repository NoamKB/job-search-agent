# src/filters.py

def filter_by_keywords(jobs, keywords):
    """
    Filter jobs by keywords in the job title.
    """
    return [
        job for job in jobs
        if any(kw.lower() in job['title'].lower() for kw in keywords)
    ]
    
def filter_by_location(jobs, allowed_locations):
    """
    Filter jobs by location (e.g., Remote, Hybrid, On-site in Israel).
    Uses case-insensitive and partial matching.
    """
    allowed = [loc.lower().strip() for loc in allowed_locations]
    filtered = []
    for job in jobs:
        job_loc = (job.get('location') or '').lower().strip()
        if any(loc in job_loc for loc in allowed):
            filtered.append(job)
    return filtered

def filter_by_min_salary(jobs, min_salary):
    """
    Filter jobs by minimum salary if salary information is available.
    Jobs without salary data will still be included for now.
    """
    filtered = []
    for job in jobs:
        salary = job.get('salary', '')
        # Try to parse salary if it's numeric
        if salary and salary.isnumeric():
            if int(salary) >= min_salary:
                filtered.append(job)
        else:
            # Keep jobs without salary data
            filtered.append(job)
    return filtered
