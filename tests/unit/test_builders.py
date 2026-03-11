import pytest

from novel_tracker.application.builders import build_novel, build_sort_by_input
from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField


@pytest.mark.parametrize(
    "field",
    [
        NovelSortField.TITLE,
        NovelSortField.SITE,
        NovelSortField.CURRENT_CHAPTER,
        NovelSortField.LAST_READ_DATE,
    ],
)
def test_build_sort_by_input_returns_enum(field):
    sort_by = build_sort_by_input(field)
    assert sort_by == field


def test_build_novel_creates_model():
    novel_input = NovelCreate(
        title="Test Novel",
        site="Test Site",
        url="http://example.com",
        current_chapter=5,
        last_read_date="2024-01-01",
    )

    novel = build_novel(novel_input)

    assert novel.title == "Test Novel"
    assert novel.site == "Test Site"
    assert novel.url == "http://example.com"
    assert novel.current_chapter == 5
    assert novel.last_read_date == "2024-01-01"
