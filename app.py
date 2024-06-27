from flask import Flask, render_template, request
import pickle
import pandas
import numpy as np


popular_df = pickle.load(open('.pkl files/popular.pkl', 'rb'))
pt = pickle.load(open('.pkl files/pt.pkl', 'rb'))
books = pickle.load(open('.pkl files/books.pkl', 'rb'))
similarity_score = pickle.load(open('.pkl files/similarity_score.pkl', 'rb'))

app = Flask('__name__')


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(np.round(popular_df['avg_ratings'].values, 3)))


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books',methods=['POST'])
def recommend():
    user_input = request.form.get('user_input')
    try:
        index = np.where(pt.index == user_input)[0][0]  # Assuming user_input is a book title
        similar_items = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))

            data.append(item)
        return render_template('recommend.html', data=data)

    except (IndexError, ValueError):  # Handle potential errors during data access
        # Render a different template with an error message
        return render_template('recommend.html', message="Book not found. Please try a different title.")


if __name__=='__main__':
    app.run(debug=True)
