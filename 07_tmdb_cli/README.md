# TMDB CLI

A small command-line tool to fetch movie lists from The Movie Database (TMDB) API and display them in a rich table.

## Features
- Fetch now playing / top rated / popular / upcoming movies
- Pretty table output using `tmdb_cli.utils.print_movies`
- Configurable via TMDB token in a `.env` file

## Requirements
- Python 3.8+
- See `requirements.txt` or `pyproject.toml`

## Setup
1. Install dependencies:
```sh
pip install -r requirements.txt
```
2. Set your TMDB token in a `.env` file (see `.env.example`):
```env
TMDB_TOKEN=your_token_here
```

## Usage
Run from project root:
```sh
python -m tmdb_cli --type playing
```
Or call the CLI entrypoint (if installed as package):
```sh
tmdb-cli --type popular
```

## CLI Options
- `--type` (required) — one of: `playing`, `top`, `popular`, `upcoming`
- `--page` — page number (default: 1)
- `--limit` — max movies to display (default: 20)
- `--help` — show help

(See `tmdb_cli/cli.py` for exact flags and defaults.)

## Examples
Fetch now playing (page 1):
```sh
python -m tmdb_cli --type playing --page 1 --limit 10
```
Fetch top rated:
```sh
python -m tmdb_cli --type top
```

## Configuration
- TMDB token is read from `TMDB_TOKEN` environment variable or `.env`.
- Optionally set `TMDB_API_URL` to override base URL.


## Project layout
- `main.py` — program entry used for development runs
- `tmdb_cli/cli.py` — CLI parsing and orchestration
- `tmdb_cli/api.py` — TMDB HTTP interactions
- `tmdb_cli/utils.py` — printing and helpers


## Acknowledgements
Powered by The Movie Database (TMDB) API.