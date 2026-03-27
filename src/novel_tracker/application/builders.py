from novel_tracker.cli.arguments import (
    SORT_BY_OPTION,
)
from novel_tracker.domain.models.novel import Novel
from novel_tracker.schemas.novel_input import NovelCreate, NovelUpdate
from novel_tracker.schemas.sort_input import NovelSortField


def normalize_url(url: str | None) -> str | None:
    return str(url).rstrip("/") if url else None


def build_novel(schema: NovelCreate) -> Novel:
    data = schema.model_dump()

    # Default current_chapter to 0 if not provided
    if data.get("current_chapter") is None:
        data["current_chapter"] = 0
    elif data["current_chapter"] < 0:
        raise ValueError("Current chapter cannot be negative.")

    return Novel(
        title=data["title"],
        site=data.get("site"),
        url=normalize_url(data.get("url")),
        current_chapter=data.get("current_chapter"),
        last_read_date=data.get("last_read_date"),
        notes=data.get("notes"),
    )


def build_novel_update(schema: NovelUpdate) -> dict:
    data = schema.model_dump(exclude_unset=True)

    # Validate current_chapter if provided
    if "current_chapter" in data and data["current_chapter"] is not None:
        if data["current_chapter"] < 0:
            raise ValueError("Current chapter cannot be negative.")

    # Normalize URL if present
    if "url" in data:
        data["url"] = normalize_url(data["url"])

    return data


def build_sort_by_input(
    sort_by: NovelSortField = SORT_BY_OPTION,
) -> NovelSortField:
    return sort_by
