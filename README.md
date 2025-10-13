
# 📚 Hybrid Book Recommender System

> A smart book recommendation engine combining **Collaborative Filtering**, **Content-Based Filtering**, and insights from an **initial popularity-based experiment**.

---

## 🔹 **Overview**

This project implements a **hybrid recommendation system** that personalizes book recommendations while addressing cold-start challenges:

1. **Collaborative Filtering (CF)** – learns user preferences from rating patterns using **SVD**.
2. **Content-Based Filtering (CBF)** – recommends books with similar metadata using **TF-IDF** and **cosine similarity**.
3. **Popularity-Based Baseline** – an initial experiment that recommended the same popular books for all users (motivated hybrid design).

> ✅ Goal: Recommend books that are **both personalized and content-aware**.

---

## 🔹 **Features**

* Hybrid recommender combining **CF + CBF**
* **TF-IDF vectorization** for book metadata
* **SVD applied only to CF** for latent factor extraction
* **Cosine similarity / NearestNeighbors** for CBF recommendations
* Popularity-based experiment as **baseline / motivation**
* Evaluates CF with **RMSE**, ready to extend with ranking metrics
* Cold-start support for new users/items

---

## 🔹 **Dataset**

| File          | Description                                                  |
| ------------- | ------------------------------------------------------------ |
| `Books.csv`   | Book metadata (title, author, description, genre)            |
| `Ratings.csv` | User–book ratings matrix (userId, bookId, rating, timestamp) |
| `Users.csv`   | Optional user demographic info                               |

---

## 🔹 **Step-by-Step Workflow**

### **1️⃣ Popularity-Based Baseline (Initial Experiment)**

* Recommended books based solely on **popularity** (number of ratings or average rating)
* Limitation: **same top books for all users**
* Motivated the hybrid system:

```python
popular_books = ratings.groupby('bookId')['rating'].count().sort_values(ascending=False)
top_books = popular_books.head(10)
```

---

### **2️⃣ Data Loading & Preprocessing**

* Clean missing titles/ratings
* Ensure **IDs align** across books, users, and ratings
* Prepare **user-item matrix** for CF and **TF-IDF matrix** for CBF

---

### **3️⃣ Content-Based Filtering (CBF)**

* TF-IDF transforms book metadata into vectors
* Compute **cosine similarity / NearestNeighbors** to find similar books
* Example: liking *"Harry Potter"* → recommend *"Percy Jackson"*, *"The Hobbit"*, etc.

> **Note:** No SVD is used here; similarity is computed directly on TF-IDF vectors.

---

### **4️⃣ Collaborative Filtering (CF)**

* User × Book rating matrix (sparse)
* Apply **SVD** to learn **latent factors** for users and books
* Predict ratings for unseen books:

[
\hat{r}_{u,i} = U_u \cdot V_i^T
]

* Evaluate using **RMSE / MSE**

---

### **5️⃣ Hybrid Recommendation**

* Combine **CF and CBF** scores:

[
\text{Final Score} = \alpha \cdot \text{CF Score} + (1 - \alpha) \cdot \text{CBF Score}
]

* CF dominates for users with ratings
* CBF dominates for **new items / cold-start scenarios**

---

### **6️⃣ Recommendation Function**

* `recommend(user_id)` or `recommend(book_title)`
* Returns **top-N books** by blending CF + CBF

```python
recommend_for_user(user_id=123)
recommend(book_title="The Hobbit")
```

---

## 🔹 **Evaluation**

* CF model evaluated with **RMSE**
* Optional: ranking metrics (**Precision@K, Recall@K, NDCG**) for top-N recommendations

---

## 🔹 **Dimensionality Reduction Concept**

* **SVD** is applied **only to CF**
* **CBF** uses cosine similarity on raw TF-IDF vectors
* **t-SNE** (if used) is only for visualization

---

## 🔹 **Pipeline Diagram**

```
Books.csv / Ratings.csv / Users.csv
           |
           v
   Data Cleaning & Preprocessing
           |
           +-----------------+
           |                 |
           v                 v
   TF-IDF Vectorization   User-Item Matrix (CF)
           |                 |
           v                 v
   Cosine Similarity       SVD (latent factors)
           |                 |
           +--------+--------+
                    |
             Hybrid Recommendation
                    |
                    v
          Top-N Recommended Books
```

---

## 🔹 **Improvements & TODO**

* Add **new-user onboarding** (seed ratings)
* Implement **ranking metrics**
* Save trained models (**joblib**: TF-IDF, SVD, NearestNeighbors)
* Use **FAISS** for large-scale similarity search
* Normalize **popularity bias** for better personalization

---

## 🔹 **License**

MIT License

---
