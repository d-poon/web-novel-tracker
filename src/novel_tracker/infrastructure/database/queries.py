import logging

from novel_tracker.infrastructure.database.connection import get_connection

logger = logging.getLogger(__name__)


def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS novels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            site TEXT NOT NULL,
            url TEXT NOT NULL,
            current_chapter INTEGER NOT NULL,
            last_read_date TEXT,
            notes TEXT
        )
    """
    )
    conn.commit()
    conn.close()


def execute_query(
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = False,
    mapper=None,
):
    logger.debug("Executing query: %s with params: %s", query, params)

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    result = None
    if fetch_one:
        row = cursor.fetchone()
        result = mapper(row) if (row and mapper) else row
    elif fetch_all:
        rows = cursor.fetchall()
        result = [mapper(r) for r in rows] if (rows and mapper) else rows
    conn.commit()
    conn.close()
    return result
