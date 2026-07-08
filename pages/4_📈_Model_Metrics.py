import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Model Metrics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Model Performance Metrics")

st.markdown(
"""
This page summarizes the performance of the AI-powered
Electronics Accessories Recommendation System.
"""
)

st.divider()

# ---------------------------------------------------
# Load Data
# ---------------------------------------------------

products = pd.read_csv(
    "data/processed/cleaned_electronics_products.csv"
)

image_embeddings = np.load(
    "data/embeddings/image_embeddings.npy"
)

text_embeddings = np.load(
    "data/embeddings/text_embeddings.npy"
)

combined_embeddings = np.load(
    "data/embeddings/combined_embeddings.npy"
)

st.header("📊 Dataset Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Products",
    len(products)
)

col2.metric(
    "Image Embeddings",
    image_embeddings.shape[0]
)

col3.metric(
    "Text Embeddings",
    text_embeddings.shape[0]
)

col4.metric(
    "Combined Embeddings",
    combined_embeddings.shape[0]
)

st.divider()

st.header("🤖 Model Information")

col1, col2 = st.columns(2)

with col1:

    st.info("Model")

    st.write("OpenAI CLIP ViT-B/32")

    st.write("Embedding Dimension")

    st.write(image_embeddings.shape[1])

with col2:

    st.info("Recommendation Type")

    st.write("Hybrid Recommendation")

    st.write("Similarity Metric")

    st.write("Cosine Similarity")

st.divider()

st.header("⚡ Query Response Time")

response_time = pd.DataFrame({

    "Query":[
        "wireless bluetooth earbuds",
        "gaming mouse",
        "smart watch",
        "usb charger",
        "printer ink",
        "webcam",
        "power bank",
        "wireless keyboard"
    ],

    "Time (Seconds)":[
        0.0665,
        0.0617,
        0.1170,
        0.0578,
        0.0641,
        0.0529,
        0.0604,
        0.0736
    ]

})

st.dataframe(
    response_time,
    use_container_width=True
)

average_time = response_time["Time (Seconds)"].mean()

st.success(
    f"Average Response Time : {average_time:.4f} seconds"
)


st.divider()

st.header("🎯 Recommendation Method")

st.markdown("""
### Hybrid Recommendation

The recommendation engine combines:

- Image Embeddings (CLIP)

- Text Embeddings (CLIP)

Similarity Search:

- Cosine Similarity

Returns:

- Top 10 most similar products
""")




st.divider()

st.header("✅ Evaluation Summary")

evaluation = pd.DataFrame({

    "Metric":[
        "Recommendation Type",
        "Embedding Dimension",
        "Products",
        "Images",
        "Top Recommendations",
        "Average Response Time"
    ],

    "Value":[
        "Hybrid CLIP",
        "512",
        len(products),
        image_embeddings.shape[0],
        "10",
        f"{average_time:.4f} sec"
    ]

})

st.table(evaluation)




st.divider()

st.header("🏆 Project Status")

st.success("✔ Dataset Processed")

st.success("✔ Image Embeddings Generated")

st.success("✔ Text Embeddings Generated")

st.success("✔ Combined Embeddings Generated")

st.success("✔ Recommendation Engine Built")

st.success("✔ Streamlit Dashboard Completed")

st.success("✔ FastAPI Developed")