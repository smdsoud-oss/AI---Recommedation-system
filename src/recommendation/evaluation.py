import numpy as np


class Evaluation:

    """
    Evaluation Metrics for Recommendation System
    """

    @staticmethod
    def precision_at_k(relevant_items, recommended_items, k=10):

        recommended_items = recommended_items[:k]

        hits = len(
            set(recommended_items)
            &
            set(relevant_items)
        )

        return hits / k

    @staticmethod
    def recall_at_k(relevant_items, recommended_items, k=10):

        recommended_items = recommended_items[:k]

        hits = len(
            set(recommended_items)
            &
            set(relevant_items)
        )

        if len(relevant_items) == 0:
            return 0

        return hits / len(relevant_items)

    @staticmethod
    def average_precision(relevant_items, recommended_items):

        score = 0
        hits = 0

        for i, item in enumerate(recommended_items):

            if item in relevant_items:

                hits += 1

                score += hits / (i + 1)

        if hits == 0:

            return 0

        return score / hits

    @staticmethod
    def mean_average_precision(all_relevant, all_recommended):

        scores = []

        for rel, rec in zip(
            all_relevant,
            all_recommended
        ):

            scores.append(

                Evaluation.average_precision(
                    rel,
                    rec
                )

            )

        return np.mean(scores)

    @staticmethod
    def ndcg_at_k(relevant_items, recommended_items, k=10):

        dcg = 0

        for i, item in enumerate(recommended_items[:k]):

            if item in relevant_items:

                dcg += 1 / np.log2(i + 2)

        idcg = 0

        ideal_hits = min(k, len(relevant_items))

        for i in range(ideal_hits):

            idcg += 1 / np.log2(i + 2)

        if idcg == 0:

            return 0

        return dcg / idcg