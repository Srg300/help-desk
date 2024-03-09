import enum


class TicketStatus(str, enum.Enum):
    new = "new"
    in_work = "in_work"
    closed = "closed"
