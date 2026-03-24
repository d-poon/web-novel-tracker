import logging

from novel_tracker.infrastructure.database.connection import get_connection

logger = logging.getLogger(__name__)


def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS novels (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL COLLATE NOCASE,
                site TEXT,
                url TEXT,
                current_chapter INTEGER,
                last_read_date TEXT,
                notes TEXT
            )
        """
        )


def execute_query(
    query: str,
    params: tuple | None = None,
    fetch_one: bool = False,
    fetch_all: bool = False,
    mapper=None,
):
    logger.debug("Executing query: %s with params: %s", query, params)

    with get_connection() as conn:
        cursor = conn.cursor()
        result = None

        cursor.execute(query, params or ())

        if fetch_one:
            row = cursor.fetchone()
            result = mapper(row) if (row and mapper) else row

        elif fetch_all:
            rows = cursor.fetchall()
            result = [mapper(r) for r in rows] if (rows and mapper) else rows

        return result
