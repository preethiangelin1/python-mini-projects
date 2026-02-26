import argparse
from .api import api

def run():
    duration_choices = ["day","week","month","year"]

    parser = argparse.ArgumentParser(prog = "github-trending")
    parser.add_argument("-d", "--duration", default="week", choices=duration_choices)
    parser.add_argument("--limit", default=10, type=int)
    parser.add_argument("-l","--language")

    args = parser.parse_args()

    api(args.duration, args.limit, args.language)
    
