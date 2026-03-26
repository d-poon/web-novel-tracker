import logging
from dataclasses import asdict

import typer

from novel_tracker.cli.formatters import (
    format_novel_list_table,
    format_novel_typer,
)
from novel_tracker.domain.models.novel import Novel
from novel_tracker.domain.repositories.novel_repository import (
    add_novel,
    delete_novel,
    get_novel_by_title,
    list_novels,
    update_novel,
)
from novel_tracker.schemas.sort_input import NovelSortField

logger = logging.getLogger(__name__)

SORT_FIELDS = {
    "title": lambda n: n.title,
    "site": lambda n: n.site,
    "current_chapter": lambda n: n.current_chapter,
    "last_read_date": lambda n: n.last_read_date,
}


def add_novel_service(novel: Novel):
    existing = get_novel_by_title(novel.title)

    if existing:
        raise ValueError(f"Novel with title '{novel.title}' already exists.")

    add_novel(novel)
    typer.echo(f"Novel added: {novel.title}")


def list_novels_service(sort_by: NovelSortField):
    novels = list_novels()

    if sort_by not in SORT_FIELDS:
        raise ValueError(
            f"Invalid sort field: {sort_by}. "
            f"Valid options are: {', '.join(SORT_FIELDS.keys())}"
        )

    novels.sort(
        key=SORT_FIELDS[sort_by], reverse=(sort_by != "title")
    )  # Sort descending for chapters and dates

    typer.echo(format_novel_list_table(novels))


def get_novel_service(title: str) -> Novel | None:
    novel = get_novel_by_title(title)

    if novel:
        typer.echo(format_novel_typer(novel))
        return novel
    else:
        logger.warning("Novel not found: %s", title)
        return None


def update_novel_service(novel: Novel):
    existing = get_novel_by_title(novel.title)
    if not existing:
        raise ValueError(f"Novel with title '{novel.title}' not found.")

    novelData = asdict(novel)  # Convert Novel dataclass to dictionary
    novelData = {
        k: v for k, v in novelData.items() if v is not None
    }  # Filter out None values

    update_novel(novelData)

    typer.echo(f"Novel updated: {novel.title}")


def delete_novel_service(title: str):
    existing = get_novel_by_title(title)
    if not existing:
        raise ValueError(f"Novel with title '{title}' not found.")

    delete_novel(title)

    typer.echo(f"Novel deleted: {title}")
