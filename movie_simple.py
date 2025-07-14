import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ast

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
new_df = movies[['id', 'title', 'tags']]
new_df['tags'] = new_df['tags'].apply(lambda x: ' '.join(x))

print(f"Processed {len(new_df)} movies")
print(f"Sample movie: {new_df.iloc[0]['title']}")

# Create vectors
print("Creating movie vectors...")
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Calculate similarity
print("Calculating similarities...")
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        
        recommended_movies = []
        for i in movies_list:
            recommended_movies.append(new_df.iloc[i[0]].title)
        
        return recommended_movies
    except:
        return []

print("\n" + "="*50)
print("MOVIE RECOMMENDER SYSTEM READY!")
print("="*50)

# Show some available movies
print("\nAvailable movies (first 10):")
for i, title in enumerate(new_df['title'].head(10), 1):
    print(f"{i}. {title}")

# Test with a sample movie
sample_movie = new_df.iloc[0]['title']
print(f"\nTesting with movie: {sample_movie}")

recommendations = recommend(sample_movie)
if recommendations:
    print(f"\nRecommendations for '{sample_movie}':")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")
else:
    print("No recommendations found.")

print("\n" + "="*50)
print("To get recommendations for any movie, use: recommend('Movie Title')")
print("="*50) 