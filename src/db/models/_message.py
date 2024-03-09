from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, text

if TYPE_CHECKING:
    from db.models import Task, Ticket, User


class Message(Base):
    """Сообщения"""

    __tablename__ = "message"

    body: Mapped[text]

    author_id: Mapped[int64] = mapped_column(ForeignKey("user.id"))
    task_id: Mapped[int64 | None] = mapped_column(ForeignKey("task.id"))
    ticket_id: Mapped[int64 | None] = mapped_column(ForeignKey("ticket.id"))

    author: Mapped[User] = relationship(back_populates="messages")

    ticket: Mapped[Ticket | None] = relationship()
    task: Mapped[Task | None] = relationship()
