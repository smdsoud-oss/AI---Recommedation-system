import streamlit as st


st.set_page_config(
    page_title="AI Electronics Accessories Recommendation System",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Electronics Accessories Recommendation System")

st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
### 📌 Project Overview

This project recommends electronics accessories using **OpenAI CLIP** embeddings and
a **hybrid recommendation engine**.

Unlike traditional keyword search, our system understands the **visual and semantic meaning**
of products, allowing users to discover similar accessories even when the exact product
name is unknown.

---

### 🚀 Key Features

✅ AI-powered product recommendation

✅ CLIP image embeddings (512-dimensional vectors)

✅ Hybrid recommendation engine

✅ Semantic search

✅ Category-aware ranking

✅ Popularity-based scoring

✅ Interactive Streamlit dashboard

✅ Recommendation Analytics

✅ Model Evaluation Metrics

---

### 🛠️ Technologies Used

- Python
- Streamlit
- PyTorch
- OpenAI CLIP
- NumPy
- Pandas
- Scikit-Learn
- Pillow

""")

with col2:

    st.metric("📦 Products", "9,600")

    st.metric("🧠 Embedding Size", "512")

    st.metric("⚡ Recommendation Model", "Hybrid")

    st.metric("🖼️ Vision Model", "OpenAI CLIP")

st.markdown("---")

st.subheader("📈 Recommendation Pipeline")

st.markdown("""

1️⃣ Product Dataset

⬇

2️⃣ Image Download

⬇

3️⃣ Image Preprocessing

⬇

4️⃣ OpenAI CLIP generates **512-dimensional embeddings**

⬇

5️⃣ Embeddings stored as NumPy arrays

⬇

6️⃣ User enters a search query

⬇

7️⃣ Query converted into CLIP embedding

⬇

8️⃣ Hybrid Recommendation Engine

- Semantic Similarity
- Title Similarity
- Category Matching
- Popularity Score

⬇

9️⃣ Top 10 Recommended Products

""")

st.markdown("---")

st.success("👈 Use the sidebar to explore Recommendations, Analytics, Model Metrics, and About.")