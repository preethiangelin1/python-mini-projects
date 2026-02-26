import requests
from .utils import print_repos, get_date_range


def api(duration, limit, language):
    days_map = {
        "day": 1,
        "week": 7,
        "month": 30,
        "year": 365
    }

    duration_days = days_map.get(duration)

    query = f"pushed:{get_date_range(duration_days)}" # "pushed:>2026-02-19"

    if language:
        query = query + f" language:{language}" # "pushed:>2026-02-19 language:python"

    GITHUB_API_BASE_URL = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={limit}"
    print(GITHUB_API_BASE_URL)

    response = requests.get(GITHUB_API_BASE_URL)

    repos_data = response.json()
    repos = repos_data.get("items")

    print_repos(repos)