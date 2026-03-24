from dataclasses import dataclass
from datetime import date


@dataclass
class Novel:
    title: str
    site: str | None = None
    url: str | None = None
    current_chapter: int | None = 0
    last_read_date: date | None = None
    notes: str | None = None


def row_to_novel(row) -> Novel:
    return Novel(
        title=row["title"],
        site=row["site"],
        url=row["url"],
        current_chapter=row["current_chapter"],
        last_read_date=date.fromisoformat(row["last_read_date"])
        if row["last_read_date"]
        else None,
        notes=row["notes"],
    )
