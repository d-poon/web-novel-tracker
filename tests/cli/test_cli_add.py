import pytest
from typer.testing import CliRunner

from novel_tracker.cli.app import app


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


runner.is_ai_generated = True
runner.is_human_added = False
runner.is_human_reviewed = True


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_add_novel_minimal(runner, temp_db):
    """Test adding a novel with only required title."""
    result = runner.invoke(app, ["novel", "add", "--title", "Test Novel"])
    assert result.exit_code == 0
    assert "Novel 'Test Novel' added successfully." in result.output


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_add_novel_complete(runner, temp_db):
    """Test adding a novel with all fields."""
    result = runner.invoke(
        app,
        [
            "novel",
            "add",
            "--title",
            "Complete Novel",
            "--site",
            "Test Site",
            "--url",
            "https://example.com/novel",
            "--current-chapter",
            "5",
            "--last-read-date",
            "2024-03-15",
            "--notes",
            "Test notes",
        ],
    )
    assert result.exit_code == 0
    assert "Novel 'Complete Novel' added successfully." in result.output


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_add_novel_duplicate_title(runner, temp_db):
    """Test adding a novel with a title that already exists."""
    # First add
    runner.invoke(app, ["novel", "add", "--title", "Duplicate Novel"])
    # Try to add again
    result = runner.invoke(app, ["novel", "add", "--title", "Duplicate Novel"])
    assert result.exit_code == 1  # Should fail
    assert "already exists" in result.output.lower()


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_add_novel_invalid_title(runner, temp_db):
    """Test adding a novel with invalid title (empty)."""
    result = runner.invoke(app, ["novel", "add", "--title", ""])
    assert result.exit_code == 1
    assert "title" in result.output.lower() and "required" in result.output.lower()


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_add_novel_negative_chapter(runner, temp_db):
    """Test adding a novel with negative chapter number."""
    result = runner.invoke(
        app, ["novel", "add", "--title", "Negative Chapter", "--current-chapter", "-1"]
    )
    assert result.exit_code == 1
    assert (
        "chapter" in result.output.lower() and "non-negative" in result.output.lower()
    )
