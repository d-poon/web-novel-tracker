import logging

from novel_tracker.infrastructure.database.connection import get_connection

logger = logging.getLogger(__name__)


def initialize_db():
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")

        # -------------------------
        # USERS
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT UNIQUE,

                password_hash TEXT,
                auth_provider TEXT DEFAULT 'local',

                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )

        # -------------------------
        # MEDIA
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL COLLATE NOCASE,

                media_type TEXT NOT NULL DEFAULT 'novel' CHECK (
                    media_type IN ('novel', 'manga', 'anime', 'movie', 'tv')
                ),

                summary TEXT,
                content_status TEXT,   -- validated in Python

                language TEXT,
                publication_year INTEGER,

                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,

                UNIQUE(title, media_type)
            )
            """
        )

        # -------------------------
        # AUTHORS
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL COLLATE NOCASE UNIQUE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media_authors (
                media_id INTEGER NOT NULL,
                author_id INTEGER NOT NULL,

                PRIMARY KEY (media_id, author_id),

                FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE,
                FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
            )
            """
        )

        # -------------------------
        # GENRES
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL COLLATE NOCASE UNIQUE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media_genres (
                media_id INTEGER NOT NULL,
                genre_id INTEGER NOT NULL,

                PRIMARY KEY (media_id, genre_id),

                FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE,
                FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE CASCADE
            )
            """
        )

        # -------------------------
        # TAGS
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tags (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL COLLATE NOCASE UNIQUE
            )
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media_tags (
                media_id INTEGER NOT NULL,
                tag_id INTEGER NOT NULL,

                PRIMARY KEY (media_id, tag_id),

                FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE,
                FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
            )
            """
        )

        # -------------------------
        # PROGRESS
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                media_id INTEGER NOT NULL,

                progress_current INTEGER NOT NULL DEFAULT 0,
                progress_total INTEGER,
                progress_unit TEXT DEFAULT 'chapter',  -- validated in Python

                start_date TEXT,

                rating REAL,
                favorite INTEGER NOT NULL DEFAULT 0,
                status TEXT,  -- validated in Python
                priority INTEGER,
                notes TEXT,

                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,

                UNIQUE(user_id, media_id),

                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE
            )
            """
        )

        # -------------------------
        # SOURCES
        # -------------------------
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS media_sources (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                media_id INTEGER NOT NULL,

                site TEXT,
                url TEXT,
                translator TEXT,
                publisher TEXT,

                created_at TEXT NOT NULL,

                UNIQUE(media_id, url),

                FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE
            )
            """
        )

        # -------------------------
        # INDEXES
        # -------------------------
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_media_title ON media(title);")
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_media_type ON media(media_type);"
        )

        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_progress_user ON progress(user_id);"
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_progress_status ON progress(status);"
        )

        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_media_authors_media_id ON media_authors(media_id);"  # noqa: E501
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_media_genres_media_id ON media_genres(media_id);"  # noqa: E501
        )
        cursor.execute(
            "CREATE INDEX IF NOT EXISTS idx_media_tags_media_id ON media_tags(media_id);"  # noqa: E501
        )

        conn.commit()


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
