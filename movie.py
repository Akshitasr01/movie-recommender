import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

# Load the datasets
movies = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\tmdb_5000_movies.csv")
credits = pd.read_csv(r"C:\Users\akshi\OneDrive\Desktop\tmdb_5000_credits.csv")

print("Movies dataset shape:", movies.shape)
print("Credits dataset shape:", credits.shape)

# Merge movies and credits datasets
movies = movies.merge(credits, on='title')
print("Merged dataset shape:", movies.shape)

# Select relevant columns
movies = movies[['genres', 'title', 'overview', 'keywords', 'popularity', 'vote_count', 'id', 'cast', 'crew']]
print("Selected columns:", movies.columns.tolist())

# Check for null values
print("Null values in each column:")
print(movies.isnull().sum())

# Drop rows with null values
movies.dropna(inplace=True)
print("Dataset shape after dropping nulls:", movies.shape)

# Function to convert string representation of lists to actual lists
def convert(obj):
    l = []
    try:
        for i in ast.literal_eval(obj):
            l.append(i['name'])
        return l
    except:
        return []

# Function to get top 3 genres/keywords
def convert3(obj):
    l = []
    counter = 0
    try:
        for i in ast.literal_eval(obj):
            if counter != 3:
                l.append(i['name'])
                counter += 1
            else:
                break
        return l
    except:
        return []

# Function to get director from crew
def fetch_director(obj):
    l = []
    try:
        for i in ast.literal_eval(obj):
            if i['job'] == 'Director':
                l.append(i['name'])
                break
        return l
    except:
        return []

# Apply conversions
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert3)
movies['crew'] = movies['crew'].apply(fetch_director)

# Fill null overviews with empty string
movies['overview'] = movies['overview'].fillna("")

# Convert overview to list of words
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces from genres and keywords
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)

# Remove spaces from overview and title
movies['overview'] = movies['overview'].apply(lambda x: [i.replace(" ", "") for i in x] if isinstance(x, list) else x)
movies['title'] = movies['title'].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else x)

# Create tags column by combining all features
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Create final dataframe with only necessary columns
new_df = movies[['id', 'title', 'tags']]

# Convert tags list to string for vectorization
new_df['tags'] = new_df['tags'].apply(lambda x: ' '.join(x))

print("Final dataset shape:", new_df.shape)
print("Sample tags for first movie:")
print(new_df['tags'][0])

# Create CountVectorizer and fit it on tags
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Calculate cosine similarity
similarity = cosine_similarity(vectors)

# Function to recommend movies
def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(new_df.iloc[i[0]].title)
    
    return recommended_movies

# Test the recommender system
print("\nMovie Recommender System Ready!")
print("Available movies (first 10):")
print(new_df['title'].head(10).tolist())

# Example recommendation (uncomment and modify the movie name to test)
# movie_name = "Avatar"  # Replace with a movie from your dataset
# if movie_name in new_df['title'].values:
#     recommendations = recommend(movie_name)
#     print(f"\nRecommendations for '{movie_name}':")
#     for i, movie in enumerate(recommendations, 1):
#         print(f"{i}. {movie}")
# else:
#     print(f"Movie '{movie_name}' not found in dataset")
