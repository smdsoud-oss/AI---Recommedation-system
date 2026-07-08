from .popularity_model import PopularityModel


class ColdStartModel:

    """
    Cold Start Recommendation

    Handles situations where:
    1. New user
    2. No matching products
    3. Empty search query

    Strategy:
    Recommend most popular products.
    """

    def __init__(self, products_df):

        self.products_df = products_df
        self.popularity_model = PopularityModel(products_df)

    def recommend(self, query=None, top_k=10):

        # Empty search
        if query is None:

            return self.popularity_model.recommend(top_k)

        if str(query).strip() == "":

            return self.popularity_model.recommend(top_k)

        # Unknown query
        if len(str(query).split()) == 0:

            return self.popularity_model.recommend(top_k)

        # Default fallback
        return self.popularity_model.recommend(top_k)