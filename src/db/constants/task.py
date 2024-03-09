import enum


class TaskStatus(str, enum.Enum):
    new = "new"
    in_work = "in_work"
    waiting = "waiting"
    closed = "closed"
