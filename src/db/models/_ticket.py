from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, int64_pk, str_256, text


class Ticket(Base):
    """Тикеты"""

    __tablename__ = "ticket"

    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()
    description: Mapped[text]

    group_id: Mapped[int | None] = mapped_column(ForeignKey("group.id"))

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("ticket.id"))
    parent: Mapped[Ticket | None] = relationship(
        back_populates="children",
        remote_side="Ticket.id",
    )
    children: Mapped[list[Ticket]] = relationship(back_populates="parent")
