import re
from difflib import SequenceMatcher
from .category_mapper import detect_category
from .brand_mapper import detect_brand


SYNONYMS = {
    "earbuds": ["earphones", "airdopes", "tws"],
    "earphones": ["earbuds", "airdopes", "tws"],
    "headphones": ["headset"],
    "speaker": ["bluetooth speaker", "portable speaker"],
    "charger": ["adapter"],
    "mouse": ["wireless mouse", "gaming mouse"],
    "keyboard": ["mechanical keyboard", "wireless keyboard"],
    "ssd": ["solid state drive"],
    "pendrive": ["usb drive", "flash drive"],
    "watch": ["smartwatch", "smart watch"]
}


def normalize_query(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def expand_query(query):
    query = normalize_query(query)

    words = query.split()

    expanded = []

    for word in words:

        expanded.append(word)

        if word in SYNONYMS:

            expanded.extend(SYNONYMS[word])

    return list(set(expanded))


def get_candidate_products(query, products_df):

    search_terms = expand_query(query)

    detected_category = detect_category(query)

    detected_brand = detect_brand(query)

    candidate_products = []

    for idx, row in products_df.iterrows():

        name = normalize_query(row["name"])

        category = normalize_query(row["sub_category"])

        score = 0

        # ------------------------
        # Keyword Match
        # ------------------------

        for word in search_terms:

            if word in name:
                score += 5

            if word in category:
                score += 3

        # ------------------------
        # Category Boost
        # ------------------------

        if detected_category:

            if detected_category in category:

                score += 20

        # ------------------------
        # Brand Boost
        # ------------------------

        if detected_brand:

            if detected_brand in name:

                score += 15

        if score > 0:

            candidate_products.append((idx, score))

    if len(candidate_products) == 0:

        return products_df.copy()

    candidate_products.sort(

        key=lambda x: x[1],

        reverse=True

    )

    candidate_indices = [

        idx

        for idx, score in candidate_products[:300]

    ]

    return products_df.loc[candidate_indices]
def title_similarity(query, product_name):

    return SequenceMatcher(
        None,
        normalize_query(query),
        normalize_query(product_name)
    ).ratio()


def category_score(query, category):

    query = normalize_query(query)
    category = normalize_query(category)

    query_words = set(query.split())

    category_words = set(category.split())

    common = query_words.intersection(category_words)

    if len(common) == 0:
        return 0.0

    return len(common) / len(query_words)


def popularity_score(rating, no_of_ratings):

    try:
        rating = float(rating)
    except:
        rating = 0

    try:
        count = float(str(no_of_ratings).replace(",", ""))
    except:
        count = 0

    rating_score = rating / 5.0

    count_score = min(count / 10000, 1)

    return rating_score * 0.7 + count_score * 0.3