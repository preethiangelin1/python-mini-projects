from rich.table import Table
from rich.console import Console

console = Console()

def print_movies(movies):
    if not movies:
        console.print(
            "[yellow]⚠️  No movies found for the given criteria.[/yellow]"
        )
        return
    
    table = Table(title="TMDB CLI TOOL", show_lines=True)
    table.add_column("Title")
    table.add_column("Overview")
    table.add_column("Vote Count")
    table.add_column("Release Date")
    table.add_column("Original Language")

    for movie in movies:
        title = movie.get("title") 
        overview = movie.get("overview")
        vote_count = str(movie.get("vote_count"))
        release_date = movie.get("release_date")
        original_lang = movie.get("original_language")
        
        table.add_row(title, overview, vote_count, release_date, original_lang)

    console.print(table)