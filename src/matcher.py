import pandas as pd
from rapidfuzz import fuzz

from utils import clean_company_name


# ----------------------------------------------------
# Exact Match
# ----------------------------------------------------

def exact_match(jobs, lookup):

    matches = []

    matched_companies = set()

    for _, job in jobs.iterrows():

        company = str(job["company"])

        clean = clean_company_name(company)

        if clean in lookup:

            row = job.copy()

            row["matched_company"] = lookup[clean]["original"]
            row["match_score"] = 100
            row["match_type"] = "Exact"

            matches.append(row)

            matched_companies.add(clean)

    return pd.DataFrame(matches), matched_companies


# ----------------------------------------------------
# Contains Match
# ----------------------------------------------------

def contains_match(jobs, lookup, matched_companies):

    matches = []

    for _, job in jobs.iterrows():

        company = str(job["company"])

        clean = clean_company_name(company)

        if clean in matched_companies:
            continue

        for sponsor in lookup.keys():

            if clean in sponsor or sponsor in clean:

                row = job.copy()

                row["matched_company"] = lookup[sponsor]["original"]
                row["match_score"] = 95
                row["match_type"] = "Contains"

                matches.append(row)

                matched_companies.add(clean)

                break

    return pd.DataFrame(matches), matched_companies


# ----------------------------------------------------
# Final Match Function
# ----------------------------------------------------

def match_jobs(jobs, lookup):

    exact, matched = exact_match(
        jobs,
        lookup
    )

    contains, matched = contains_match(
        jobs,
        lookup,
        matched
    )

    results = pd.concat(
        [
            exact,
            contains
        ],
        ignore_index=True
    )

    return results