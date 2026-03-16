from datetime import date

import pytest
from pydantic import ValidationError

from novel_tracker.domain.models.novel import Novel, row_to_novel
from novel_tracker.schemas.novel_input import NovelCreate


@pytest.mark.parametrize("input_title", ["   ", "", "\t\n\r"])
def test_title_blank_raises_value_error(input_title):
    with pytest.raises(ValueError, match="Title is required"):
        NovelCreate(title=input_title)


def test_missing_title_raises_validation_error():
    with pytest.raises(ValidationError):
        NovelCreate()


def test_title_is_stripped_and_accepts_unicode_and_long():
    t = "  The Great Novel  "
    n = NovelCreate(title=t)
    assert n.title == "The Great Novel"

    long_title = "A" * 2000
    n2 = NovelCreate(title=long_title)
    assert n2.title == long_title

    unicode_title = "小说标题"
    n3 = NovelCreate(title=unicode_title)
    assert n3.title == unicode_title


@pytest.mark.parametrize(
    "site_input,expected",
    [("  Example Site  ", "Example Site"), ("", None), (None, None), ("   ", "")],
)
def test_site_trimming_and_empty_handling(site_input, expected):
    n = NovelCreate(title="T", site=site_input)
    assert n.site == expected


def test_url_accepts_valid_and_rejects_invalid():
    good = NovelCreate(title="T", url="https://example.com/novel")
    assert str(good.url) == "https://example.com/novel"

    with pytest.raises(ValidationError):
        NovelCreate(title="T", url="not-a-valid-url")


def test_current_chapter_validation_behaviour():
    # valid values
    n0 = NovelCreate(title="T", current_chapter=0)
    assert n0.current_chapter == 0

    n5 = NovelCreate(title="T", current_chapter=5)
    assert n5.current_chapter == 5

    # negative -> ValueError from validator
    with pytest.raises(
        ValueError, match="Current chapter must be a non-negative integer"
    ):
        NovelCreate(title="T", current_chapter=-1)

    # floats and strings are rejected by pydantic for int fields
    with pytest.raises(TypeError):
        NovelCreate(title="T", current_chapter=1.5)

    with pytest.raises(TypeError):
        NovelCreate(title="T", current_chapter="10")

    # booleans are accepted by pydantic as ints (True -> 1, False -> 0)
    nb = NovelCreate(title="T", current_chapter=True)
    assert nb.current_chapter == 1

    nf = NovelCreate(title="T", current_chapter=False)
    assert nf.current_chapter == 0

    # None should map to 0 per validator
    n_none = NovelCreate(title="T", current_chapter=None)
    assert n_none.current_chapter == 0


def test_last_read_date_parsing_and_validation():
    n = NovelCreate(title="T", last_read_date="2024-01-01")
    assert isinstance(n.last_read_date, date)
    assert n.last_read_date.isoformat() == "2024-01-01"

    with pytest.raises(ValidationError):
        NovelCreate(title="T", last_read_date="not-a-date")


def test_notes_optional_preserved_and_none():
    n = NovelCreate(title="T", notes="Some notes")
    assert n.notes == "Some notes"

    n2 = NovelCreate(title="T", notes=None)
    assert n2.notes is None


def test_novel_dataclass_and_row_to_novel():
    row = {
        "title": "Row Novel",
        "site": "Site",
        "url": "https://example.org/",
        "current_chapter": 3,
        "last_read_date": "2024-02-02",
        "notes": "row notes",
    }

    novel = row_to_novel(row)
    assert isinstance(novel, Novel)
    assert novel.title == "Row Novel"
    assert novel.site == "Site"
    assert novel.url == "https://example.org/"
    assert novel.current_chapter == 3
    assert isinstance(novel.last_read_date, date)
    assert novel.last_read_date == date.fromisoformat("2024-02-02")
    assert novel.notes == "row notes"


def test_row_to_novel_missing_key_raises():
    row = {"title": "X"}
    with pytest.raises(KeyError):
        row_to_novel(row)


def test_row_to_novel_non_iso_date_raises_value_error():
    row = {
        "title": "Row Novel",
        "site": None,
        "url": None,
        "current_chapter": 1,
        "last_read_date": "02-02-2024",
        "notes": None,
    }
    with pytest.raises(ValueError):
        row_to_novel(row)


def test_row_to_novel_numeric_chapter_as_string_is_preserved():
    row = {
        "title": "Row Novel",
        "site": None,
        "url": None,
        "current_chapter": "3",
        "last_read_date": None,
        "notes": None,
    }
    novel = row_to_novel(row)
    assert novel.current_chapter == "3"


def test_url_edge_cases_and_scheme_rejection():
    # query params and percent-encoding accepted
    n = NovelCreate(title="T", url="https://example.com/novel?chapter=1&lang=en")
    assert str(n.url).endswith("/novel?chapter=1&lang=en")

    # ftp scheme should be rejected by HttpUrl
    with pytest.raises(ValidationError):
        NovelCreate(title="T", url="ftp://example.com/resource")


def test_current_chapter_extremely_large():
    big = 10**18
    n = NovelCreate(title="T", current_chapter=big)
    assert n.current_chapter == big


def test_last_read_date_leap_and_future_dates():
    n = NovelCreate(title="T", last_read_date="2024-02-29")
    assert n.last_read_date == date.fromisoformat("2024-02-29")

    future = NovelCreate(title="T", last_read_date="2999-01-01")
    assert future.last_read_date == date.fromisoformat("2999-01-01")


def test_notes_preserve_large_content():
    large = "x" * 100_000
    n = NovelCreate(title="T", notes=large)
    assert n.notes == large
