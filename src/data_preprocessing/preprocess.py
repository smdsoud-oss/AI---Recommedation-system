import pandas as pd


def load_products(csv_path):
    """
    Load processed products dataset.
    """

    return pd.read_csv(csv_path)