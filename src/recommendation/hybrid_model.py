import numpy as np


class HybridModel:

    def __init__(
        self,
        clip_weight=0.60,
        title_weight=0.20,
        category_weight=0.10,
        popularity_weight=0.10
    ):

        self.clip_weight = clip_weight
        self.title_weight = title_weight
        self.category_weight = category_weight
        self.popularity_weight = popularity_weight

    def rank(
        self,
        clip_scores,
        title_scores,
        category_scores,
        popularity_scores
    ):

        clip_scores = np.array(clip_scores)

        title_scores = np.array(title_scores)

        category_scores = np.array(category_scores)

        popularity_scores = np.array(popularity_scores)

        final_scores = (

            self.clip_weight * clip_scores

            +

            self.title_weight * title_scores

            +

            self.category_weight * category_scores

            +

            self.popularity_weight * popularity_scores

        )

        return final_scores