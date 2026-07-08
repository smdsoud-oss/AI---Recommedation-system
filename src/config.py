import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

IMAGE_FOLDER = os.path.join(DATA_DIR, "images")

EMBEDDING_FOLDER = os.path.join(DATA_DIR, "embeddings")

PROCESSED_DATA = os.path.join(
    DATA_DIR,
    "processed",
    "cleaned_electronics_products.csv"
)