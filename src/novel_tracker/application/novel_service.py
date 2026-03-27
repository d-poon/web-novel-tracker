import logging

from novel_tracker.domain.models.novel import Novel
from novel_tracker.domain.repositories.novel_repository import NovelRepository
from novel_tracker.schemas.sort_input import NovelSortField

logger = logging.getLogger(__name__)

repo = NovelRepository()

SORT_FIELDS = {
    NovelSortField.TITLE: lambda n: n.title,
    NovelSortField.SITE: lambda n: n.site,
    NovelSortField.URL: lambda n: n.url,
    NovelSortField.CURRENT_CHAPTER: lambda n: n.current_chapter,
    NovelSortField.LAST_READ_DATE: lambda n: n.last_read_date,
}


def add_novel_service(novel: Novel):
    existing = repo.get_novel_by_title(novel.title)

    if existing:
        raise ValueError(f"Novel with title '{novel.title}' already exists.")

    repo.add_novel(novel)
    return novel


def list_novels_service(sort_by: str):
    try:
        sort_by = NovelSortField(sort_by.lower())
    except ValueError as e:
        raise ValueError(
            f"Invalid sort field: {sort_by}. "
            f"Valid options are: {', '.join([field.value for field in NovelSortField])}"
        ) from e

    novels = repo.list_novels()

    novels.sort(
        key=SORT_FIELDS[sort_by], reverse=(sort_by != NovelSortField.TITLE)
    )  # Sort descending for chapters and dates

    return novels


def get_novel_service(title: str) -> Novel | None:
    novel = repo.get_novel_by_title(title)

    if not novel:
        raise ValueError(f"Novel not found with title '{title}'.")

    return novel


def update_novel_service(update_data: dict) -> dict:
    existing = repo.get_novel_by_title(update_data["title"])
    if not existing:
        raise ValueError(f"Novel not found with title '{update_data['title']}'.")

    if len(update_data) == 1:
        raise ValueError("No fields provided to update.")

    repo.update_novel(update_data)

    return update_data


def delete_novel_service(title: str):
    existing = repo.get_novel_by_title(title)
    if not existing:
        raise ValueError(f"Novel not found with title '{title}'.")

    repo.delete_novel(title)

    return title
