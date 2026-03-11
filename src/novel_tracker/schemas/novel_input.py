from datetime import date

from pydantic import BaseModel, HttpUrl


class NovelCreate(BaseModel):
    title: str
    site: str | None
    url: HttpUrl | None
    current_chapter: int
    last_read_date: date | None
    notes: str | None
