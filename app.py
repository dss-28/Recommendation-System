# app.py (updated for demo with side-by-side display)
import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ----------------- Load Saved Model Components -----------------
with open("model/user_map.pkl", "rb") as f:
    user_map = pickle.load(f)

with open("model/item_map.pkl", "rb") as f:
    item_map = pickle.load(f)

with open("model/matrix_reduced.pkl", "rb") as f:
    matrix_reduced = pickle.load(f)

with open("model/svd_components.pkl", "rb") as f:
    svd_components = pickle.load(f)

with open("model/pt.pkl", "rb") as f:
    pt = pickle.load(f)

similarity_scores = np.load("model/similarity_scores.npy")
books = pd.read_csv("data/books.csv")

# ----------------- Define Hybrid Recommender -----------------
def get_cf_scores(user_id):
    user_idx = list(user_map.keys())[list(user_map.values()).index(user_id)]
    cf_scores_array = matrix_reduced[user_idx] @ svd_components
    cf_dict = {item_map[i]: cf_scores_array[i] for i in range(len(item_map))}
    return cf_dict

def get_cbf_scores(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = list(enumerate(similarity_scores[index]))
    cbf_dict = {pt.index[i]: score for i, score in similar_items}
    return cbf_dict

def hybrid_recommend(user_id, book_name=None, alpha=0.6, top_n=10):
    cf_dict = get_cf_scores(user_id)
    cbf_dict = get_cbf_scores(book_name) if book_name else {}
    all_items = set(cf_dict.keys()).union(set(cbf_dict.keys()))
    hybrid_scores = {item: alpha * cf_dict.get(item, 0) + (1 - alpha) * cbf_dict.get(item, 0)
                     for item in all_items}
    recommended = sorted(hybrid_scores.items(), key=lambda x: x[1], reverse=True)[:top_n]
    data = []
    for title, score in recommended:
        temp_df = books[books['Book-Title'] == title].drop_duplicates('Book-Title')
        for _, row in temp_df.iterrows():
            data.append([row['Book-Title'], row['Book-Author'], row['Image-URL-M']])
    return data

# ----------------- Streamlit UI -----------------
st.title("📚 Hybrid Book Recommendation System")
st.markdown("Get personalized book recommendations using Collaborative + Content-based filtering.")

# Dropdown for demo User IDs
user_ids = list(user_map.values())[:50]  # top 50 users for demo
user_id_input = st.selectbox("Select User ID:", user_ids)

# Dropdown for seed books (optional)
book_names = list(pt.index)[:100]  # first 100 books for demo
book_name_input = st.selectbox("Select Seed Book (optional):", [""] + book_names)

if st.button("Get Recommendations"):
    try:
        book_name = book_name_input if book_name_input != "" else None
        recommendations = hybrid_recommend(user_id_input, book_name)
        st.success(f"Top {len(recommendations)} Recommendations:")

        # Display books side by side
        books_per_row = 3  # adjust for columns per row
        for i in range(0, len(recommendations), books_per_row):
            cols = st.columns(books_per_row)
            for j, (title, author, img_url) in enumerate(recommendations[i:i+books_per_row]):
                with cols[j]:
                    st.markdown(f"**{title}** by {author}")
                    if img_url and str(img_url) != "nan":
                        st.image(img_url, width=120)

    except Exception as e:
        st.warning(f"Error: {e}. Please select valid User ID and Seed Book.")
