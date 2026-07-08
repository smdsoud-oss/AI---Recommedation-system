"""
Collaborative Recommendation Model

This file is included to match the
recommended project architecture.

Current project uses a Content-Based
Recommendation System with OpenAI CLIP.

Collaborative Filtering requires:

- user_id
- product_id
- interaction history
- ratings/clicks/purchases

Since the current dataset does not contain
user interaction history, collaborative
filtering has not been implemented.

Future work:

- Matrix Factorization
- User-User CF
- Item-Item CF
- LightFM
- Surprise Library
"""


class CollaborativeModel:

    def __init__(self):

        pass

    def recommend(self):

        raise NotImplementedError(

            "Collaborative Filtering requires user interaction data."

        )