import argparse
from .api import fetch_movies
from .utils import print_movies

def run():
    parser = argparse.ArgumentParser(prog="tmdb_cli")
    parser.add_argument("--type")

    args = parser.parse_args()

    movies = fetch_movies(args.type)

    print_movies(movies)

   
