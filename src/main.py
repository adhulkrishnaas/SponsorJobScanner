from sponsor_loader import load_sponsors

print("=" * 50)
print("SponsorJobScanner")
print("=" * 50)

print()

print("Loading sponsor list...")

sponsors = load_sponsors()
from utils import clean_company_name

print()

for company in sponsors["Organisation Name"].head(10):

    print(company)

    print(" ↓ ")

    print(clean_company_name(company))

    print()

print()

print(sponsors.head())