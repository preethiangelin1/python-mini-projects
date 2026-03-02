import os
from .api import fetch_movies
from dotenv import load_dotenv
load_dotenv()

def test_fetch_movies(mocker):
    mock_get = mocker.patch("tmdb_cli.api.requests.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "results": [
            {
                "title": "The Super Mario Bros. Movie",
                "overview": "Test overview",
                "vote_count": 1400,
                "release_date": "2023-04-05",
                "original_language": "English"
            }
        ]
    }

    movies = fetch_movies("playing")
    assert movies == [
            {
                "title": "The Super Mario Bros. Movie",
                "overview": "Test overview",
                "vote_count": 1400,
                "release_date": "2023-04-05",
                "original_language": "English"
            }
        ]
        
    url = f"https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
    TOKEN = os.getenv("TMDB_TOKEN")
    headers = {
        "accept" : "application/json",
        "Authorization" : f"Bearer {TOKEN}"
    }

    mock_get.assert_called_once_with(url, headers=headers)