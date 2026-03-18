"""
Comprehensive tests for schema validation in novel_tracker.schemas.

Tests cover:
- NovelCreate model validation (all field validators)
- NovelSortField enum validation
- Edge cases, error scenarios, and type coercion
"""

from datetime import date

import pytest
from pydantic import ValidationError

from novel_tracker.schemas.novel_input import NovelCreate
from novel_tracker.schemas.sort_input import NovelSortField


class TestNovelCreateTitleValidator:
    """Test the title field validator."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_valid_titles(self, title_validation_case):
        """Test that valid titles pass validation."""
        title, should_pass = title_validation_case
        if should_pass:
            novel = NovelCreate(title=title)
            assert novel.title == title.strip() if title else title
        else:
            with pytest.raises(ValidationError):
                NovelCreate(title=title)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_title_stripping(self):
        """Test that leading/trailing whitespace is stripped from title."""
        novel = NovelCreate(title="  Spaced Title  ")
        assert novel.title == "Spaced Title"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_title_with_special_characters(self):
        """Test title with various special characters."""
        special_title = "Title: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        novel = NovelCreate(title=special_title)
        assert novel.title == special_title

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_title_unicode_support(self):
        """Test title with Unicode characters."""
        unicode_title = "小说标题 ñáéíóú 中文 🚀"
        novel = NovelCreate(title=unicode_title)
        assert novel.title == unicode_title

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_title_very_long(self):
        """Test title with very long content."""
        long_title = "A" * 1000
        novel = NovelCreate(title=long_title)
        assert novel.title == long_title


class TestNovelCreateSiteValidator:
    """Test the site field validator."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_site_validation_cases(self, site_validation_case):
        """Test various site input cases."""
        input_value, expected_output = site_validation_case
        novel = NovelCreate(title="Test", site=input_value)
        assert novel.site == expected_output

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_site_special_characters(self):
        """Test site with special characters."""
        site = "Site with Special: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        novel = NovelCreate(title="Test", site=site)
        assert novel.site == site

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_site_unicode(self):
        """Test site with Unicode characters."""
        site = "Site with Unicode: ñáéíóú 中文 🚀"
        novel = NovelCreate(title="Test", site=site)
        assert novel.site == site


class TestNovelCreateUrlValidator:
    """Test the url field validator."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_valid_urls(self, valid_url_case):
        """Test that valid URLs pass validation."""
        novel = NovelCreate(title="Test", url=valid_url_case)
        assert str(novel.url) == valid_url_case

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_invalid_urls(self, invalid_url_case):
        """Test that invalid URLs raise ValidationError."""
        with pytest.raises(ValidationError):
            NovelCreate(title="Test", url=invalid_url_case)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_url_none(self):
        """Test that None URL is valid."""
        novel = NovelCreate(title="Test", url=None)
        assert novel.url is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_url_with_fragment_and_query(self):
        """Test URL with fragment and query parameters."""
        url = "https://example.com/path?param=value#fragment"
        novel = NovelCreate(title="Test", url=url)
        assert str(novel.url) == url


class TestNovelCreateCurrentChapterValidator:
    """Test the current_chapter field validator (complex - has two validators)."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_valid_current_chapter_values(self, valid_current_chapter_case):
        """Test valid current_chapter values."""
        input_value, expected_output = valid_current_chapter_case
        novel = NovelCreate(title="Test", current_chapter=input_value)
        assert novel.current_chapter == expected_output

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_current_chapter_none_defaults_to_zero(self):
        """Test that None current_chapter defaults to 0."""
        novel = NovelCreate(title="Test", current_chapter=None)
        assert novel.current_chapter == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_invalid_current_chapter_values(self, invalid_current_chapter_case):
        """Test invalid current_chapter values raise ValidationError."""
        input_value, expected_error = invalid_current_chapter_case
        with pytest.raises(ValidationError) as exc_info:
            NovelCreate(title="Test", current_chapter=input_value)
        assert expected_error in str(exc_info.value)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_invalid_current_chapter_types(self, invalid_current_chapter_type_case):
        """Test invalid current_chapter types raise TypeError."""
        input_value, expected_exception = invalid_current_chapter_type_case
        with pytest.raises(expected_exception):
            NovelCreate(title="Test", current_chapter=input_value)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_current_chapter_large_values(self):
        """Test current_chapter with very large values."""
        large_chapter = 999999
        novel = NovelCreate(title="Test", current_chapter=large_chapter)
        assert novel.current_chapter == large_chapter

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_current_chapter_zero_explicit(self):
        """Test explicit zero current_chapter."""
        novel = NovelCreate(title="Test", current_chapter=0)
        assert novel.current_chapter == 0


class TestNovelCreateLastReadDateValidator:
    """Test the last_read_date field validator."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_valid_date_objects(self):
        """Test valid date objects."""
        test_date = date(2024, 3, 15)
        novel = NovelCreate(title="Test", last_read_date=test_date)
        assert novel.last_read_date == test_date

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_date_none(self):
        """Test None date is valid."""
        novel = NovelCreate(title="Test", last_read_date=None)
        assert novel.last_read_date is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_date_today(self):
        """Test today's date."""
        today = date.today()
        novel = NovelCreate(title="Test", last_read_date=today)
        assert novel.last_read_date == today

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_date_future(self):
        """Test future dates are allowed."""
        future_date = date(2030, 12, 31)
        novel = NovelCreate(title="Test", last_read_date=future_date)
        assert novel.last_read_date == future_date

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_date_past(self):
        """Test past dates are allowed."""
        past_date = date(2000, 1, 1)
        novel = NovelCreate(title="Test", last_read_date=past_date)
        assert novel.last_read_date == past_date


class TestNovelCreateNotesField:
    """Test the notes field (least restricted field)."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_none(self):
        """Test None notes."""
        novel = NovelCreate(title="Test", notes=None)
        assert novel.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_empty_string(self):
        """Test empty string notes."""
        novel = NovelCreate(title="Test", notes="")
        assert novel.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_normal_string(self):
        """Test normal string notes."""
        notes = "These are some notes about the novel."
        novel = NovelCreate(title="Test", notes=notes)
        assert novel.notes == notes

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_multiline(self):
        """Test multiline notes."""
        notes = "Line 1\nLine 2\nLine 3"
        novel = NovelCreate(title="Test", notes=notes)
        assert novel.notes == notes

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_special_characters(self):
        """Test notes with special characters."""
        notes = "Notes with special: !@#$%^&*()_+-=[]{}|;':\",./<>?"
        novel = NovelCreate(title="Test", notes=notes)
        assert novel.notes == notes

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_unicode(self):
        """Test notes with Unicode characters."""
        notes = "Notes with Unicode: ñáéíóú 中文 🚀"
        novel = NovelCreate(title="Test", notes=notes)
        assert novel.notes == notes

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_notes_very_long(self):
        """Test very long notes."""
        long_notes = "A" * 10000
        novel = NovelCreate(title="Test", notes=long_notes)
        assert novel.notes == long_notes


class TestNovelSortFieldEnum:
    """Test the NovelSortField enum."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_all_enum_values_accessible(self, all_sort_fields):
        """Test all enum values are accessible."""
        for field in all_sort_fields:
            assert isinstance(field, NovelSortField)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_enum_string_values(self):
        """Test enum string values."""
        assert NovelSortField.TITLE == "title"
        assert NovelSortField.SITE == "site"
        assert NovelSortField.URL == "url"
        assert NovelSortField.CURRENT_CHAPTER == "current_chapter"
        assert NovelSortField.LAST_READ_DATE == "last_read_date"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_enum_membership(self):
        """Test enum membership checks."""
        assert "title" in NovelSortField
        assert "invalid_field" not in NovelSortField

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_enum_iteration(self):
        """Test enum iteration."""
        fields = list(NovelSortField)
        assert len(fields) == 5
        assert NovelSortField.TITLE in fields
        assert NovelSortField.SITE in fields


class TestNovelCreateIntegration:
    """Integration tests for NovelCreate with multiple fields."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_minimal_valid_creation(self, minimal_novel_create):
        """Test creation with minimal valid data."""
        assert minimal_novel_create.title == "Minimal Novel"
        assert minimal_novel_create.site is None
        assert minimal_novel_create.url is None
        assert minimal_novel_create.current_chapter == 0
        assert minimal_novel_create.last_read_date is None
        assert minimal_novel_create.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_complete_valid_creation(self, complete_novel_create):
        """Test creation with all fields populated."""
        assert complete_novel_create.title == "Complete Test Novel"
        assert complete_novel_create.site == "Test Site"
        assert str(complete_novel_create.url) == "https://example.com/novel"
        assert complete_novel_create.current_chapter == 42
        assert complete_novel_create.last_read_date == date(2024, 3, 15)
        assert (
            complete_novel_create.notes
            == "This is a test novel with all fields filled."
        )

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_whitespace_handling(self, novel_create_with_whitespace):
        """Test that whitespace is properly stripped."""
        assert novel_create_with_whitespace.title == "Spaced Title"
        assert novel_create_with_whitespace.site == "Spaced Site"
        assert novel_create_with_whitespace.notes == "Spaced Notes"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_edge_cases(self, novel_create_with_edge_cases):
        """Test edge case values."""
        assert (
            novel_create_with_edge_cases.title == "Title with Special Chars: !@#$%^&*()"
        )
        assert novel_create_with_edge_cases.site == "Site with Unicode: ñáéíóú 中文 🚀"
        assert str(novel_create_with_edge_cases.url) == "http://localhost:8000/novel"
        assert novel_create_with_edge_cases.current_chapter == 0
        assert novel_create_with_edge_cases.last_read_date == date.today()
        assert novel_create_with_edge_cases.notes is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_model_dump(self, complete_novel_create, expected_complete_novel_dict):
        """Test model_dump produces expected dictionary."""
        dumped = complete_novel_create.model_dump()
        dumped["url"] = (
            str(dumped["url"]) if dumped.get("url") else None
        )  # Convert URL to string for comparison
        assert dumped == expected_complete_novel_dict

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_json_serialization(self, complete_novel_create):
        """Test JSON serialization works."""
        json_str = complete_novel_create.model_dump_json()
        assert isinstance(json_str, str)
        assert "Complete Test Novel" in json_str
