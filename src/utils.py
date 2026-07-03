import re

REMOVE_WORDS = {
    "limited",
    "ltd",
    "plc",
    "llp",
    "uk",
    "services",
    "service",
    "group",
    "holdings",
    "holding",
    "international",
    "company",
    "co"
}


def clean_company_name(name):

    if not isinstance(name, str):
        return ""

    name = name.lower()

    name = re.sub(r"[^a-z0-9 ]", "", name)

    words = name.split()

    words = [
        word
        for word in words
        if word not in REMOVE_WORDS
    ]

    return " ".join(words)