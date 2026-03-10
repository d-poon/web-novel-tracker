import typer

from novel_tracker.infrastructure.database.queries import initialize_db

app = typer.Typer(help="Manage database operations for your web novel tracker.")


@app.command()
def init():
    """Initialize the database and necessary files."""
    initialize_db()
    typer.echo("Web Novel Tracker initialized.")
