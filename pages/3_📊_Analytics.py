import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dataset Analytics")

# -------------------------
# Load Dataset
# -------------------------

df = pd.read_csv("data/processed/cleaned_electronics_products.csv")

# -------------------------
# Data Cleaning
# -------------------------

df["ratings"] = pd.to_numeric(df["ratings"], errors="coerce")

df["discount_price"] = (
    df["discount_price"]
    .replace(r"[₹,]", "", regex=True)
)

df["discount_price"] = pd.to_numeric(
    df["discount_price"],
    errors="coerce"
)

# -------------------------
# Dataset Overview
# -------------------------

st.header("Dataset Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Products", len(df))

col2.metric("Main Categories", df["main_category"].nunique())

col3.metric("Sub Categories", df["sub_category"].nunique())

st.divider()

# -------------------------
# Main Category Distribution
# -------------------------

st.subheader("Main Category Distribution")

category_counts = df["main_category"].value_counts()

fig, ax = plt.subplots(figsize=(8,5))

category_counts.plot(
    kind="bar",
    ax=ax
)

plt.xticks(rotation=45)

st.pyplot(fig)

# -------------------------
# Ratings Distribution
# -------------------------

st.subheader("Ratings Distribution")

fig, ax = plt.subplots(figsize=(8,5))

df["ratings"].dropna().hist(
    bins=20,
    ax=ax
)

st.pyplot(fig)

# -------------------------
# Price Distribution
# -------------------------

st.subheader("Discount Price Distribution")

fig, ax = plt.subplots(figsize=(8,5))

df["discount_price"].dropna().hist(
    bins=30,
    ax=ax
)

st.pyplot(fig)

# -------------------------
# Top 10 Highest Rated Products
# -------------------------

st.subheader("Top Rated Products")

top_products = df.sort_values(
    by="ratings",
    ascending=False
).head(10)

st.dataframe(
    top_products[
        [
            "name",
            "ratings",
            "discount_price"
        ]
    ],
    use_container_width=True
)