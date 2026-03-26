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
def test_list_novels_empty(runner, temp_db):
    """Test listing novels when database is empty."""
    result = runner.invoke(app, ["novel", "list"])
    assert result.exit_code == 0
    assert "TITLE" in result.output  # Header should be present
    assert "SITE" in result.output
    # Should have no rows


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_list_novels_with_data(runner, temp_db):
    """Test listing novels with some data."""
    # Add some novels
    runner.invoke(app, ["novel", "add", "--title", "Novel A", "--site", "Site A"])
    runner.invoke(
        app,
        [
            "novel",
            "add",
            "--title",
            "Novel B",
            "--site",
            "Site B",
            "--current-chapter",
            "10",
        ],
    )

    result = runner.invoke(app, ["novel", "list"])
    assert result.exit_code == 0
    assert "Novel A" in result.output
    assert "Novel B" in result.output
    assert "Site A" in result.output
    assert "Site B" in result.output
    assert "10" in result.output  # Chapter for Novel B


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_list_novels_sort_by_title(runner, temp_db):
    """Test sorting novels by title."""
    # Add novels in reverse order
    runner.invoke(app, ["novel", "add", "--title", "Z Novel"])
    runner.invoke(app, ["novel", "add", "--title", "A Novel"])

    result = runner.invoke(app, ["novel", "list", "--sort-by", "title"])
    assert result.exit_code == 0
    lines = result.output.strip().split("\n")
    # Find the data lines (after header and separator)
    data_lines = [
        line
        for line in lines
        if line.strip() and not line.startswith("-") and "TITLE" not in line
    ]
    assert len(data_lines) >= 2
    # First data line should contain A Novel
    assert "A Novel" in data_lines[0]


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_list_novels_sort_by_chapter(runner, temp_db):
    """Test sorting novels by current chapter (descending)."""
    runner.invoke(
        app, ["novel", "add", "--title", "Low Chapter", "--current-chapter", "1"]
    )
    runner.invoke(
        app, ["novel", "add", "--title", "High Chapter", "--current-chapter", "50"]
    )

    result = runner.invoke(app, ["novel", "list", "--sort-by", "current_chapter"])
    assert result.exit_code == 0
    lines = result.output.strip().split("\n")
    data_lines = [
        line
        for line in lines
        if line.strip() and not line.startswith("-") and "TITLE" not in line
    ]
    assert len(data_lines) >= 2
    # First should be High Chapter (higher number)
    assert "High Chapter" in data_lines[0]


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_list_novels_invalid_sort(runner, temp_db):
    """Test listing with invalid sort field."""
    result = runner.invoke(app, ["novel", "list", "--sort-by", "invalid"])
    assert result.exit_code == 1
    assert "invalid sort field" in result.output.lower()


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_list_novels_ls_alias(runner, temp_db):
    """Test that 'ls' is an alias for 'list'."""
    runner.invoke(app, ["novel", "add", "--title", "Test Novel"])
    result = runner.invoke(app, ["novel", "ls"])
    assert result.exit_code == 0
    assert "Test Novel" in result.output
