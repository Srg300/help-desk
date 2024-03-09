from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Column, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, str_256

if TYPE_CHECKING:
    from db.models import User, Ticket


user_group = Table(
    "user_group",
    Base.metadata,
    Column(
        "group_id",
        ForeignKey("group.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "user_id",
        ForeignKey("user.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Group(Base):
    """Группы пользователя"""

    __tablename__ = "group"

    name: Mapped[str_256] = mapped_column(unique=True)

    leader_id: Mapped[int64 | None] = mapped_column(ForeignKey("user.id"))

    leader: Mapped[User] = relationship(
        back_populates="group",
        foreign_keys=[leader_id]
    )
    tickets: Mapped[list[Ticket]] = relationship(back_populates="group")
    users: Mapped[list[User]] = relationship(secondary=user_group)
