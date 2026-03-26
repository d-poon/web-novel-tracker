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
def test_delete_novel_existing(runner, temp_db):
    """Test deleting an existing novel."""
    # Add a novel
    runner.invoke(app, ["novel", "add", "--title", "Delete Test"])

    # Delete it
    result = runner.invoke(app, ["novel", "delete", "Delete Test"])
    assert result.exit_code == 0
    assert "Novel 'Delete Test' deleted successfully." in result.output

    # Verify it's gone
    list_result = runner.invoke(app, ["novel", "list"])
    assert "Delete Test" not in list_result.output


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_delete_novel_nonexistent(runner, temp_db):
    """Test deleting a novel that doesn't exist."""
    result = runner.invoke(app, ["novel", "delete", "Nonexistent Novel"])
    assert result.exit_code == 1
    assert "not found" in result.output.lower()


@pytest.mark.is_ai_generated
@pytest.mark.is_human_added
@pytest.mark.is_human_reviewed
def test_delete_novel_case_sensitive(runner, temp_db):
    """Test that delete is case sensitive."""
    runner.invoke(app, ["novel", "add", "--title", "Delete Case"])

    result = runner.invoke(app, ["novel", "delete", "delete case"])  # lowercase
    assert result.exit_code == 0  # Should find
    assert "not found" in result.output.lower()

    # Verify it is gone
    list_result = runner.invoke(app, ["novel", "list"])
    assert "Delete Case" not in list_result.output


@pytest.mark.is_ai_generated
@pytest.mark.is_human_reviewed
def test_delete_novel_after_update(runner, temp_db):
    """Test deleting a novel that was previously updated."""
    runner.invoke(app, ["novel", "add", "--title", "Update Then Delete"])
    runner.invoke(
        app,
        ["novel", "update", "--title", "Update Then Delete", "--current-chapter", "10"],
    )

    result = runner.invoke(app, ["novel", "delete", "Update Then Delete"])
    assert result.exit_code == 0

    # Verify deleted
    list_result = runner.invoke(app, ["novel", "list"])
    assert "Update Then Delete" not in list_result.output
