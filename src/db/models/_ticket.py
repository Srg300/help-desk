from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, str_256, text
from db.constants.ticket import TicketStatus
from db.models import Group

if TYPE_CHECKING:
    from db.models import User, Message


class Ticket(Base):
    """Тикеты"""

    __tablename__ = "ticket"

    name: Mapped[str_256] = mapped_column(unique=True)
    description: Mapped[text]
    status: Mapped[TicketStatus] = mapped_column(
        Enum(TicketStatus, native_enum=False, length=20),
    )
    author_id: Mapped[int64] = mapped_column(ForeignKey("user.id"))
    # author: Mapped[User] = relationship()

    group_id: Mapped[int64 | None] = mapped_column(ForeignKey("group.id"))
    # group: Mapped[Group] = relationship(back_populates="ticket")

    worker_id: Mapped[int64] = mapped_column(ForeignKey("user.id"))
    # worker: Mapped[User] = relationship()

    parent_id: Mapped[int64 | None] = mapped_column(ForeignKey("ticket.id"))
    parent: Mapped[Ticket | None] = relationship(
        back_populates="children",
        remote_side="Ticket.id",
    )
    children: Mapped[list[Ticket]] = relationship(back_populates="parent")
    # messages: Mapped[list[Message]] = relationship(back_populates="ticket")
