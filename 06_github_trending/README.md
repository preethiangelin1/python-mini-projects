# GitHub Trending CLI

Small CLI to fetch and display trending GitHub repositories using the GitHub Search API and render a rich table.

## Features
- View trending repos for: day, week, month, year
- Filter by language and limit results
- Pretty table output via `rich`

## Requirements
- Python 3.8+
- See [06_github_trending/requirements.txt](06_github_trending/requirements.txt) or [06_github_trending/pyproject.toml](06_github_trending/pyproject.toml)

## Install
```sh
pip install -r 06_github_trending/requirements.txt
```

## Usage
Run from project root:
```sh
python -m 06_github_trending.main
```
Or use the console script (if installed):
```sh
github-trending --duration week --limit 10 --language python
```
See CLI flags in [`github_trending.cli.run`](06_github_trending/github_trending/cli.py).

## Project layout
- Entrypoint: [06_github_trending/main.py](06_github_trending/main.py)
- CLI: [`github_trending.cli.run`](06_github_trending/github_trending/cli.py)
- API logic: [`github_trending.api.api`](06_github_trending/github_trending/api.py)
- Output helpers: [`github_trending.utils.print_repos`](06_github_trending/github_trending/utils.py) and [`github_trending.utils.get_date_range`](06_github_trending/github_trending/utils.py)

## Example
Fetch top 10 repos pushed in last week:
```sh
python -m 06_github_trending.main --duration week --limit 10
```

## Notes
- The tool builds a GitHub search query (see [`github_trending.api.api`](06_github_trending/github_trending/api.py)).
- No authentication is required for basic usage but be mindful of GitHub API rate limits.