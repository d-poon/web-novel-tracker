from dataclasses import dataclass


@dataclass
class Novel:
    title: str
    site: str | None = None
    url: str | None = None
    current_chapter: int | None = None
    last_read_date: str | None = None
    notes: str | None = None


def row_to_novel(row) -> Novel:
    return Novel(
        title=row["title"],
        site=row["site"],
        url=row["url"],
        current_chapter=row["current_chapter"],
        last_read_date=row["last_read_date"],
        notes=row["notes"],
    )
