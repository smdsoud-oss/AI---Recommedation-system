import clip
import torch
import numpy as np

from .search_utils import (
    get_candidate_products,
    title_similarity,
    category_score,
    popularity_score
)

from .content_model import ContentModel


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
        self.embeddings = combined_embeddings
        self.mapping_df = mapping_df
        self.products_df = products_df

        self.content_model = ContentModel(
            combined_embeddings
        )

    def recommend(
        self,
        query,
        top_k=10
    ):

        candidate_df = get_candidate_products(
            query,
            self.products_df
        )

        candidate_indices = [
             idx
             for idx in candidate_df.index.tolist()
             if idx < len(self.embeddings)
        ]

        if len(candidate_indices) == 0:
            return self.products_df.iloc[0:0].copy()

        candidate_embeddings = self.embeddings[
            candidate_indices
        ]
        


        tokens = clip.tokenize(
            [query],
            truncate=True
        ).to(self.device)

        with torch.no_grad():

            query_embedding = self.model.encode_text(tokens)

        query_embedding = query_embedding.cpu().numpy()

        query_embedding = query_embedding / np.linalg.norm(
            query_embedding,
            axis=1,
            keepdims=True
        )

        clip_scores = self.content_model.similarity(
            query_embedding,
            candidate_embeddings
        )

        final_scores = []

        query_lower = query.lower()

        for i, idx in enumerate(candidate_indices):

            row = self.products_df.iloc[idx]

            clip_score = float(clip_scores[i])

            title_score = title_similarity(
                query,
                row["name"]
            )

            category_match = category_score(
                query,
                row["sub_category"]
            )

            popularity = popularity_score(
                row["ratings"],
                row["no_of_ratings"]
            )

            product_name = str(row["name"]).lower()

            score = (
                 clip_score * 0.65
                 + title_score * 0.20
                 + category_match * 0.10
                 + popularity * 0.05
            )

            # Exact query boost
            if query_lower in product_name:
                 score += 0.50

            # First word boost
            first_word = query_lower.split()[0]

            if first_word in product_name:
                 score += 0.25

            # Multiple keyword boost
            matched_words = 0

            for word in query_lower.split():
                 if word in product_name:
                      matched_words += 1

            score += matched_words * 0.10

            final_scores.append(score)

        ranked = np.argsort(final_scores)[::-1]

        top_indices = []
        top_scores = []

        for idx in ranked[:top_k]:

            top_indices.append(candidate_indices[idx])
            top_scores.append(final_scores[idx])

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