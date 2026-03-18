"""
Pytest configuration and shared fixtures for the novel tracker test suite.
"""

import pytest

from tests.fixtures.sample_novels import *  # noqa


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
