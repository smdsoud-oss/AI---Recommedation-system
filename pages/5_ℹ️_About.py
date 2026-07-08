import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About the Project")

st.markdown("---")

# -----------------------------------------------------
# Project Overview
# -----------------------------------------------------

st.header("📖 Project Overview")

st.write("""
The **AI Electronics Accessories Recommendation System** is an AI-powered
content-based recommendation engine that suggests relevant electronics
products using OpenAI's CLIP model.

The system converts both product images and user search queries into
512-dimensional embeddings and recommends the most semantically similar
products using Cosine Similarity.
""")

st.markdown("---")

# -----------------------------------------------------
# Problem Statement
# -----------------------------------------------------

st.header("🎯 Problem Statement")

st.write("""
Finding the right electronic accessory among thousands of products can be
time-consuming. Traditional keyword search often fails to understand the
actual intent of the user.

This project solves this problem by using Artificial Intelligence to
recommend visually and semantically similar products.
""")

st.markdown("---")

# -----------------------------------------------------
# Objectives
# -----------------------------------------------------

st.header("🎯 Project Objectives")

st.markdown("""
- Build an AI-powered recommendation system.
- Recommend the Top-10 relevant products.
- Reduce product search time.
- Improve user shopping experience.
- Deploy using Streamlit and FastAPI.
""")

st.markdown("---")

# -----------------------------------------------------
# Recommendation Workflow
# -----------------------------------------------------

st.header("⚙️ Recommendation Workflow")

st.markdown("""
1. User enters a product query.

2. CLIP converts the query into a text embedding.

3. Product image embeddings are loaded.

4. Cosine Similarity compares embeddings.

5. Top-10 most similar products are retrieved.

6. Products are displayed with images, price, ratings and similarity score.
""")

st.markdown("---")

# -----------------------------------------------------
# Technology Stack
# -----------------------------------------------------

st.header("🧠 Technology Stack")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Programming")

    st.markdown("""
- Python
- NumPy
- Pandas
- Matplotlib
""")

    st.subheader("Machine Learning")

    st.markdown("""
- PyTorch
- OpenAI CLIP
- Scikit-Learn
""")

with col2:

    st.subheader("Deployment")

    st.markdown("""
- Streamlit
- FastAPI
- Uvicorn
""")

    st.subheader("Development")

    st.markdown("""
- VS Code
- Git
- GitHub
""")

st.markdown("---")

# -----------------------------------------------------
# Project Statistics
# -----------------------------------------------------

st.header("📊 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Products", "9,600")

col2.metric("Images", "9,600")

col3.metric("Embedding Size", "512")

col4.metric("Recommendations", "Top 10")

st.markdown("---")

# -----------------------------------------------------
# Folder Structure
# -----------------------------------------------------

st.header("📂 Project Structure")

st.code("""
AI-Electronics-Accessories-Recommendation-System/

├── api/
├── dashboard/
├── data/
├── notebooks/
├── pages/
├── src/
├── tests/
├── app.py
├── requirements.txt
├── README.md
""")

st.markdown("---")

# -----------------------------------------------------
# Future Improvements
# -----------------------------------------------------

st.header("🚀 Future Scope")

st.markdown("""
- User Login & Authentication
- Personalized Recommendations
- User Purchase History
- Collaborative Filtering
- Hybrid Recommendation System
- Real-time Product Database
- Cloud Deployment (AWS/Azure/GCP)
- Mobile Application
""")

st.markdown("---")

# -----------------------------------------------------
# Project Status
# -----------------------------------------------------

st.header("✅ Current Status")

st.success("✔ Data Collection Completed")

st.success("✔ Data Cleaning Completed")

st.success("✔ Image Download Completed")

st.success("✔ Image Embeddings Generated")

st.success("✔ Text Embeddings Generated")

st.success("✔ Combined Embeddings Generated")

st.success("✔ Recommendation Engine Developed")

st.success("✔ FastAPI Developed")

st.success("✔ Streamlit Dashboard Developed")

st.success("✔ Project Successfully Completed")

st.markdown("---")

# -----------------------------------------------------
# Developer
# -----------------------------------------------------

st.header("👨‍💻 Developer")

st.info("""
**Developed by:**

Mohammed Soud

B.Tech – Artificial Intelligence & Data Science

AI Electronics Accessories Recommendation System
""")

st.markdown("---")

st.caption("© 2026 AI Electronics Accessories Recommendation System")