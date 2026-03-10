import typer

from novel_tracker.application.novel_service import (
    add_novel_service,
    delete_novel_service,
    get_novel_service,
    list_novels_service,
    update_novel_service,
)
from novel_tracker.cli.builders import build_novel
from novel_tracker.schemas.sort_schema import NovelSortField

app = typer.Typer(help="Manage your web novel tracking with ease.")


@app.command()
def add(novel=build_novel):
    """Add a new novel to the tracker."""
    add_novel_service(novel)


@app.command(name="list")
@app.command(name="ls")
def list_novels(
    sort_by: NovelSortField = NovelSortField.TITLE,
):
    """List all tracked novels."""
    list_novels_service(sort_by)


@app.command()
def get(title: str):
    """Get details of a specific novel by title."""
    get_novel_service(title)


@app.command()
def update(novel=build_novel):
    """Update details of an existing novel."""
    update_novel_service(novel)


@app.command()
def delete(title: str):
    """Delete a novel from the tracker."""
    delete_novel_service(title)
