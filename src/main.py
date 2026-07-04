from sponsor_loader import load_sponsors, build_lookup
from job_search import search_jobs
from matcher import match_jobs


def main():
    print("=" * 60)
    print("SponsorJobScanner v1.0")
    print("=" * 60)

    # --------------------------------------------------
    # Load Sponsor Companies
    # --------------------------------------------------
    print("\nLoading sponsor companies...")

    sponsors = load_sponsors()
    lookup = build_lookup(sponsors)

    print(f"Loaded {len(sponsors):,} sponsor companies")
    print(f"Unique cleaned names: {len(lookup):,}")

    # --------------------------------------------------
    # Search Live Jobs
    # --------------------------------------------------
    print("\nSearching live jobs...")

    jobs = search_jobs()

    print(f"\nTotal jobs found: {len(jobs):,}")

    if jobs.empty:
        print("\nNo jobs found.")
        return

    # --------------------------------------------------
    # Match Sponsor Companies
    # --------------------------------------------------
    print("\nMatching sponsor companies...")

    matched_jobs = match_jobs(
    jobs,
    lookup
)

    print(f"\nSponsor jobs found: {len(matched_jobs):,}")

    if matched_jobs.empty:
        print("\nNo sponsor jobs matched.")
        return

    # --------------------------------------------------
    # Display Results
    # --------------------------------------------------
    print("\nFirst 20 matched jobs:\n")

    print(
        matched_jobs[
            [
                "company",
                "matched_company",
                "title",
                "location",
                "match_score",
                "match_type",
            ]
        ].head(20)
    )


if __name__ == "__main__":
    main()