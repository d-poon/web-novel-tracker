import pytest
from typer.testing import CliRunner

from novel_tracker.cli.app import app


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


runner.is_ai_generated = True
runner.is_human_added = False
runner.is_human_reviewed = True


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_add_novel_minimal(runner, temp_db):
    """Test adding a novel with only required title."""
    result = runner.invoke(app, ["novel", "add", "Test Novel"])
    assert result.exit_code == 0
    assert "Novel 'Test Novel' added successfully." in result.output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_add_novel_complete(runner, temp_db):
    """Test adding a novel with all fields."""
    result = runner.invoke(
        app,
        [
            "novel",
            "add",
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


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_add_novel_duplicate_title(runner, temp_db):
    """Test adding a novel with a title that already exists."""
    # First add
    runner.invoke(app, ["novel", "add", "Duplicate Novel"])
    # Try to add again
    result = runner.invoke(app, ["novel", "add", "Duplicate Novel"])
    assert result.exit_code == 1  # Should fail
    output = result.output.lower()
    assert "already exists" in output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_add_novel_invalid_title(runner, temp_db):
    """Test adding a novel with invalid title (empty)."""
    result = runner.invoke(app, ["novel", "add", ""])
    assert result.exit_code == 1
    output = result.output.lower()
    assert "title" in output and "required" in output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_add_novel_negative_chapter(runner, temp_db):
    """Test adding a novel with negative chapter number."""
    result = runner.invoke(
        app, ["novel", "add", "Negative Chapter", "--current-chapter", "-1"]
    )
    assert result.exit_code == 1
    output = result.output.lower()
    assert "chapter" in output and "non-negative" in output
