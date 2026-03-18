import logging

from novel_tracker.domain.models.novel import Novel, row_to_novel
from novel_tracker.infrastructure.database.queries import execute_query

logger = logging.getLogger(__name__)


class NovelRepository:
    """
    Repository for managing Novel entities in the database.
    Provides methods for CRUD operations and abstracts away database interactions.
    """

    def __init__(self, connection=None):
        self.connection = connection

    def add_novel(self, novel: Novel):
        execute_query(
            """
            INSERT INTO novels (title, site, url, current_chapter, last_read_date, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            params=(
                novel.title,
                novel.site,
                novel.url,
                novel.current_chapter,
                novel.last_read_date,
                novel.notes,
            ),
            fetch_one=False,
            fetch_all=False,
        )

    def list_novels(self):
        rows = execute_query(
            "SELECT title, site, url, current_chapter, last_read_date, notes FROM novels",
            fetch_all=True,
        )
        return [row_to_novel(row) for row in rows]

    def get_novel_by_title(self, title: str) -> Novel:
        row = execute_query(
            "SELECT title, site, url, current_chapter, last_read_date, notes "
            "FROM novels WHERE title = ?",
            params=(title,),
            fetch_one=True,
        )
        if row:
            return row_to_novel(row)
        return None

    def update_novel(self, novel_data: dict):
        fields = []
        values = []
        for key, value in novel_data.items():
            if key != "title":
                fields.append(f"{key} = ?")
                values.append(value)
        values.append(novel_data["title"])  # Add title for WHERE clause
        execute_query(
            f"""
            UPDATE novels
            SET {", ".join(fields)}
            WHERE title = ?
        """,
            params=values,
            fetch_one=False,
            fetch_all=False,
        )

    def delete_novel(self, title: str):
        execute_query("DELETE FROM novels WHERE title = ?", params=(title,))
