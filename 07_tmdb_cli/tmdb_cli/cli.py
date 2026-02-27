import argparse
from .api import fetch_movies

def run():
    parser = argparse.ArgumentParser(prog="tmdb_cli")
    parser.add_argument("--type")

    args = parser.parse_args()

    fetch_movies(args.type)

   
