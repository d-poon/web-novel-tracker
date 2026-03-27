import typer
from pydantic import ValidationError

from novel_tracker.application.builders import build_novel, build_novel_update
from novel_tracker.application.novel_service import (
    add_novel_service,
    delete_novel_service,
    get_novel_service,
    list_novels_service,
    update_novel_service,
)
from novel_tracker.cli.arguments import (
    CURRENT_CHAPTER_OPTION,
    LAST_READ_DATE_OPTION,
    NOTES_OPTION,
    SITE_OPTION,
    SORT_BY_OPTION,
    TITLE_ARG,
    URL_OPTION,
)
from novel_tracker.cli.formatters import format_novel_list_table, format_novel_typer
from novel_tracker.cli.utils import prompt_if_interactive
from novel_tracker.schemas.novel_input import NovelCreate, NovelUpdate

app = typer.Typer(help="Manage your web novel tracking with ease.")


@app.command()
def add(
    title: str = TITLE_ARG,
    site: str | None = SITE_OPTION,
    url: str | None = URL_OPTION,
    current_chapter: int | None = CURRENT_CHAPTER_OPTION,
    last_read_date: str | None = LAST_READ_DATE_OPTION,
    notes: str | None = NOTES_OPTION,
):
    """Add a new novel to the tracker."""

    # User helper function if prompts enabled
    site = prompt_if_interactive(site, "Novel Site")
    url = prompt_if_interactive(url, "Novel URL")
    current_chapter = prompt_if_interactive(current_chapter, "Current Chapter")
    last_read_date = prompt_if_interactive(last_read_date, "Last Read Date")
    notes = prompt_if_interactive(notes, "Notes")

    try:
        schema = NovelCreate(
            title=title,
            site=site,
            url=url,
            current_chapter=current_chapter,
            last_read_date=last_read_date,
            notes=notes,
        )

        novel = build_novel(schema)
        added_novel = add_novel_service(novel)
        typer.echo(f"Novel '{added_novel.title}' added successfully.")
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except ValidationError as e:
        typer.echo(f"Error adding novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except ValueError as e:
        typer.echo(f"Error adding novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1) from None


@app.command(name="list")
@app.command(name="ls")
def list_novels(
    sort_by: str = SORT_BY_OPTION,
):
    """List all tracked novels."""

    sort_by = prompt_if_interactive(sort_by, "Sort By Field")

    try:
        novels = list_novels_service(sort_by)
        typer.echo(format_novel_list_table(novels))
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except ValidationError as e:
        typer.echo(f"Error listing novels: {e}", err=True)
        raise typer.Exit(code=1) from None

    except ValueError as e:
        typer.echo(f"Error listing novels: {e}", err=True)
        raise typer.Exit(code=1) from None

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1) from None


@app.command()
def get(title: str = TITLE_ARG):
    """Get details of a specific novel by title."""
    try:
        novel = get_novel_service(title)
        typer.echo(format_novel_typer(novel))
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except ValidationError as e:
        typer.echo(f"Error getting novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except ValueError as e:
        typer.echo(f"Error getting novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1) from None


def empty_to_none(value: str | None) -> str | None:
    if value == "":
        return None
    return value


@app.command()
def update(
    title: str = TITLE_ARG,
    site: str | None = SITE_OPTION,
    url: str | None = URL_OPTION,
    current_chapter: int | None = CURRENT_CHAPTER_OPTION,
    last_read_date: str | None = LAST_READ_DATE_OPTION,
    notes: str | None = NOTES_OPTION,
):
    """Update details of an existing novel."""

    # Only convert to None and prompt if interactive if the user passed the option

    kwargs = {}

    if site is not None:
        kwargs["site"] = empty_to_none(prompt_if_interactive(site, "Novel Site"))
    if url is not None:
        kwargs["url"] = empty_to_none(prompt_if_interactive(url, "Novel URL"))
    if current_chapter is not None:
        kwargs["current_chapter"] = prompt_if_interactive(
            current_chapter, "Current Chapter"
        )
    if last_read_date is not None:
        kwargs["last_read_date"] = empty_to_none(
            prompt_if_interactive(last_read_date, "Last Read Date")
        )
    if notes is not None:
        kwargs["notes"] = empty_to_none(prompt_if_interactive(notes, "Notes"))

    try:
        schema = NovelUpdate(title=title, **kwargs)
        update_data = build_novel_update(schema)
        updated_novel = update_novel_service(update_data)
        typer.echo(f"Novel '{updated_novel['title']}' updated successfully.")
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except ValidationError as e:
        typer.echo(f"Error updating novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except ValueError as e:
        typer.echo(f"Error updating novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1) from None


@app.command()
def delete(title: str = TITLE_ARG):
    """Delete a novel from the tracker."""
    try:
        deleted_title = delete_novel_service(title)
        typer.echo(f"Novel '{deleted_title}' deleted successfully.")
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except ValidationError as e:
        typer.echo(f"Error deleting novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except ValueError as e:
        typer.echo(f"Error deleting novel: {e}", err=True)
        raise typer.Exit(code=1) from None

    except Exception as e:
        typer.echo(f"Unexpected error: {e}", err=True)
        raise typer.Exit(code=1) from None
