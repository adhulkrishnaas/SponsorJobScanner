import pandas as pd

def load_sponsors():

    sponsors = pd.read_csv(
        "data/sponsor_list.csv"
    )

    return sponsors