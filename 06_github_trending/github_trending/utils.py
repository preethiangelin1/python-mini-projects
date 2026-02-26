from datetime import date, timedelta
from rich.table import Table
from rich.console import Console

console = Console()

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


def get_date_range(days):
    today = date.today()
    target_date = today - timedelta(days=days)
    return f">{target_date}"