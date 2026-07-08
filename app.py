import streamlit as st

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="AI Electronics Recommendation System",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------
# Title
# ---------------------------------------

st.title("🛍️ AI Electronics Accessories Recommendation System")

st.markdown("---")

st.header("📖 Project Overview")

st.write("""
This project is an AI-powered Electronics Accessories Recommendation System
that recommends visually and semantically similar products using OpenAI's
CLIP model.

The system combines image embeddings and text embeddings to provide
high-quality product recommendations through a modern Streamlit dashboard
and FastAPI backend.
""")

st.markdown("---")

st.header("🎯 Objectives")

st.markdown("""
- Recommend relevant electronics products
- Understand user search intent
- Improve shopping experience
- Reduce product search time
- Demonstrate AI-powered recommendation systems
""")

st.markdown("---")

st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:
    st.success("✅ Text-based Product Search")
    st.success("✅ CLIP Image Embeddings")
    st.success("✅ CLIP Text Embeddings")
    st.success("✅ Hybrid Recommendation")

with col2:
    st.success("✅ FastAPI Backend")
    st.success("✅ Streamlit Dashboard")
    st.success("✅ Top 10 Recommendations")
    st.success("✅ Similarity Score")

st.markdown("---")

st.header("📊 Dataset Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Products", "9,600")
col2.metric("Images", "9,600")
col3.metric("Embedding Size", "512")
col4.metric("Response Time", "~0.06 sec")

st.markdown("---")

st.header("🧠 Technology Stack")

st.markdown("""
- Python
- OpenAI CLIP
- PyTorch
- NumPy
- Pandas
- Scikit-Learn
- Streamlit
- FastAPI
""")

st.markdown("---")

st.info("👈 Use the sidebar to navigate through the dashboard pages.")