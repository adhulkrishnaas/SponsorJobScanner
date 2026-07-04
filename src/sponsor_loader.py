import pandas as pd
from utils import clean_company_name


def load_sponsors():
    sponsors = pd.read_csv("data/sponsor_list.csv")

    sponsors["clean_name"] = (
        sponsors["Organisation Name"]
        .fillna("")
        .apply(clean_company_name)
    )

    return sponsors


def build_lookup(sponsors):
    lookup = {}

    for _, row in sponsors.iterrows():

        lookup[row["clean_name"]] = {

            "original": row["Organisation Name"],

            "city": row["Town/City"],

            "route": row["Route"]

        }

    return lookup