"""
Comprehensive tests for builder functions in novel_tracker.application.builders.

Tests cover:
- build_novel() function with various inputs
- build_sort_by_input() function
- Integration with schema validation
- Error handling and edge cases
"""

from datetime import date

import pytest

from novel_tracker.application.builders import build_novel, build_sort_by_input
from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField


class TestBuildNovelFunction:
    """Test the build_novel builder function."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_minimal_input(
        self, minimal_novel_create, expected_minimal_novel_dict
    ):
        """Test building novel with minimal input."""
        novel = build_novel(minimal_novel_create)

        assert novel.title == expected_minimal_novel_dict["title"]
        assert novel.site == expected_minimal_novel_dict["site"]
        assert novel.url == expected_minimal_novel_dict["url"]
        assert novel.current_chapter == expected_minimal_novel_dict["current_chapter"]
        assert novel.last_read_date == expected_minimal_novel_dict["last_read_date"]
        assert novel.notes == expected_minimal_novel_dict["notes"]

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_complete_input(
        self, complete_novel_create, expected_complete_novel_dict
    ):
        """Test building novel with complete input."""
        novel = build_novel(complete_novel_create)

        assert novel.title == expected_complete_novel_dict["title"]
        assert novel.site == expected_complete_novel_dict["site"]
        assert novel.url == expected_complete_novel_dict["url"]
        assert novel.current_chapter == expected_complete_novel_dict["current_chapter"]
        assert novel.last_read_date == expected_complete_novel_dict["last_read_date"]
        assert novel.notes == expected_complete_novel_dict["notes"]

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_whitespace_handling(
        self, novel_create_with_whitespace, expected_whitespace_stripped_novel_dict
    ):
        """Test that build_novel handles whitespace stripping correctly."""
        novel = build_novel(novel_create_with_whitespace)

        assert novel.title == expected_whitespace_stripped_novel_dict["title"]
        assert novel.site == expected_whitespace_stripped_novel_dict["site"]
        assert novel.notes == expected_whitespace_stripped_novel_dict["notes"]

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_edge_cases(self, novel_create_with_edge_cases):
        """Test building novel with edge case values."""
        novel = build_novel(novel_create_with_edge_cases)

        assert novel.title == "Title with Special Chars: !@#$%^&*()"
        assert novel.site == "Site with Unicode: ñáéíóú 中文 🚀"
        assert novel.url == "http://localhost:8000/novel"
        assert novel.current_chapter == 0
        assert novel.last_read_date == date.today()
        assert novel.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_url_conversion(self):
        """Test that HttpUrl is properly converted to string in Novel model."""
        url_input = NovelCreate(title="Test", url="https://example.com/novel")
        novel = build_novel(url_input)

        # Novel model expects string URL, not HttpUrl
        assert isinstance(novel.url, str)
        assert novel.url == "https://example.com/novel"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_date_preservation(self):
        """Test that date objects are preserved correctly."""
        test_date = date(2024, 3, 15)
        date_input = NovelCreate(title="Test", last_read_date=test_date)
        novel = build_novel(date_input)

        assert novel.last_read_date == test_date
        assert isinstance(novel.last_read_date, date)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_none_handling(self):
        """Test that None values are handled correctly."""
        none_input = NovelCreate(
            title="Test",
            site=None,
            url=None,
            current_chapter=None,
            last_read_date=None,
            notes=None,
        )
        novel = build_novel(none_input)

        assert novel.site is None
        assert novel.url is None
        assert novel.current_chapter == 0  # None becomes 0 for current_chapter
        assert novel.last_read_date is None
        assert novel.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_type_coercion(self):
        """Test that type coercion works through the builder."""
        # Test boolean to int coercion for current_chapter
        bool_input = NovelCreate(title="Test", current_chapter=True)
        novel = build_novel(bool_input)
        assert novel.current_chapter == 1

        # Test False boolean
        false_input = NovelCreate(title="Test", current_chapter=False)
        novel = build_novel(false_input)
        assert novel.current_chapter == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_field_mapping(self):
        """Test that all fields are correctly mapped from schema to model."""
        input_data = NovelCreate(
            title="Mapping Test",
            site="Mapping Site",
            url="https://mapping.example.com",
            current_chapter=99,
            last_read_date=date(2023, 12, 25),
            notes="Field mapping notes",
        )
        novel = build_novel(input_data)

        # Verify all fields are mapped correctly
        assert novel.title == "Mapping Test"
        assert novel.site == "Mapping Site"
        assert novel.url == "https://mapping.example.com"
        assert novel.current_chapter == 99
        assert novel.last_read_date == date(2023, 12, 25)
        assert novel.notes == "Field mapping notes"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_creates_new_instance(self):
        """Test that build_novel creates a new Novel instance, not modifying input."""
        original = NovelCreate(title="Original", current_chapter=5)
        novel = build_novel(original)

        # Modify the built novel
        novel.current_chapter = 10

        # Original should be unchanged
        assert original.current_chapter == 5
        assert novel.current_chapter == 10


class TestBuildSortByInputFunction:
    """Test the build_sort_by_input builder function."""

    @pytest.mark.parametrize(
        "field",
        [
            NovelSortField.TITLE,
            NovelSortField.SITE,
            NovelSortField.URL,
            NovelSortField.CURRENT_CHAPTER,
            NovelSortField.LAST_READ_DATE,
        ],
    )
    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_sort_by_input_returns_enum(self, field):
        """Test that build_sort_by_input returns the input enum unchanged."""
        result = build_sort_by_input(field)
        assert result == field
        assert isinstance(result, NovelSortField)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_sort_by_input_all_fields(self, all_sort_fields):
        """Test build_sort_by_input with all possible sort fields."""
        for field in all_sort_fields:
            result = build_sort_by_input(field)
            assert result == field
            assert isinstance(result, NovelSortField)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_sort_by_input_string_conversion(self):
        """Test that enum values work as strings."""
        result = build_sort_by_input(NovelSortField.TITLE)
        assert str(result) == "title"

        result = build_sort_by_input(NovelSortField.CURRENT_CHAPTER)
        assert str(result) == "current_chapter"


class TestBuilderIntegrationWithValidation:
    """Integration tests combining builders with schema validation."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_with_validated_schema(self):
        """Test that builders work with properly validated schemas."""
        # Create a valid schema
        schema = NovelCreate(
            title="Integration Test",
            site="Integration Site",
            url="https://integration.example.com",
            current_chapter=25,
            last_read_date=date(2024, 6, 15),
            notes="Integration test notes",
        )

        # Build the novel
        novel = build_novel(schema)

        # Verify the result
        assert novel.title == "Integration Test"
        assert novel.site == "Integration Site"
        assert novel.url == "https://integration.example.com"
        assert novel.current_chapter == 25
        assert novel.last_read_date == date(2024, 6, 15)
        assert novel.notes == "Integration test notes"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_builders_handle_validation_errors_upstream(self):
        """Test that builders don't need to handle validation errors (schemas do)."""
        # This test verifies that if invalid data gets past schema validation,
        # the builder functions don't crash (though in practice, invalid data
        # should be caught by schema validation before reaching builders)

        # Create a minimal valid schema (bypassing validation for testing)
        class MockSchema:
            def __init__(self, **kwargs):
                for k, v in kwargs.items():
                    setattr(self, k, v)

            def model_dump(self):
                return {
                    "title": getattr(self, "title", None),
                    "site": getattr(self, "site", None),
                    "url": getattr(self, "url", None),
                    "current_chapter": getattr(self, "current_chapter", None),
                    "last_read_date": getattr(self, "last_read_date", None),
                    "notes": getattr(self, "notes", None),
                }

        # Test with None title (would normally be caught by validation)
        mock_schema = MockSchema(title=None)
        novel = build_novel(mock_schema)
        assert novel.title is None  # Builder just passes through

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_builder_chain_with_sort_field(self):
        """Test using both builders together."""
        # Create a novel
        novel_schema = NovelCreate(title="Chain Test")
        novel = build_novel(novel_schema)

        # Use sort field
        sort_field = build_sort_by_input(NovelSortField.TITLE)

        # Verify both work
        assert novel.title == "Chain Test"
        assert sort_field == NovelSortField.TITLE


class TestBuilderErrorHandling:
    """Test error handling in builder functions."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_novel_none_input(self):
        """Test build_novel with None input."""
        with pytest.raises(AttributeError):
            build_novel(None)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_sort_by_input_none(self):
        """Test build_sort_by_input with None input."""
        # This should work since the function just returns the input
        result = build_sort_by_input(None)
        assert result is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_build_sort_by_input_invalid_type(self):
        """Test build_sort_by_input with invalid type."""
        # Function just returns input, no validation
        result = build_sort_by_input("invalid")
        assert result == "invalid"
