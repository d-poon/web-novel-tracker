"""
Integration tests for the database layer.
Tests database connection, initialization, and query execution.
"""

import sqlite3

import pytest

from novel_tracker.infrastructure.database.connection import get_connection
from novel_tracker.infrastructure.database.queries import execute_query, initialize_db


class TestDatabaseConnection:
    """Tests for database connection and setup."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_get_connection_returns_valid_connection(self, temp_db):
        """Test that get_connection returns a valid SQLite connection."""
        conn = get_connection()
        assert isinstance(conn, sqlite3.Connection)
        conn.close()

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_connection_has_row_factory(self, temp_db):
        """Test that connection has Row factory for dict-like access."""
        conn = get_connection()
        assert conn.row_factory == sqlite3.Row
        conn.close()

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_database_file_exists_after_connection(self, temp_db):
        """Test that database file is created after connection attempt."""
        conn = get_connection()
        assert temp_db.exists()
        conn.close()


class TestDatabaseInitialization:
    """Tests for database schema initialization."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_initialize_db_creates_table(self, empty_db, db_connection):
        """Test that initialize_db creates the novels table."""
        cursor = db_connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='novels'"
        )
        table = cursor.fetchone()
        assert table is not None
        assert table[0] == "novels"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_novels_table_has_correct_columns(self, empty_db, db_connection):
        """Test that novels table has all required columns."""
        cursor = db_connection.cursor()
        cursor.execute("PRAGMA table_info(novels)")
        columns = cursor.fetchall()

        column_names = [col[1] for col in columns]
        expected_columns = [
            "id",
            "title",
            "site",
            "url",
            "current_chapter",
            "last_read_date",
            "notes",
        ]

        assert column_names == expected_columns

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_id_column_is_primary_key_autoincrement(self, empty_db, db_connection):
        """Test that id column is configured correctly."""
        cursor = db_connection.cursor()
        cursor.execute("PRAGMA table_info(novels)")
        columns = {col[1]: col for col in cursor.fetchall()}

        id_col = columns["id"]
        # Column definition: (cid, name, type, notnull, dflt_value, pk)
        assert id_col[5] == 1  # pk flag should be 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_initialize_db_idempotent(self, empty_db, db_connection):
        """Test that calling initialize_db multiple times is safe."""
        # First initialization already done by fixture
        # Call again
        initialize_db()

        # Table should still exist and work
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO novels (title, site, url, current_chapter) "
            "VALUES (?, ?, ?, ?)",
            ("Test", "Site", "http://test.com", 1),
        )
        db_connection.commit()

        cursor.execute("SELECT COUNT(*) FROM novels")
        count = cursor.fetchone()[0]
        assert count == 1


class TestQueryExecution:
    """Tests for the execute_query function."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_insert(self, empty_db):
        """Test execute_query with INSERT operation."""
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )
        params = ("Test Novel", "Test Site", "http://test.com", 5)

        result = execute_query(query, params)
        assert result is None  # INSERT doesn't return data

        # Verify insertion by querying
        verify_query = "SELECT COUNT(*) FROM novels"
        rows = execute_query(verify_query, fetch_all=True)
        assert len(rows) == 1
        assert rows[0][0] == 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_fetch_one(self, db_with_sample_novels):
        """Test execute_query with fetch_one=True."""
        query = "SELECT title FROM novels WHERE title = ?"
        result = execute_query(query, ("Minimal Novel",), fetch_one=True)

        assert result is not None
        assert result["title"] == "Minimal Novel"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_fetch_all(self, db_with_sample_novels):
        """Test execute_query with fetch_all=True."""
        query = "SELECT title FROM novels ORDER BY title"
        results = execute_query(query, fetch_all=True)

        assert len(results) >= 1
        assert all(isinstance(row, sqlite3.Row) for row in results)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_with_mapper(self, db_with_sample_novels):
        """Test execute_query with row mapper function."""

        def row_to_title(row):
            return row["title"]

        query = "SELECT title FROM novels WHERE title = ?"
        result = execute_query(
            query, ("Minimal Novel",), fetch_one=True, mapper=row_to_title
        )

        assert result == "Minimal Novel"

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_with_mapper_fetch_all(self, db_with_sample_novels):
        """Test execute_query with mapper for multiple rows."""

        def row_to_title(row):
            return row["title"]

        query = "SELECT title FROM novels ORDER BY title"
        results = execute_query(query, fetch_all=True, mapper=row_to_title)

        assert len(results) >= 1
        assert all(isinstance(title, str) for title in results)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_parameterized_prevents_injection(self, empty_db):
        """Test that parameterized queries prevent SQL injection."""
        # Notice: the novels table requires non-null site/url fields
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )
        params = ("Title'; DROP TABLE novels; --", "Site", "http://test.com", 1)

        # This should insert the string literally, not execute the DROP
        execute_query(query, params)

        # Verify table still exists
        check_query = "SELECT COUNT(*) FROM novels"
        result = execute_query(check_query, fetch_all=True)
        assert len(result) > 0

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_no_params(self, empty_db):
        """Test execute_query without parameters."""
        # Insert without params
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) "
            "VALUES ('Default', 'Default', 'http://default.com', 0)"
        )
        execute_query(query)

        # Verify
        verify_query = "SELECT COUNT(*) FROM novels"
        result = execute_query(verify_query, fetch_all=True)
        assert result[0][0] == 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_fetch_none_when_no_results(self, empty_db):
        """Test execute_query returns None when fetch_one with no results."""
        query = "SELECT * FROM novels WHERE title = ?"
        result = execute_query(query, ("NonExistent",), fetch_one=True)

        assert result is None

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_execute_query_fetch_empty_list_when_no_results(self, empty_db):
        """Test execute_query returns empty list when fetch_all with no results."""
        query = "SELECT * FROM novels WHERE title = ?"
        results = execute_query(query, ("NonExistent",), fetch_all=True)

        assert results == []


class TestConstraintViolations:
    """Tests for handling database constraint violations."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_insert_duplicate_unique_constraint(self, db_with_sample_novels):
        """Test that inserting duplicate titles (if unique constraint exists) fails."""
        # Note: UNIQUE constraint now enforced, this now reflects that a novel with
        # a duplicate title can not be added

        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )
        params = ("Minimal Novel", "Another Site", "http://another.com", 10)

        # Should raise an error with UNIQUE constraint
        with pytest.raises(sqlite3.IntegrityError) as exc_info:
            execute_query(query, params)

        assert "UNIQUE constraint failed" in str(exc_info.value)

        # Verify only one record exists
        verify_query = "SELECT COUNT(*) FROM novels WHERE title = ?"
        count_result = execute_query(verify_query, ("Minimal Novel",), fetch_all=True)
        assert count_result[0][0] == 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_insert_missing_required_field(self, empty_db):
        """Test that inserting without required field fails."""
        query = "INSERT INTO novels (site, url, current_chapter) VALUES (?, ?, ?)"
        params = ("Site", "http://test.com", 5)

        with pytest.raises(sqlite3.IntegrityError):
            execute_query(query, params)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_query_with_invalid_table(self, empty_db):
        """Test that querying non-existent table raises error."""
        query = "SELECT * FROM nonexistent_table"

        with pytest.raises(sqlite3.OperationalError):
            execute_query(query, fetch_all=True)

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_query_with_type_mismatch_in_insert(self, empty_db):
        """Test behavior when inserting wrong data types."""
        # SQLite is flexible with types, but we test the insertion succeeds
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )

        # Pass integer where site (text) expected - SQLite coerces it
        params = ("Test", 12345, "http://test.com", 1)
        result = execute_query(query, params)
        assert result is None

        # Verify it was stored as text
        verify_query = "SELECT site FROM novels WHERE title = ?"
        row = execute_query(verify_query, ("Test",), fetch_one=True)
        assert isinstance(row["site"], str)


class TestDataPersistence:
    """Tests for data persistence across connections."""

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_data_persists_after_connection_close(self, empty_db):
        """Test that data survives connection closure."""
        # Insert data
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )
        execute_query(
            query, ("Persistent Novel", "Persistent Site", "http://persist.com", 99)
        )

        # Open new connection and verify data
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM novels")
        count = cursor.fetchone()[0]
        conn.close()

        assert count == 1

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_multiple_inserts_accumulate(self, empty_db):
        """Test that multiple inserts accumulate in database."""
        query = (
            "INSERT INTO novels (title, site, url, current_chapter) VALUES (?, ?, ?, ?)"
        )

        for i in range(3):
            params = (f"Novel {i}", f"Site {i}", f"http://test{i}.com", i)
            execute_query(query, params)

        # Verify all 3 records exist
        verify_query = "SELECT COUNT(*) FROM novels"
        result = execute_query(verify_query, fetch_all=True)
        assert result[0][0] == 3

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_updates_persist(self, db_with_sample_novels):
        """Test that updates persist in database."""
        # Update a record
        update_query = "UPDATE novels SET current_chapter = ? WHERE title = ?"
        execute_query(update_query, (999, "Minimal Novel"))

        # Verify update persisted with new connection
        verify_query = "SELECT current_chapter FROM novels WHERE title = ?"
        result = execute_query(verify_query, ("Minimal Novel",), fetch_one=True)
        assert result["current_chapter"] == 999

    @pytest.mark.generated_by_ai
    @pytest.mark.human_reviewed
    def test_delete_persists(self, db_with_sample_novels):
        """Test that deletions persist in database."""
        # Delete a record
        delete_query = "DELETE FROM novels WHERE title = ?"
        execute_query(delete_query, ("Minimal Novel",))

        # Verify deletion persisted
        verify_query = "SELECT COUNT(*) FROM novels WHERE title = ?"
        result = execute_query(verify_query, ("Minimal Novel",), fetch_all=True)
        assert result[0][0] == 0
