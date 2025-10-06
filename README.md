
# 📚 Book Recommendation System

A Python-based recommendation system for books, combining **Popularity-Based**, **Collaborative Filtering**, and planned **Content-Based Filtering** approaches. Designed to provide personalized and relevant book suggestions.

---

## 🚀 Project Overview

This project implements a book recommendation engine using multiple approaches:

1. **Popularity-Based Recommender**
   - Recommend books based on number of ratings and average rating.
   - Useful for highlighting trending books or “safe” recommendations.

2. **Collaborative Filtering (Item–Item, Cosine Similarity)**
   - Recommends books based on user rating patterns.
   - Finds books similar to a given book using **cosine similarity**.

3. **Planned Features**
   - **Content-Based Filtering (CBF)**: Using TF-IDF / embeddings on book metadata (title, author, publisher).
   - **Hybrid Recommender**: Blending popularity, CF, and CBF for personalized recommendations.
   - **Evaluation Metrics**: Precision@K, Recall@K, NDCG@K.
   - **Interactive Demo**: Streamlit / Gradio interface for exploring recommendations with book covers.

---

## 📦 Dataset

Three datasets are used:

1. **Books**
   - Columns: `Book-Title`, `Book-Author`, `Image-URL-M`, etc.
2. **Users**
   - Columns: `User-ID`, `Location`, `Age`
3. **Ratings**
   - Columns: `User-ID`, `ISBN`, `Book-Rating`

The datasets are merged to form a single `ratings_with_name` table for easier lookups.

---

## 🔹 Current Implementation

### 1. Popularity-Based Recommender
- Computes number of ratings per book.
- Computes average rating per book.
- Recommends books by popularity or rating.

**Output includes:**
- `Book-Title`, `Book-Author`, `Image-URL-M`
- `num_ratings`, `avg_ratings`

### 2. Collaborative Filtering (Item–Item)
- Creates a user–item matrix (users × books).
- Fills missing ratings with zeros.
- Computes cosine similarity between books.
- Function to recommend top N similar books for a given book title.

---

## ⚡ Next Steps

- Implement **Content-Based Filtering** using TF-IDF or BERT embeddings.
- Combine Popularity + CF + CBF into a **Hybrid Recommender**.
- Add evaluation metrics and an interactive front-end using Streamlit or Gradio.

---

## 💻 How to Run

1. Clone the repository:
```bash
git clone <your-repo-link>
