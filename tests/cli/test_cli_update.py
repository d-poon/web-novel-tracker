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
def test_update_novel_existing(runner, temp_db):
    """Test updating an existing novel."""
    # Add initial novel
    runner.invoke(app, ["novel", "add", "Update Test", "--current-chapter", "1"])

    # Update it
    result = runner.invoke(
        app,
        [
            "novel",
            "update",
            "Update Test",
            "--current-chapter",
            "10",
            "--notes",
            "Updated notes",
        ],
    )
    assert result.exit_code == 0
    assert "Novel 'Update Test' updated successfully." in result.output

    # Verify update
    get_result = runner.invoke(app, ["novel", "get", "Update Test"])
    assert "Chapter 10" in get_result.output
    assert "Updated notes" in get_result.output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_update_novel_nonexistent(runner, temp_db):
    """Test updating a novel that doesn't exist."""
    result = runner.invoke(
        app, ["novel", "update", "Nonexistent", "--current-chapter", "5"]
    )
    assert result.exit_code == 1
    assert "not found" in result.output.lower()


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_update_novel_partial(runner, temp_db):
    """Test updating only some fields of a novel."""
    # Add novel with multiple fields
    runner.invoke(
        app,
        [
            "novel",
            "add",
            "Partial Update",
            "--site",
            "Original Site",
            "--current-chapter",
            "5",
            "--notes",
            "Original notes",
        ],
    )

    # Update only chapter
    result = runner.invoke(
        app, ["novel", "update", "Partial Update", "--current-chapter", "20"]
    )
    assert result.exit_code == 0

    # Check that other fields remain
    get_result = runner.invoke(app, ["novel", "get", "Partial Update"])
    assert "Original Site" in get_result.output
    assert "Chapter 20" in get_result.output
    assert "Original notes" in get_result.output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_update_novel_clear_fields(runner, temp_db):
    """Test updating a novel to clear optional fields."""
    # Add novel with notes
    runner.invoke(app, ["novel", "add", "Clear Test", "--notes", "Some notes"])

    # Update with empty notes (should clear)
    result = runner.invoke(app, ["novel", "update", "Clear Test", "--notes", ""])
    assert result.exit_code == 0

    # Verify notes are cleared
    get_result = runner.invoke(app, ["novel", "get", "Clear Test"])
    assert "Some notes" not in get_result.output


@pytest.mark.generated_by_ai
@pytest.mark.human_reviewed
def test_update_novel_invalid_data(runner, temp_db):
    """Test updating with invalid data."""
    runner.invoke(app, ["novel", "add", "Invalid Update"])

    result = runner.invoke(
        app, ["novel", "update", "Invalid Update", "--current-chapter", "-1"]
    )
    assert result.exit_code == 1
    assert (
        "chapter" in result.output.lower() and "non-negative" in result.output.lower()
    )
