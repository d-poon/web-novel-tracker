from novel_tracker.cli.arguments import (
    SORT_BY_OPTION,
)
from novel_tracker.domain.models.novel import Novel
from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField


def build_novel(schema: NovelCreate) -> Novel:
    return Novel(**schema.model_dump())


def build_sort_by_input(
    sort_by: NovelSortField = SORT_BY_OPTION,
) -> NovelSortField:
    return sort_by
