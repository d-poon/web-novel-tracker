from novel_tracker.database.queries import execute_query
from novel_tracker.models.novel import row_to_novel


def total_novels():
    row = execute_query(
        """
        SELECT COUNT(*) as count
        FROM novels
        """,
        fetch_one=True,
    )
    return row["count"] if row else 0


def total_chapters_read():
    row = execute_query(
        """
        SELECT SUM(current_chapter) as total
        FROM novels
        """,
        fetch_one=True,
    )
    return row["total"] if row and row["total"] is not None else 0


def average_chapters_per_novel():
    row = execute_query(
        """
        SELECT AVG(current_chapter) as average
        FROM novels
        """,
        fetch_one=True,
    )
    return row["average"] if row and row["average"] is not None else 0


def most_recently_read():
    row = execute_query(
        """
        SELECT *
        FROM novels
        ORDER BY last_read_date DESC
        LIMIT 1
        """,
        fetch_one=True,
    )
    return row_to_novel(row) if row else None


def most_used_sites():
    rows = execute_query(
        """
        SELECT site, COUNT(*) as count
        FROM novels
        WHERE site IS NOT NULL
        GROUP BY site
        ORDER BY count DESC
        """,
        fetch_all=True,
    )
    return [(row["site"], row["count"]) for row in (rows or [])]


def novels_by_site(site: str):
    rows = execute_query(
        """
        SELECT *
        FROM novels
        WHERE LOWER(site) = LOWER(?)
        """,
        params=(site,),
        fetch_all=True,
    )
    return [row_to_novel(row) for row in (rows or [])]


def count_novels_by_site(site: str):
    row = execute_query(
        """
        SELECT COUNT(*) as count
        FROM novels
        WHERE site = ?
        """,
        params=(site,),
        fetch_one=True,
    )
    return row["count"] if row else 0


def recently_read_novels(days: int = 7):
    rows = execute_query(
        """
        SELECT *
        FROM novels
        WHERE last_read_date >= DATE('now', ?)
        """,
        params=(f"-{days} days",),
        fetch_all=True,
    )
    return [row_to_novel(row) for row in (rows or [])]


def recently_updated_novels(limit: int = 5):
    rows = execute_query(
        """
        SELECT *
        FROM novels
        ORDER BY last_read_date DESC
        LIMIT ?
        """,
        params=(limit,),
        fetch_all=True,
    )
    return [row_to_novel(row) for row in (rows or [])]


def longest_novels_read(limit: int = 5):
    rows = execute_query(
        """
        SELECT *
        FROM novels
        ORDER BY current_chapter DESC
        LIMIT ?
        """,
        params=(limit,),
        fetch_all=True,
    )
    return [row_to_novel(row) for row in (rows or [])]
