import pytest
from typer.testing import CliRunner

import novel_tracker.infrastructure.database.connection as conn_module
from novel_tracker.cli.app import app


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


runner.is_ai_generated = True
runner.is_human_added = False
runner.is_human_reviewed = True


@pytest.mark.is_ai_generated
@pytest.mark.is_human_added
@pytest.mark.is_human_reviewed
def test_db_init_success(runner, tmp_path, monkeypatch):
    """Test successful database initialization using a temporary DB file."""
    # Use a temporary database file
    db_path = tmp_path / "test.db"

    # Patch the module-level DB_NAME to use our temp file
    monkeypatch.setattr(conn_module, "DB_NAME", db_path)

    # Invoke the db init command
    result = runner.invoke(app, ["db", "init"])

    # CLI should indicate success
    assert result.exit_code == 0
    assert "initialized" in result.output.lower()

    # Verify database file was created
    assert db_path.exists()

    # Verify we can connect and query
    with conn_module.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert len(tables) > 0  # Should have some tables


@pytest.mark.is_ai_generated
@pytest.mark.is_human_added
@pytest.mark.is_human_reviewed
def test_db_init_idempotent(runner, tmp_path, monkeypatch):
    """Test that db init can be run multiple times safely."""
    # Use a temporary database file
    db_path = tmp_path / "test_idempotent.db"

    # Patch the module-level DB_NAME to use our temp file
    monkeypatch.setattr(conn_module, "DB_NAME", db_path)

    # First init
    result1 = runner.invoke(app, ["db", "init"])
    assert result1.exit_code == 0

    # Second init
    result2 = runner.invoke(app, ["db", "init"])
    assert result2.exit_code == 0  # Should not fail

    # Database should still be functional
    with conn_module.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert len(tables) > 0
