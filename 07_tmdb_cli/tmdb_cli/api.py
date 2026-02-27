import requests
import os
from dotenv import load_dotenv
from .utils import print_movies

load_dotenv()

def fetch_movies(type):
    TOKEN = os.getenv("TMDB_TOKEN")
    movie_types = {
        "playing": "now_playing",
        "top": "top_rated",
        "popular": "popular",
        "upcoming": "upcoming"
    }

    movie_type = movie_types.get(type)

    url = f"https://api.themoviedb.org/3/movie/{movie_type}?language=en-US&page=1"

    headers = {
        "accept" : "application/json",
        "Authorization" : f"Bearer {TOKEN}"
    }
    try:
        response = requests.get(url, headers=headers)
        movies_data = response.json()
        print_movies(movies_data.get("results"))

    except requests.exceptions.HTTPError as e:
        print(f"🌐 HTTP error occurred: {e}")

    except requests.exceptions.RequestException as e:
        print(f"🌐 Network error: {e}")

    except requests.exceptions.ConnectionError as e:
        print(f"🌐 Connection error: {e}")

