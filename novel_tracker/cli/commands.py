import typer

from novel_tracker.cli.builders import build_novel, build_sort_by_input
from novel_tracker.database.queries import initialize_db
from novel_tracker.models.novel import Novel
from novel_tracker.services.novel_services import (
    add_novel_service,
    delete_novel_service,
    get_novel_service,
    list_novels_service,
    update_novel_service,
)


def register_commands(app: typer.Typer):

    @app.command()
    def init():
        """Initialize the database and necessary files."""
        initialize_db()
        typer.echo("Web Novel Tracker initialized.")

    @app.command()
    def add(novel: Novel = build_novel):
        """Add a new novel to the tracker."""
        add_novel_service(novel)

    @app.command(name="list")
    @app.command(name="ls")
    def list(sort_by: str = build_sort_by_input):
        """List all tracked novels."""
        list_novels_service(sort_by)

    @app.command()
    def get(title: str):
        """Get details of a specific novel by title."""
        get_novel_service(title)

    @app.command()
    def update(novel: Novel = build_novel):
        """Update details of an existing novel."""
        update_novel_service(novel)

    @app.command()
    def delete(title: str):
        """Delete a novel from the tracker."""
        delete_novel_service(title)
