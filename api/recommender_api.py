import numpy as np
import pandas as pd

from src.embedding.clip_model import load_clip_model
from src.recommendation.recommender import ProductRecommender


# ----------------------------
# Load Model
# ----------------------------

model, preprocess, device = load_clip_model()


# ----------------------------
# Load Embeddings
# ----------------------------

combined_embeddings = np.load(
    "data/embeddings/combined_embeddings.npy"
)

mapping_df = pd.read_csv(
    "data/embeddings/image_mapping.csv"
)

mapping_df["product_index"] = (
    mapping_df["image_name"]
    .str.replace(".jpg", "", regex=False)
    .astype(int)
)

products_df = pd.read_csv(
    "data/processed/cleaned_electronics_products.csv"
)


# ----------------------------
# Initialize Recommender
# ----------------------------

recommender = ProductRecommender(
    model,
    device,
    combined_embeddings,
    mapping_df,
    products_df
)


# ----------------------------
# Recommendation Function
# ----------------------------

def get_recommendations(query: str):

    results = recommender.recommend(query)

    recommendations = []

    for _, product in results.iterrows():

        recommendations.append({

            "name": product["name"],

            "price": str(product["discount_price"]),

            "rating": str(product["ratings"]),

            "similarity": round(
                product["similarity_score"] * 100,
                2
            ),

            "image_name": product["image_name"],

            "link": product["link"]

        })

    return recommendations