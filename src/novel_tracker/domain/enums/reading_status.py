from enum import StrEnum


class ReadingStatus(StrEnum):
    READING = "reading"
    COMPLETED = "completed"
    DROPPED = "dropped"
    PLAN_TO_READ = "plan_to_read"
