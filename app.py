from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast
import pickle
import os

app = Flask(__name__)

# Global variables to store the model and data
movies_df = None
similarity_matrix = None
cv = None

def load_and_process_data():
    """Load and process the movie data"""
    global movies_df, similarity_matrix, cv
    
    print("Loading movie datasets...")
    
    # Load the datasets
    movies = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\tmdb_5000_movies.csv")
    credits = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\tmdb_5000_credits.csv")
    
    print(f"Movies dataset: {movies.shape}")
    print(f"Credits dataset: {credits.shape}")
    
    # Merge datasets
    movies = movies.merge(credits, on='title')
    print(f"Merged dataset: {movies.shape}")
    
    # Select relevant columns
    movies = movies[['genres', 'title', 'overview', 'keywords', 'id', 'cast', 'crew']]
    
    # Handle missing values
    movies['overview'] = movies['overview'].fillna("")
    movies.dropna(inplace=True)
    print(f"Final dataset: {movies.shape}")
    
    # Function to convert string lists to actual lists
    def convert(obj):
        try:
            l = []
            for i in ast.literal_eval(obj):
                l.append(i['name'])
            return l
        except:
            return []

    def fetch_director(obj):
        try:
            l = []
            for i in ast.literal_eval(obj):
                if i['job'] == 'Director':
                    l.append(i['name'])
                    break
            return l
        except:
            return []

    print("Processing movie features...")
    
    # Apply conversions
    movies['genres'] = movies['genres'].apply(convert)
    movies['keywords'] = movies['keywords'].apply(convert)
    movies['cast'] = movies['cast'].apply(convert)
    movies['crew'] = movies['crew'].apply(fetch_director)
    
    # Convert overview to list of words
    movies['overview'] = movies['overview'].apply(lambda x: x.split())
    
    # Clean up text (remove spaces)
    movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
    movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
    movies['overview'] = movies['overview'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
    
    # Create tags
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    
    # Create final dataframe
    movies_df = movies[['id', 'title', 'tags']].copy()
    movies_df['tags'] = movies_df['tags'].apply(lambda x: ' '.join(x))
    
    print(f"Processed {len(movies_df)} movies")
    
    # Create vectors
    print("Creating movie vectors...")
    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies_df['tags']).toarray()
    
    # Calculate similarity
    print("Calculating similarities...")
    similarity_matrix = cosine_similarity(vectors)
    
    print("Data processing complete!")

def recommend_movies(movie_title):
    """Get movie recommendations"""
    try:
        movie_index = movies_df[movies_df['title'] == movie_title].index[0]
        distances = similarity_matrix[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(movies_df.iloc[i[0]].title)
        
        return recommended_movies
    except:
        return []

def search_movies(query):
    """Search for movies by title"""
    if not query:
        return []
    
    query = query.lower()
    matching_movies = []
    
    for title in movies_df['title']:
        if query in title.lower():
            matching_movies.append(title)
            if len(matching_movies) >= 10:  # Limit to 10 results
                break
    
    return matching_movies

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/api/search')
def search():
    """API endpoint for movie search"""
    query = request.args.get('q', '')
    results = search_movies(query)
    return jsonify(results)

@app.route('/api/recommend')
def recommend():
    """API endpoint for movie recommendations"""
    movie_title = request.args.get('movie', '')
    recommendations = recommend_movies(movie_title)
    return jsonify(recommendations)

@app.route('/api/movies')
def get_movies():
    """API endpoint to get all movies"""
    movies_list = movies_df['title'].tolist()
    return jsonify(movies_list)

if __name__ == '__main__':
    # Load data when starting the app
    load_and_process_data()
    
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    print("Starting Flask web server...")
    app.run(debug=True, host='0.0.0.0', port=5000) 