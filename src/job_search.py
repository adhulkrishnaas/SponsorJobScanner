from jobspy import scrape_jobs
import pandas as pd

from config import (
    SEARCH_TERMS,
    LOCATION,
    RESULTS_PER_SEARCH,
    JOB_SITES
)


def search_jobs():

    all_jobs = []

    for term in SEARCH_TERMS:

        print(f"\nSearching: {term}")

        jobs = scrape_jobs(
            site_name=JOB_SITES,
            search_term=term,
            location=LOCATION,
            results_wanted=RESULTS_PER_SEARCH,
            hours_old=168,
            country_indeed="UK"
        )

        print(f"Found {len(jobs)} jobs")

        all_jobs.append(jobs)

    if len(all_jobs) == 0:
        return pd.DataFrame()

    jobs = pd.concat(
        all_jobs,
        ignore_index=True
    )

    jobs = jobs.drop_duplicates(
        subset=["job_url"]
    )

    return jobs