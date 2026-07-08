import pandas as pd


class PopularityModel:

    def __init__(self, products_df):

        self.products_df = products_df.copy()

    def recommend(self, top_k=10):

        df = self.products_df.copy()

        # Calculate popularity score
        df["popularity_score"] = (

            df["ratings"] *

            df["no_of_ratings"]

        )

        recommendations = (

            df.sort_values(

                by="popularity_score",

                ascending=False

            )

            .head(top_k)

        )

        return recommendations