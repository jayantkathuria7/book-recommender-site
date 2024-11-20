# 📚 Book Recommender App

A **Streamlit**-based Book Recommender app that allows users to explore popular books, search for specific books, and receive personalized book recommendations based on content similarity and genre-based factors. This app helps users discover new books to read with ease.

You can access the live app here: [Book Recommender App](https://book-recommender-app.streamlit.app/)

## Features
- **Top 50 Popular Books:** Display a list of the top 50 popular books with their details (title, author, ratings, etc.) and allow users to search through them.
- **Book Recommendations:** Recommend books similar to a user-selected book using a content-based recommendation system. Future versions will improve recommendations based on book genres.
- **Image Support:** Displays book cover images fetched from external URLs.
- **Responsive Layout:** The app features a dynamic layout that adjusts to various screen sizes.
- **Search & Filter:** Users can search for books or filter them by title and author.

## Technologies Used
- **Streamlit:** For creating the user interface and managing app flow.
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical computations.
- **Pillow:** For image handling (book cover images).
- **Requests:** To fetch book images from external URLs.
- **Python:** For backend logic and algorithms.
- **Scikit-learn (optional in future):** For advanced machine learning models (like collaborative filtering).

## Live Demo
You can try out the app live at the following URL:  
[Book Recommender App](https://book-recommender-app.streamlit.app/)

Feel free to explore, search for your favorite books, and get recommendations!

## Installation

To run this app locally, follow the steps below:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/book-recommender-app.git
   cd book-recommender-app
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and go to `http://localhost:8501` to interact with the app.

## Dataset
This app uses the following datasets:
- **books.csv:** Contains information about the books (titles, authors, genres, etc.).
- **ratings.csv:** Includes user ratings for the books (used for collaborative filtering and improving recommendations).
- **users.csv:** Contains user information (for future enhancements such as user profiles).

## Key Features to Explore
1. **Search for Books:** You can search for books based on their title or author.
2. **Personalized Recommendations:** After selecting a book, the app suggests similar books based on content similarity and genre.
3. **Book Details:** Each book’s title, author, rating, and cover image are displayed for easy browsing.
4. **Mobile-Friendly Design:** The layout is responsive, ensuring a great experience on both desktop and mobile devices.

## Future Enhancements
- **Genre-Based Recommendations:** The app will be updated to provide better book recommendations based on the genre of books.
- **User Profiles:** Add user authentication to save book preferences and reading history.
- **Collaborative Filtering:** Integrate collaborative filtering algorithms to provide more personalized recommendations based on user behavior.
- **Visualization of Ratings:** Add charts and graphs to visualize the rating distributions or genres of books.
- **Multilingual Support:** Extend the app to support multiple languages for a wider audience.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a pull request.


### Contact
If you have any questions or suggestions, feel free to contact me at [jayantkathuria7@gmail.com].


### Additional Notes:
- **Planned Dataset Updates:** The dataset will be frequently updated to reflect new book ratings and user reviews. Future improvements include handling genre-based filtering and using a hybrid recommendation model to improve recommendations.
