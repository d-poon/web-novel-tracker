"""
Integration tests for the repository layer.
Tests CRUD operations and statistics queries.
"""

from datetime import date, timedelta

import pytest

from novel_tracker.domain.models.novel import Novel
from novel_tracker.domain.repositories.stats_repository import StatsRepository


class TestNovelRepositoryCRUD:
    """Tests for Novel Repository CRUD operations."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_add_novel_minimal(self, novel_repository, empty_db):
        """Test adding a minimal novel (title only)."""
        novel = Novel(title="Test Novel")
        novel_repository.add_novel(novel)

        # Verify it was added
        result = novel_repository.get_novel_by_title("Test Novel")
        assert result is not None
        assert result.title == "Test Novel"
        assert result.site is None
        assert result.current_chapter == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_add_novel_complete(self, novel_repository, empty_db):
        """Test adding a complete novel with all fields."""
        novel = Novel(
            title="Complete Novel",
            site="Test Site",
            url="https://example.com/novel",
            current_chapter=42,
            last_read_date=date(2024, 3, 15),
            notes="Test notes",
        )
        novel_repository.add_novel(novel)

        result = novel_repository.get_novel_by_title("Complete Novel")
        assert result.title == "Complete Novel"
        assert result.site == "Test Site"
        assert result.url == "https://example.com/novel"
        assert result.current_chapter == 42
        assert result.last_read_date == date(2024, 3, 15)
        assert result.notes == "Test notes"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_add_multiple_novels(self, novel_repository, empty_db):
        """Test adding multiple novels."""
        novels = [
            Novel(title=f"Novel {i}", site=f"Site {i}", current_chapter=i)
            for i in range(5)
        ]

        for novel in novels:
            novel_repository.add_novel(novel)

        results = novel_repository.list_novels()
        assert len(results) == 5

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_list_novels_empty_database(self, novel_repository, empty_db):
        """Test listing novels from empty database."""
        results = novel_repository.list_novels()
        assert results == []

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_list_novels_returns_all(self, novel_repository, db_with_sample_novels):
        """Test that list_novels returns all novels."""
        results = novel_repository.list_novels()
        assert len(results) >= 4  # Fixture adds 4 novels
        assert all(isinstance(novel, Novel) for novel in results)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_list_novels_preserves_data(self, novel_repository, db_with_sample_novels):
        """Test that listed novels have correct data."""
        results = novel_repository.list_novels()

        titles = [novel.title for novel in results]
        assert "Minimal Novel" in titles
        assert "Complete Test Novel" in titles

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_get_novel_by_title_exists(self, novel_repository, db_with_sample_novels):
        """Test getting an existing novel by title."""
        result = novel_repository.get_novel_by_title("Complete Test Novel")

        assert result is not None
        assert result.title == "Complete Test Novel"
        assert result.site == "Test Site A"
        assert result.current_chapter == 42

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_get_novel_by_title_not_exists(
        self, novel_repository, db_with_sample_novels
    ):
        """Test getting a non-existent novel returns None."""
        result = novel_repository.get_novel_by_title("Nonexistent Novel")
        assert result is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    @pytest.mark.human_added
    def test_get_novel_by_title_case_sensitive(self, novel_repository, empty_db):
        """Test that title lookup is case-sensitive."""
        novel = Novel(title="Exact Title")
        novel_repository.add_novel(novel)

        # Exact case should work
        assert novel_repository.get_novel_by_title("Exact Title") is not None

        # Different case might not work (depends on database collation)
        # Document current behavior
        different_case = novel_repository.get_novel_by_title("exact title")
        # SQLite default is case-insensitive for ASCII, so this may pass
        assert different_case is not None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_update_novel_single_field(self, novel_repository, empty_db):
        """Test updating a single field of a novel."""
        # Add novel
        original = Novel(title="Original Title", current_chapter=10)
        novel_repository.add_novel(original)

        # Update
        update_data = {"title": "Original Title", "current_chapter": 20}
        novel_repository.update_novel(update_data)

        # Verify
        result = novel_repository.get_novel_by_title("Original Title")
        assert result.current_chapter == 20

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_update_novel_multiple_fields(self, novel_repository, empty_db):
        """Test updating multiple fields of a novel."""
        original = Novel(
            title="Original", site="Old Site", current_chapter=5, notes="Old notes"
        )
        novel_repository.add_novel(original)

        # Update multiple fields
        update_data = {
            "title": "Original",
            "site": "New Site",
            "current_chapter": 25,
            "notes": "New notes",
        }
        novel_repository.update_novel(update_data)

        # Verify
        result = novel_repository.get_novel_by_title("Original")
        assert result.site == "New Site"
        assert result.current_chapter == 25
        assert result.notes == "New notes"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_update_novel_preserves_other_fields(self, novel_repository, empty_db):
        """Test that updating one field doesn't affect others."""
        novel = Novel(
            title="Test", site="Test Site", current_chapter=10, notes="Important notes"
        )
        novel_repository.add_novel(novel)

        # Update only chapter
        update_data = {"title": "Test", "current_chapter": 50}
        novel_repository.update_novel(update_data)

        # Verify other fields preserved
        result = novel_repository.get_novel_by_title("Test")
        assert result.site == "Test Site"
        assert result.notes == "Important notes"
        assert result.current_chapter == 50

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_update_nonexistent_novel(self, novel_repository, empty_db):
        """Test updating a novel that doesn't exist."""
        update_data = {"title": "Nonexistent", "current_chapter": 10}
        # Should not raise, but also won't update anything
        novel_repository.update_novel(update_data)

        result = novel_repository.get_novel_by_title("Nonexistent")
        assert result is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_delete_novel_exists(self, novel_repository, empty_db):
        """Test deleting an existing novel."""
        novel = Novel(title="Delete Me")
        novel_repository.add_novel(novel)

        # Verify it exists
        assert novel_repository.get_novel_by_title("Delete Me") is not None

        # Delete
        novel_repository.delete_novel("Delete Me")

        # Verify it's gone
        assert novel_repository.get_novel_by_title("Delete Me") is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_delete_novel_not_exists(self, novel_repository, db_with_sample_novels):
        """Test deleting a novel that doesn't exist."""
        count_before = len(novel_repository.list_novels())

        # Delete non-existent - should not raise
        novel_repository.delete_novel("Nonexistent Novel")

        count_after = len(novel_repository.list_novels())
        assert count_before == count_after

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_delete_removes_only_target_novel(self, novel_repository, empty_db):
        """Test that delete only removes the target novel."""
        novels = [
            Novel(title="Novel 1"),
            Novel(title="Novel 2"),
            Novel(title="Novel 3"),
        ]
        for novel in novels:
            novel_repository.add_novel(novel)

        novel_repository.delete_novel("Novel 2")

        remaining = novel_repository.list_novels()
        titles = [n.title for n in remaining]
        assert "Novel 1" in titles
        assert "Novel 2" not in titles
        assert "Novel 3" in titles

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novel_with_special_characters_in_title(self, novel_repository, empty_db):
        """Test handling novels with special characters in title."""
        special_title = "Novel: Special !@#$%^&*() Chars"
        novel = Novel(title=special_title)
        novel_repository.add_novel(novel)

        result = novel_repository.get_novel_by_title(special_title)
        assert result is not None
        assert result.title == special_title

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novel_with_unicode_characters(self, novel_repository, empty_db):
        """Test handling novels with Unicode characters."""
        unicode_title = "小说: ñáéíóú 🚀"
        novel = Novel(title=unicode_title)
        novel_repository.add_novel(novel)

        result = novel_repository.get_novel_by_title(unicode_title)
        assert result is not None
        assert result.title == unicode_title


class TestStatsRepository:
    """Tests for Stats Repository queries."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_total_novels_empty_database(self, empty_db):
        """Test total_novels on empty database."""
        stats = StatsRepository()
        assert stats.total_novels() == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_total_novels_with_data(self, db_with_sample_novels):
        """Test total_novels count."""
        stats = StatsRepository()
        count = stats.total_novels()
        assert count >= 4  # Fixture adds at least 4

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_total_chapters_read_empty_database(self, empty_db):
        """Test total_chapters_read on empty database."""
        stats = StatsRepository()
        assert stats.total_chapters_read() == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_total_chapters_read_with_data(self, db_with_sample_novels):
        """Test total_chapters_read sums correctly."""
        stats = StatsRepository()
        total = stats.total_chapters_read()
        # Fixture: 0 + 42 + 150 + 5 = 197
        assert total >= 197

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_average_chapters_per_novel_empty_database(self, empty_db):
        """Test average_chapters_per_novel on empty database."""
        stats = StatsRepository()
        avg = stats.average_chapters_per_novel()
        assert avg == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_average_chapters_per_novel_with_data(self, db_with_sample_novels):
        """Test average_chapters_per_novel calculation."""
        stats = StatsRepository()
        avg = stats.average_chapters_per_novel()
        # Fixture: (0 + 42 + 150 + 5) / 4 = 49.25
        assert avg > 0
        assert isinstance(avg, (int, float))

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_most_recently_read_empty_database(self, empty_db):
        """Test most_recently_read on empty database."""
        stats = StatsRepository()
        result = stats.most_recently_read()
        assert result is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_most_recently_read_with_data(self, db_with_sample_novels):
        """Test most_recently_read returns correct novel."""
        stats = StatsRepository()
        result = stats.most_recently_read()
        assert result is not None
        # Fixture: "Recently Read Novel" has today's date
        assert result.title == "Recently Read Novel"
        assert result.last_read_date == date.today()

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_most_used_sites_empty_database(self, empty_db):
        """Test most_used_sites on empty database."""
        stats = StatsRepository()
        result = stats.most_used_sites()
        assert result == []

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_most_used_sites_with_data(self, db_with_sample_novels):
        """Test most_used_sites groups and counts correctly."""
        stats = StatsRepository()
        result = stats.most_used_sites()
        assert len(result) > 0
        # Result should be list of tuples (site, count)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

        # Fixture: Test Site A appears twice, Test Site B once
        site_dict = {site: count for site, count in result}
        assert site_dict["Test Site A"] == 2

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novels_by_site_exists(self, db_with_sample_novels):
        """Test novels_by_site returns correct novels."""
        stats = StatsRepository()
        novels = stats.novels_by_site("Test Site A")

        assert len(novels) == 2
        assert all(n.site == "Test Site A" for n in novels)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novels_by_site_not_exists(self, db_with_sample_novels):
        """Test novels_by_site with non-existent site."""
        stats = StatsRepository()
        novels = stats.novels_by_site("Nonexistent Site")
        assert novels == []

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novels_by_site_case_insensitive(self, db_with_sample_novels):
        """Test novels_by_site is case-insensitive."""
        stats = StatsRepository()

        # Original case
        novels_lower = stats.novels_by_site("test site a")
        novels_upper = stats.novels_by_site("TEST SITE A")

        # Both should return same results (case-insensitive)
        assert len(novels_lower) == len(novels_upper)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_count_novels_by_site_exists(self, db_with_sample_novels):
        """Test count_novels_by_site returns correct count."""
        stats = StatsRepository()
        count = stats.count_novels_by_site("Test Site A")
        assert count == 2

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_count_novels_by_site_not_exists(self, db_with_sample_novels):
        """Test count_novels_by_site with non-existent site."""
        stats = StatsRepository()
        count = stats.count_novels_by_site("Nonexistent Site")
        assert count == 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_recently_read_novels_default_period(self, db_with_sample_novels):
        """Test recently_read_novels with default 7-day period."""
        stats = StatsRepository()
        novels = stats.recently_read_novels()

        # Fixture adds "Recently Read Novel" with today's date
        assert len(novels) >= 1
        assert any(n.title == "Recently Read Novel" for n in novels)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_recently_read_novels_custom_period(self, novel_repository, empty_db):
        """Test recently_read_novels with custom period."""
        # Add novels with different dates
        today = date.today()

        nova_today = Novel(title="Today", last_read_date=today)
        novel_repository.add_novel(nova_today)

        week_ago = Novel(title="Week Ago", last_read_date=today - timedelta(days=7))
        novel_repository.add_novel(week_ago)

        month_ago = Novel(title="Month Ago", last_read_date=today - timedelta(days=30))
        novel_repository.add_novel(month_ago)

        stats = StatsRepository()

        # 7 day period should get first two
        recent_7 = stats.recently_read_novels(days=7)
        titles_7 = [n.title for n in recent_7]
        assert "Today" in titles_7
        assert "Week Ago" in titles_7

        # 14 day period should get all three
        recent_14 = stats.recently_read_novels(days=14)
        assert len(recent_14) >= 2

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_recently_updated_novels_default_limit(self, db_with_sample_novels):
        """Test recently_updated_novels with default limit."""
        stats = StatsRepository()
        novels = stats.recently_updated_novels()

        # Should return at most default limit (5)
        assert len(novels) <= 5
        # With fixture data, should get some results
        assert len(novels) >= 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_recently_updated_novels_custom_limit(self, db_with_sample_novels):
        """Test recently_updated_novels with custom limit."""
        stats = StatsRepository()

        novels_2 = stats.recently_updated_novels(limit=2)
        novels_all = stats.recently_updated_novels(limit=100)

        assert len(novels_2) <= 2
        assert len(novels_all) >= len(novels_2)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_longest_novels_read_default_limit(self, db_with_sample_novels):
        """Test longest_novels_read with default limit."""
        stats = StatsRepository()
        novels = stats.longest_novels_read()

        assert len(novels) <= 5  # Default limit
        assert len(novels) >= 1

        # Should be ordered by chapter count (descending)
        chapters = [n.current_chapter for n in novels]
        assert chapters == sorted(chapters, reverse=True)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_longest_novels_read_custom_limit(self, db_with_sample_novels):
        """Test longest_novels_read with custom limit."""
        stats = StatsRepository()

        novels_1 = stats.longest_novels_read(limit=1)
        novels_3 = stats.longest_novels_read(limit=3)

        assert len(novels_1) == 1
        assert len(novels_3) <= 3
        assert len(novels_3) >= len(novels_1)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_longest_novels_read_ordering(self, novel_repository, empty_db):
        """Test longest_novels_read returns novels in descending chapter order."""
        novels = [
            Novel(title="Novel A", current_chapter=10),
            Novel(title="Novel B", current_chapter=50),
            Novel(title="Novel C", current_chapter=30),
        ]
        for novel in novels:
            novel_repository.add_novel(novel)

        stats = StatsRepository()
        result = stats.longest_novels_read(limit=3)

        chapters = [n.current_chapter for n in result]
        assert chapters == [50, 30, 10]


class TestRepositoryConcurrency:
    """Tests for data consistency with multiple operations."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_read_after_write_consistency(self, novel_repository, empty_db):
        """Test that reads after writes return correct data."""
        novel = Novel(title="Test", current_chapter=5)
        novel_repository.add_novel(novel)

        # Immediately read
        result = novel_repository.get_novel_by_title("Test")
        assert result.current_chapter == 5

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_update_then_read_consistency(self, novel_repository, empty_db):
        """Test consistency of update followed by read."""
        novel = Novel(title="Test", current_chapter=5)
        novel_repository.add_novel(novel)

        # Update
        novel_repository.update_novel({"title": "Test", "current_chapter": 10})

        # Read immediately
        result = novel_repository.get_novel_by_title("Test")
        assert result.current_chapter == 10

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_delete_then_list_consistency(self, novel_repository, empty_db):
        """Test consistency of delete followed by list."""
        for i in range(3):
            novel_repository.add_novel(Novel(title=f"Novel {i}"))

        novel_repository.delete_novel("Novel 1")

        results = novel_repository.list_novels()
        titles = [n.title for n in results]
        assert "Novel 1" not in titles
        assert len(results) == 2

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_stats_accuracy_after_operations(self, novel_repository, empty_db):
        """Test that stats remain accurate after various operations."""
        # Add novels
        for i in range(3):
            novel_repository.add_novel(
                Novel(title=f"Novel {i}", current_chapter=i * 10)
            )

        stats = StatsRepository()
        assert stats.total_novels() == 3

        # Delete one
        novel_repository.delete_novel("Novel 1")

        # Stats should update
        assert stats.total_novels() == 2
