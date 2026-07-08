import streamlit as st
import pandas as pd
import numpy as np
import os
from PIL import Image

from src.embedding.clip_model import load_clip_model
from src.recommendation.recommender import ProductRecommender


# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    st.title("🏠 Home"),
    page_title="AI Electronics Recommendation System",
    page_icon="🛍️",
    layout="wide"
)


# =====================================================
# Custom CSS
# =====================================================

st.markdown("""
<style>

.product-card{
    border:1px solid #d9d9d9;
    border-radius:12px;
    padding:12px;
    margin-bottom:20px;
    background-color:white;
    box-shadow:0px 2px 8px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# Cache Resources
# =====================================================

@st.cache_resource
def load_model():
    return load_clip_model()


@st.cache_data
def load_data():

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

    products_df = products_df.iloc[
        mapping_df["product_index"]
    ].reset_index(drop=True)

    return combined_embeddings, mapping_df, products_df


# =====================================================
# Load Model
# =====================================================

model, preprocess, device = load_model()

combined_embeddings, mapping_df, products_df = load_data()

recommender = ProductRecommender(
    model,
    device,
    combined_embeddings,
    mapping_df,
    products_df
)


# =====================================================
# Sidebar
# =====================================================

st.sidebar.title("📌 About")

st.sidebar.write("""
### AI Electronics Accessories Recommendation System

Built Using:

- OpenAI CLIP
- PyTorch
- Streamlit
- Cosine Similarity

""")

st.sidebar.metric(
    "Products",
    len(products_df)
)

st.sidebar.metric(
    "Embedding Size",
    combined_embeddings.shape[1]
)

st.sidebar.success(f"Running on: {device.upper()}")


# =====================================================
# Main Title
# =====================================================

st.title("🛍️ AI Electronics Accessories Recommendation System")

st.write(
    "Search for an electronics product and receive visually similar recommendations using CLIP embeddings."
)


# =====================================================
# Sample Queries
# =====================================================

st.subheader("🔍 Search Products")

sample_queries = [
    "Select an example...",
    "wireless bluetooth earbuds",
    "gaming mouse",
    "smart watch",
    "bluetooth speaker",
    "webcam",
    "usb charger",
    "type c cable",
    "power bank",
    "wireless keyboard",
    "printer ink",
    "hdmi cable",
    "laptop stand"
]

selected_query = st.selectbox(
    "🎯 Try a Sample Search",
    sample_queries
)

query = st.text_input(
    "Or type your own product",
    value="" if selected_query == "Select an example..." else selected_query,
    placeholder="Example: bluetooth earbuds"
)


# =====================================================
# Recommendation Button
# =====================================================

if st.button("🚀 Recommend Products"):

    if query.strip() == "":
        st.warning("Please enter a search query.")

    else:

        with st.spinner("Generating Recommendations..."):

            results = recommender.recommend(query)

        st.success(f"Showing recommendations for **{query}**")

        cols = st.columns(5)

        for i in range(min(10, len(results))):
            product = results.iloc[i]
            image_path = os.path.join("data/images", product["image_name"])

            with cols[i % 5]:
                st.markdown(
                    '<div class="product-card">',
                    unsafe_allow_html=True
                )

                if os.path.exists(image_path):
                    img = Image.open(image_path).convert("RGB")
                    BOX_SIZE = (220, 220)
                    img.thumbnail(BOX_SIZE)
                    background = Image.new("RGB", BOX_SIZE, (255, 255, 255))
                    x = (BOX_SIZE[0] - img.width) // 2
                    y = (BOX_SIZE[1] - img.height) // 2
                    background.paste(img, (x, y))
                    st.image(background, width=220)
                else:
                    st.write("Image Not Found")

                title = str(product["name"])
                if len(title) > 55:
                    title = title[:55] + "..."

                st.markdown(
                    f"""
                    <div style="
                        height:65px;
                        overflow:hidden;
                        font-weight:bold;
                        font-size:15px;
                    ">
                        {title}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                price = product["discount_price"]
                if pd.isna(price):
                    price = "Not Available"

                st.markdown(
                    f"**💰 Price:** {price}"
                )

                rating = product["ratings"]
                if pd.isna(rating):
                    rating = "N/A"

                st.markdown(
                    f"**⭐ Rating:** {rating}"
                )

                similarity = float(product["similarity_score"])
                st.progress(similarity)
                st.markdown(
                    f"**🎯 Match:** {similarity*100:.1f}%"
                )

                if "link" in product.index:
                    st.link_button(
                        "🛒 View Product",
                        product["link"],
                        use_container_width=True
                    )

                st.markdown("</div>", unsafe_allow_html=True)

            if (i + 1) % 5 == 0 and i != 9:
                cols = st.columns(5)

# =====================================================
# Footer
# =====================================================

st.markdown("---")

st.markdown(
    """
    <center>

    Developed by <b>Mohammed Soud</b>

    <br><br>

    AI Electronics Accessories Recommendation System

    <br>

    Powered by OpenAI CLIP • PyTorch • Streamlit

    </center>
    """,
    unsafe_allow_html=True
)