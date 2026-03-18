"""
Test fixtures for novel-related data structures and schemas.
Provides reusable test data for comprehensive pytest coverage.
"""

from datetime import date

import pytest

from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField

# ===== VALID NOVEL CREATE INSTANCES =====


@pytest.fixture
def minimal_novel_create():
    """Minimal valid NovelCreate with only required title field."""
    return NovelCreate(title="Minimal Novel")


@pytest.fixture
def complete_novel_create():
    """Complete NovelCreate with all fields populated."""
    return NovelCreate(
        title="Complete Test Novel",
        site="Test Site",
        url="https://example.com/novel",
        current_chapter=42,
        last_read_date=date(2024, 3, 15),
        notes="This is a test novel with all fields filled.",
    )


@pytest.fixture
def novel_create_with_whitespace():
    """NovelCreate with leading/trailing whitespace that should be stripped."""
    return NovelCreate(
        title="  Spaced Title  ", site="  Spaced Site  ", notes="  Spaced Notes  "
    )


@pytest.fixture
def novel_create_with_edge_cases():
    """NovelCreate with edge case values."""
    return NovelCreate(
        title="Title with Special Chars: !@#$%^&*()",
        site="Site with Unicode: ñáéíóú 中文 🚀",
        url="http://localhost:8000/novel",
        current_chapter=0,  # Edge case: zero chapter
        last_read_date=date.today(),  # Today's date
        notes="",  # Empty notes
    )


# ===== INVALID NOVEL CREATE DATA (for error testing) =====


@pytest.fixture
def invalid_novel_data_empty_title():
    """Data that should fail validation due to empty title."""
    return {"title": "", "site": "Valid Site"}


@pytest.fixture
def invalid_novel_data_whitespace_title():
    """Data that should fail validation due to whitespace-only title."""
    return {"title": "   \t\n   ", "site": "Valid Site"}


@pytest.fixture
def invalid_novel_data_negative_chapter():
    """Data that should fail validation due to negative chapter."""
    return {"title": "Valid Title", "current_chapter": -1}


@pytest.fixture
def invalid_novel_data_wrong_chapter_type():
    """Data that should fail validation due to wrong chapter type."""
    return {"title": "Valid Title", "current_chapter": "not_a_number"}


@pytest.fixture
def invalid_novel_data_invalid_url():
    """Data that should fail validation due to invalid URL."""
    return {"title": "Valid Title", "url": "not-a-valid-url"}


# ===== SORT FIELD ENUM VALUES =====


@pytest.fixture
def all_sort_fields():
    """All valid NovelSortField enum values."""
    return [
        NovelSortField.TITLE,
        NovelSortField.SITE,
        NovelSortField.URL,
        NovelSortField.CURRENT_CHAPTER,
        NovelSortField.LAST_READ_DATE,
    ]


# ===== EXPECTED NOVEL MODEL DATA =====


@pytest.fixture
def expected_minimal_novel_dict():
    """Expected dictionary representation of minimal novel."""
    return {
        "title": "Minimal Novel",
        "site": None,
        "url": None,
        "current_chapter": 0,
        "last_read_date": None,
        "notes": None,
    }


@pytest.fixture
def expected_complete_novel_dict():
    """Expected dictionary representation of complete novel."""
    return {
        "title": "Complete Test Novel",
        "site": "Test Site",
        "url": "https://example.com/novel",
        "current_chapter": 42,
        "last_read_date": date(2024, 3, 15),
        "notes": "This is a test novel with all fields filled.",
    }


@pytest.fixture
def expected_whitespace_stripped_novel_dict():
    """Expected dictionary after whitespace stripping."""
    return {
        "title": "Spaced Title",
        "site": "Spaced Site",
        "url": None,
        "current_chapter": 0,
        "last_read_date": None,
        "notes": "Spaced Notes",
    }
