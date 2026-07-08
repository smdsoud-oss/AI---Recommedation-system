import numpy as np
import clip
import torch
import re
from sklearn.metrics.pairwise import cosine_similarity

SYNONYMS = {

    "earbuds": "earphones",
    "buds": "earphones",
    "tws": "earphones",

    "charger": "adapter",

    "pendrive": "usb drive",
    "pen drive": "usb drive",

    "watch": "smart watch",

    "keyboard": "keyboard",
    "mouse": "mouse",
    "webcam": "webcam"
}


def normalize_query(query):

    query = query.lower().strip()

    query = re.sub(r"[^a-z0-9 ]", "", query)

    return query


def expand_query(query):

    query = normalize_query(query)

    words = query.split()

    expanded = []

    for word in words:

        expanded.append(word)

        if word in SYNONYMS:

            expanded.append(SYNONYMS[word])

    return " ".join(expanded)
class ProductRecommender:

    def __init__(
        self,
        model,
        device,
        combined_embeddings,
        mapping_df,
        products_df
    ):

        self.model = model
        self.device = device
        self.combined_embeddings = combined_embeddings
        self.mapping_df = mapping_df
        self.products_df = products_df

    def recommend(self, query, top_k=10):

        # -----------------------------
        # Normalize and expand query
        # -----------------------------

        query = expand_query(query)

        # -----------------------------
        # Candidate Filtering
        # -----------------------------

        candidate_df = self.products_df[

            self.products_df["name"]
            .str.lower()
            .str.contains(query.split()[0], na=False)

        ]

        if len(candidate_df) == 0:

            candidate_df = self.products_df

        candidate_indices = candidate_df.index.tolist()

        # -----------------------------
        # Candidate Embeddings
        # -----------------------------

        candidate_embeddings = self.combined_embeddings[
            candidate_indices
        ]

        # -----------------------------
        # Encode Query
        # -----------------------------

        text = clip.tokenize(
            [query],
            truncate=True
        ).to(self.device)

        with torch.no_grad():

            query_embedding = self.model.encode_text(text)

        query_embedding = query_embedding.cpu().numpy()

        query_embedding = query_embedding / np.linalg.norm(
            query_embedding,
            axis=1,
            keepdims=True
        )

        # -----------------------------
        # Similarity
        # -----------------------------

        similarity_scores = cosine_similarity(
            query_embedding,
            candidate_embeddings
        )[0]

        # -----------------------------
        # Name Match Boost
        # -----------------------------

        for i, idx in enumerate(candidate_indices):

            product_name = self.products_df.iloc[idx]["name"].lower()

            if normalize_query(query).split()[0] in product_name:

                similarity_scores[i] += 0.15

        # -----------------------------
        # Similarity Threshold
        # -----------------------------

        threshold = 0.55

        ranked = np.argsort(similarity_scores)[::-1]

        top_indices = []

        top_scores = []

        for idx in ranked:

            if similarity_scores[idx] >= threshold:

                top_indices.append(candidate_indices[idx])

                top_scores.append(similarity_scores[idx])

            if len(top_indices) == top_k:

                break

        # -----------------------------
        # Mapping
        # -----------------------------

        mapping = self.mapping_df.set_index(
            "product_index"
        )

        image_names = []

        for idx in top_indices:

            if idx in mapping.index:

                image_names.append(
                    mapping.loc[idx]["image_name"]
                )

            else:

                image_names.append(None)

        recommended_products = self.products_df.iloc[
            top_indices
        ].copy()

        recommended_products["image_name"] = image_names

        recommended_products["similarity_score"] = top_scores

        return recommended_products