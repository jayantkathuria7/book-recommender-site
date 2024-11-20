import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import requests
from io import BytesIO

# Set the page layout to wide
st.set_page_config(layout="wide")

# Load your data
popular_df = pd.read_pickle('.pkl files/popular.pkl')
pt = pd.read_pickle('.pkl files/pt.pkl')
books = pd.read_pickle('.pkl files/books.pkl')
similarity_score = pd.read_pickle('.pkl files/similarity_score.pkl')

# Function to fetch image from URL
def fetch_image_from_url(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            return img
        else:
            return None
    except Exception:
        return None

# CSS for enhanced styling and tighter margins
def apply_custom_css():
    st.markdown(
        """
        <style>
        .block-container {
            padding: 5rem;
        }
        .stSidebar {
            background-image: linear-gradient(to bottom, #6a11cb, #2575fc);
            color: white;
        }
        .stButton button {
            background-color: #2575fc;
            color: white;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Define functions for each page
def display_popular_books():
    st.title('🌟 Top 50 Books 🌟')

    # Search functionality
    search_term = st.text_input("🔍 Search in Top 50 Books", "")
    top_50_books = popular_df.head(50)

    if search_term:
        top_50_books = top_50_books[top_50_books['Book-Title'].str.contains(search_term, case=False, na=False)]

    if top_50_books.empty:
        st.warning("No books found for your search!")
        return

    # Grid display: 5 books per row
    num_columns = 5
    num_items = len(top_50_books)
    num_rows = (num_items // num_columns) + (1 if num_items % num_columns > 0 else 0)

    for i in range(num_rows):
        cols = st.columns(num_columns)
        for j, col in enumerate(cols):
            idx = i * num_columns + j
            if idx < num_items:
                book = top_50_books.iloc[idx]
                with col:
                    st.markdown(f"### 📖 {book['Book-Title']}")
                    st.text(f"Author: {book['Book-Author']}")
                    img = fetch_image_from_url(book['Image-URL-M'])
                    if img:
                        st.image(img, caption=f"⭐ {np.round(book['avg_ratings'], 2)} | 📊 {book['num_ratings']} ratings", use_column_width=True)
                    else:
                        st.write("Image not available")
                    st.markdown("---")

def recommend_books():
    st.title('📚 Recommend Books')
    st.markdown('🔍 Start typing a book title:')

    user_input = st.text_input('Search for a book:', '')
    filtered_books = []

    if user_input:
        filtered_books = [title for title in pt.index if user_input.lower() in title.lower()]

    selected_book = st.selectbox(
        "Matching books:",
        options=filtered_books if filtered_books else ["No matches found"],
        label_visibility="collapsed"
    )

    if selected_book != "No matches found" and st.button('💡 Recommend'):
        with st.spinner("Finding recommendations..."):
            try:
                index = np.where(pt.index == selected_book)[0][0]
                similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

                st.subheader("🔗 Recommended Books:")
                # Display all recommendations in a single row
                cols = st.columns(5)  # Show 5 books in a single row
                for i, item in enumerate(similar_items):
                    item_index = item[0]
                    temp_df = books[books['Book-Title'] == pt.index[item_index]].drop_duplicates('Book-Title')
                    with cols[i]:
                        st.markdown(f"**📘 {temp_df['Book-Title'].values[0]}** by {temp_df['Book-Author'].values[0]}")
                        img = fetch_image_from_url(temp_df['Image-URL-M'].values[0])
                        if img:
                            st.image(img, use_column_width=True)
                        else:
                            st.write("Image not available")
                st.markdown("---")
            except IndexError:
                st.error("Book not found. Please try another title.")

# Main function to manage navigation
def main():
    apply_custom_css()

    pages = {
        "Popular Books": display_popular_books,
        "Recommend Books": recommend_books,
    }

    st.sidebar.title('📖 Book Recommender')
    st.sidebar.markdown("Navigate through the options below:")
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == '__main__':
    main()
