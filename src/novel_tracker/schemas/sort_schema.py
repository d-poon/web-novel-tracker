import enum


class NovelSortField(enum.StrEnum):
    title = "title"
    site = "site"
    url = "url"
    current_chapter = "current_chapter"
    last_read_date = "last_read_date"
