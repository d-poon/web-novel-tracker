from novel_tracker.cli.arguments import (
    SORT_BY_OPTION,
)
from novel_tracker.domain.models.novel import Novel
from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField


def normalize_url(url: str | None) -> str | None:
    return str(url).rstrip("/") if url else None


def build_novel(schema: NovelCreate) -> Novel:
    data = schema.model_dump()

    return Novel(
        title=data["title"],
        site=data.get("site"),
        url=normalize_url(data.get("url")),
        current_chapter=data.get("current_chapter"),
        last_read_date=data.get("last_read_date"),
        notes=data.get("notes"),
    )


def build_sort_by_input(
    sort_by: NovelSortField = SORT_BY_OPTION,
) -> NovelSortField:
    return sort_by
