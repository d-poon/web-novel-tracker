from enum import Enum


class MediaType(str, Enum):  # noqa: B014
    NOVEL = "novel"
    MANGA = "manga"
    ANIME = "anime"
    MOVIE = "movie"
    TV = "tv"
