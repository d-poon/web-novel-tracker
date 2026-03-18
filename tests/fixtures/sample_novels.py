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


# ===== PARAMETERIZED TEST CASES =====


@pytest.fixture(
    params=[
        ("Valid Title", True),
        ("Title with Numbers 123", True),
        ("Title with Special !@#$", True),
        ("Unicode Title: ñáéíóú 中文", True),
        ("", False),  # Empty title should fail
        ("   \t\n   ", False),  # Whitespace-only should fail
    ]
)
def title_validation_case(request):
    """Parameterized fixture for title validation test cases."""
    title, should_pass = request.param
    return title, should_pass


@pytest.fixture(
    params=[
        (None, None),  # None should remain None
        ("", None),  # Empty string should become None
        ("Valid Site", "Valid Site"),  # Normal site
        ("  Spaced Site  ", "Spaced Site"),  # Should be stripped
        ("Site with Unicode: ñáéíóú", "Site with Unicode: ñáéíóú"),  # Unicode preserved
    ]
)
def site_validation_case(request):
    """Parameterized fixture for site validation test cases."""
    input_value, expected_output = request.param
    return input_value, expected_output


@pytest.fixture(
    params=[
        (None, 0),  # None should default to 0
        (0, 0),  # Zero should be valid
        (1, 1),  # Positive int should be valid
        (1000, 1000),  # Large positive should be valid
        (True, 1),  # Boolean True -> 1
        (False, 0),  # Boolean False -> 0
    ]
)
def valid_current_chapter_case(request):
    """Parameterized fixture for valid current_chapter values."""
    input_value, expected_output = request.param
    return input_value, expected_output


@pytest.fixture(
    params=[
        (-1, "Current chapter must be a non-negative integer"),  # Negative should fail
        (
            -100,
            "Current chapter must be a non-negative integer",
        ),  # Large negative should fail
    ]
)
def invalid_current_chapter_case(request):
    """Parameterized fixture for invalid current_chapter values."""
    input_value, expected_error = request.param
    return input_value, expected_error


@pytest.fixture(
    params=[
        (1.5, TypeError),  # Float should raise TypeError
        ("5", TypeError),  # String should raise TypeError
        ([5], TypeError),  # List should raise TypeError
        ({"chapter": 5}, TypeError),  # Dict should raise TypeError
    ]
)
def invalid_current_chapter_type_case(request):
    """Parameterized fixture for invalid current_chapter types."""
    input_value, expected_exception = request.param
    return input_value, expected_exception


@pytest.fixture(
    params=[
        "https://example.com/",
        "http://example.com/path/",
        "https://subdomain.example.com/novel/",
        "http://localhost:8000/",
        "https://example.com/path?query=value&other=123/",
    ]
)
def valid_url_case(request):
    """Parameterized fixture for valid URL test cases."""
    return request.param


@pytest.fixture(
    params=[
        "not-a-url",
        "ftp://example.com",  # Wrong scheme
        "example.com",  # Missing scheme
        "https://",  # Incomplete
        "",  # Empty string
    ]
)
def invalid_url_case(request):
    """Parameterized fixture for invalid URL test cases."""
    return request.param
