import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")

# Select important columns
movies = movies[['title','overview','genres']]

# Create tags column
movies['tags'] = movies['overview'] + movies['genres']
movies['tags'] = movies['tags'].fillna('')

# Convert text into vectors
tfidf = TfidfVectorizer(stop_words='english')
vectors = tfidf.fit_transform(movies['tags'])

# Calculate similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    movie = movie.lower()

    if movie not in movies['title'].str.lower().values:
        return []

    idx = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[idx]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)[1:6]

    recommended = []

    for i in distances:
        title = movies.iloc[i[0]].title
        details = get_movie_details(title)

        if details:
            recommended.append(details)

    return recommended


API_KEY = "f9c35c0"   # your omdb key

def get_movie_details(title):
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    res = requests.get(url).json()

    if res["Response"] == "True":
        return {
            "title": res["Title"],
            "poster": res["Poster"],
            "rating": res["imdbRating"]
        }
    else:
        return None

