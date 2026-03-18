"""
Test fixtures for database setup and teardown.
Provides isolated temporary SQLite databases for integration testing.
"""

import tempfile
from datetime import date
from pathlib import Path

import pytest

from novel_tracker.domain.models.novel import Novel
from novel_tracker.domain.repositories.novel_repository import NovelRepository
from novel_tracker.infrastructure.database.connection import get_connection
from novel_tracker.infrastructure.database.queries import initialize_db


@pytest.fixture(scope="function")
def temp_db(monkeypatch):
    """
    Fixture that provides an isolated temporary SQLite database for testing.

    - Creates a temporary file-based database (not in-memory, to match production)
    - Initializes the schema
    - Patches connection.DB_NAME to use the temp database
    - Cleans up the temporary file after the test

    Yields:
        Path: The path to the temporary database file
    """
    # Create a named temporary file that persists
    temp_file = tempfile.NamedTemporaryFile(suffix=".db", delete=False, dir=None)
    temp_db_path = Path(temp_file.name)
    temp_file.close()

    # Patch the connection module to use our temp database
    import novel_tracker.infrastructure.database.connection as conn_module

    monkeypatch.setattr(conn_module, "DB_NAME", temp_db_path)

    # Initialize the database schema
    initialize_db()

    yield temp_db_path

    # Cleanup: remove the temporary database file
    if temp_db_path.exists():
        temp_db_path.unlink()


# Metadata as booleans
temp_db.is_ai_generated = True
temp_db.is_human_added = False
temp_db.is_human_reviewed = True


@pytest.fixture
def db_connection(temp_db):
    """
    Fixture that provides a connection to the temporary test database.

    Yields:
        sqlite3.Connection: A database connection with Row factory enabled
    """
    conn = get_connection()
    yield conn
    conn.close()


# Metadata as booleans
db_connection.is_ai_generated = True
db_connection.is_human_added = False
db_connection.is_human_reviewed = True


@pytest.fixture
def empty_db(temp_db):
    """
    Fixture that provides an empty initialized test database.

    Yields:
        Path: The path to the empty temporary database
    """
    yield temp_db


# Metadata as booleans
empty_db.is_ai_generated = True
empty_db.is_human_added = False
empty_db.is_human_reviewed = True


@pytest.fixture
def db_with_sample_novels(temp_db):
    """
    Fixture that provides a test database pre-populated with sample novels.

    Populates the database with:
    - Minimal novel (only title)
    - Complete novel (all fields)
    - Multiple novels with various sites

    Yields:
        Path: The path to the populated temporary database
    """
    repo = NovelRepository()

    # Add sample novels
    minimal = Novel(title="Minimal Novel")
    repo.add_novel(minimal)

    complete = Novel(
        title="Complete Test Novel",
        site="Test Site A",
        url="https://example.com/novel",
        current_chapter=42,
        last_read_date=date(2024, 3, 15),
        notes="A complete test novel with all fields",
    )
    repo.add_novel(complete)

    multi_chapter = Novel(
        title="Long Running Series",
        site="Test Site B",
        url="https://example.com/long-series",
        current_chapter=150,
        last_read_date=date(2024, 3, 10),
        notes="A long-running series",
    )
    repo.add_novel(multi_chapter)

    recently_read = Novel(
        title="Recently Read Novel",
        site="Test Site A",
        url="https://example.com/recent",
        current_chapter=5,
        last_read_date=date.today(),
        notes="Read today",
    )
    repo.add_novel(recently_read)

    yield temp_db


# Metadata as booleans
db_with_sample_novels.is_ai_generated = True
db_with_sample_novels.is_human_added = False
db_with_sample_novels.is_human_reviewed = True


@pytest.fixture
def novel_repository(temp_db):
    """
    Fixture that provides a NovelRepository instance connected to the temp database.

    Yields:
        NovelRepository: A repository instance for testing
    """
    yield NovelRepository()


# Metadata as booleans
novel_repository.is_ai_generated = True
novel_repository.is_human_added = False
novel_repository.is_human_reviewed = True
