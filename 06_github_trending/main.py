import argparse
import requests
from datetime import date, timedelta
from rich.table import Table
from rich.console import Console

duration_choices = ["day","week","month","year"]
console = Console()

parser = argparse.ArgumentParser(prog = "github-trending")
parser.add_argument("-d", "--duration", default="week", choices=duration_choices)
parser.add_argument("--limit", default=10, type=int)
parser.add_argument("-l","--language")

def get_date_range(days):
    today = date.today()
    target_date = today - timedelta(days=days)
    return f">{target_date}"

def print_repos(repos):
    if not repos:
        console.print(
            "[yellow]⚠️  No repositories found for the given criteria.[/yellow]"
        )
        return
    
    table = Table(title="GitHub Trending Repos")
    table.add_column("Rank", width=6, style="bold green")
    table.add_column("Repository")
    table.add_column("Language")
    table.add_column("⭐ Stars", justify="right")
    table.add_column("🍴 Forks", justify="right")
    table.add_column("Description", max_width=50)

    rank = 1
    for repo in repos:
        lang = repo.get("language") or "-"
        stars = str(repo.get("stargazers_count"))
        forks = str(repo.get("forks_count"))
        description = repo.get("description", "No description")[:100] or "No description"
        
        table.add_row(str(rank), repo.get("name"), lang, stars, forks, description)
        rank += 1

    console.print(table)

args = parser.parse_args()

days_map = {
    "day": 1,
    "week": 7,
    "month": 30,
    "year": 365
}

duration_days = days_map.get(args.duration)

query = f"pushed:{get_date_range(duration_days)}"

if args.language:
    query = query + f" language:{args.language}" 

GITHUB_API_BASE_URL = f"https://api.github.com/search/repositories?q={query}&sort=stars&order=desc&per_page={args.limit}"

response = requests.get(GITHUB_API_BASE_URL)

repos_data = response.json()
repos = repos_data.get("items")
print_repos(repos)