# 🛍️ AI Electronics Accessories Recommendation System

An AI-powered recommendation system that recommends visually and semantically similar electronics accessories using **OpenAI CLIP**, **PyTorch**, **Scikit-Learn**, **FastAPI**, and **Streamlit**.

---

## 📌 Project Overview

This project is an AI-powered Electronics Accessories Recommendation System that helps users discover relevant products through natural language search. Instead of relying only on keyword matching, the system uses OpenAI's CLIP model to understand both product images and user text queries. A hybrid recommendation algorithm combines semantic similarity, title similarity, category matching, and popularity score to generate accurate Top-10 product recommendations.

---

## 🎯 Problem Statement

Traditional e-commerce search systems rely heavily on keyword matching, which often fails to understand the user's actual intent. As online marketplaces grow, users spend more time searching for suitable products. This project addresses that challenge by using Artificial Intelligence and Computer Vision to recommend visually and semantically similar electronics accessories, improving both recommendation quality and user experience.

---

## 🎯 Objectives

- Develop an AI-powered recommendation system.
- Recommend visually and semantically similar products.
- Improve recommendation accuracy using a hybrid scoring algorithm.
- Handle cold-start scenarios gracefully.
- Provide an interactive Streamlit dashboard.
- Expose recommendation services using FastAPI.

---

## ✨ Features

- 🔍 Natural Language Product Search
- 🧠 OpenAI CLIP Image & Text Embeddings
- 🤖 Hybrid Recommendation Engine
- 📊 Cosine Similarity Matching
- ⭐ Popularity-Based Ranking
- ❄️ Cold Start Handling
- 🌐 FastAPI REST API
- 💻 Interactive Streamlit Dashboard
- 📈 Model Evaluation Metrics
- 🎯 Top 10 Personalized Recommendations

---

## 🏗️ System Architecture

```text
User Query
     │
     ▼
Search Candidate Products
     │
     ▼
CLIP Text Encoder
     │
     ▼
Generate Query Embedding
     │
     ▼
Cosine Similarity
     │
     ▼
Hybrid Scoring
(CLIP + Title + Category + Popularity)
     │
     ▼
Top 10 Recommendations
     │
     ▼
Streamlit Dashboard
```

---

## ⚙️ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Deep Learning | PyTorch |
| AI Model | OpenAI CLIP (ViT-B/32) |
| Machine Learning | Scikit-Learn |
| Numerical Computing | NumPy |
| Data Analysis | Pandas |
| API Framework | FastAPI |
| Frontend | Streamlit |
| Visualization | Matplotlib, Seaborn |
| Development | Jupyter Notebook |

---

## 📂 Dataset

- Source: Kaggle
- Domain: Electronics Accessories
- Products: ~9,600
- Images: ~9,600
- Data includes:
  - Product Name
  - Category
  - Price
  - Rating
  - Number of Ratings
  - Product Image

---

## 🧹 Data Preprocessing

The dataset was cleaned before training the recommendation model.

### Steps Performed

- Removed duplicate products
- Handled missing values
- Cleaned product names
- Standardized categories
- Verified image availability
- Processed ratings and review counts

---

## 🧠 Embedding Generation

Product images were converted into **512-dimensional embeddings** using OpenAI CLIP.

### Workflow

- Load CLIP (ViT-B/32)
- Preprocess images
- Generate image embeddings
- Generate text embeddings
- Combine embeddings
- Store embeddings as NumPy arrays

Each product is represented as a **512-dimensional feature vector**, enabling efficient similarity comparison.

---

## 🔍 Recommendation Pipeline

1. User enters a product query.
2. Candidate products are filtered.
3. Query is converted into a CLIP text embedding.
4. Cosine similarity is computed between the query and product embeddings.
5. A hybrid score is calculated.
6. Products are ranked.
7. Top 10 recommendations are displayed.

---

## 🏆 Hybrid Recommendation Formula

Final Score =

```
0.60 × CLIP Similarity
+ 0.20 × Title Similarity
+ 0.10 × Category Match
+ 0.10 × Popularity Score
```

---

## ⭐ Popularity Model

Popularity is calculated using:

- Product Rating
- Number of Customer Reviews

Products with higher ratings and more customer reviews receive higher popularity scores.

---

## ❄️ Cold Start Strategy

If the searched product is unavailable in the dataset:

- Display "Product Not Found"
- Recommend highly rated and popular products
- Prevent application crashes
- Ensure a smooth user experience

---

## 📊 Evaluation Metrics

The recommendation model is evaluated using:

- Precision@K
- Recall@K
- MAP@K (Mean Average Precision)
- NDCG@K (Normalized Discounted Cumulative Gain)

---

## 📁 Project Structure

```
AI-Electronics-Accessories-Recommendation-System
│
├── api/
├── dashboard/
├── data/
├── embeddings/
├── images/
├── notebooks/
├── pages/
├── src/
│   ├── embedding/
│   ├── recommendation/
│   └── utils/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone <repository-url>
cd AI-Electronics-Accessories-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## ▶️ Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📷 Dashboard Screenshots

### Home Page

(Add Screenshot)

### Recommendation Page

(Add Screenshot)

### Analytics Dashboard

(Add Screenshot)

### API Documentation

(Add Screenshot)

---

## 📈 Future Enhancements

- Integrate FAISS for faster similarity search
- Connect to real-time e-commerce APIs
- Support dynamic embedding generation
- Personalized user recommendations
- Brand-aware recommendation engine
- Voice-based product search
- Multi-language search support
- Cloud deployment using Docker and AWS

---

## 👨‍💻 Author

**Mohammed Soud**

B.Tech – Artificial Intelligence & Data Science

---

## 📜 License

This project is developed for academic and educational purposes.