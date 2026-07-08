import re

BRANDS = [

    "boat",
    "noise",
    "jbl",
    "sony",
    "logitech",
    "hp",
    "dell",
    "lenovo",
    "samsung",
    "realme",
    "oneplus",
    "redmi",
    "mi",
    "apple",
    "ambrane",
    "portronics",
    "zebronics",
    "philips",
    "sandisk",
    "kingston",
    "crucial",
    "wd",
    "seagate",
    "marshall",
    "fastrack",
    "fire-boltt",
    "fireboltt",
    "crossbeats",
    "anker",
    "belkin"

]


def detect_brand(query):

    query = query.lower()

    query = re.sub(r"[^a-z0-9\- ]", " ", query)

    for brand in BRANDS:

        if brand in query:

            return brand

    return None