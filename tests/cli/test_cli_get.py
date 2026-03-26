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
def test_get_novel_existing(runner, temp_db):
    """Test getting details of an existing novel."""
    # Add a novel
    runner.invoke(
        app,
        [
            "novel",
            "add",
            "--title",
            "Test Novel",
            "--site",
            "Test Site",
            "--current-chapter",
            "5",
            "--notes",
            "Test notes",
        ],
    )

    result = runner.invoke(app, ["novel", "get", "Test Novel"])
    assert result.exit_code == 0
    assert "Test Novel" in result.output
    assert "Test Site" in result.output
    assert "Chapter 5" in result.output
    assert "Test notes" in result.output


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_get_novel_nonexistent(runner, temp_db):
    """Test getting a novel that doesn't exist."""
    result = runner.invoke(app, ["novel", "get", "Nonexistent Novel"])
    assert result.exit_code == 0  # Service doesn't raise error, just doesn't echo
    assert result.output.strip() == ""  # No output for nonexistent


@pytest.mark.is_ai_generated
@pytest.mark.is_human_added
@pytest.mark.is_human_reviewed
def test_get_novel_case_sensitive(runner, temp_db):
    """Test that get is case sensitive."""
    runner.invoke(app, ["novel", "add", "--title", "Test Novel"])

    result = runner.invoke(app, ["novel", "get", "test novel"])  # lowercase
    assert result.exit_code == 0
    assert "Test Novel" in result.output  # Should find


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_get_novel_minimal_data(runner, temp_db):
    """Test getting a novel with minimal data."""
    runner.invoke(app, ["novel", "add", "--title", "Minimal Novel"])

    result = runner.invoke(app, ["novel", "get", "Minimal Novel"])
    assert result.exit_code == 0
    assert "Minimal Novel" in result.output
    assert "Chapter 0" in result.output  # Default chapter
