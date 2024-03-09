from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, int64_pk, str_256


class Group(Base):
    """Группы пользователя"""

    __tablename__ = "group"

    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()

    leader_id: Mapped[int | None] = mapped_column(ForeignKey("user.id"))

    leader: Mapped[Group | None] = relationship(
        back_populates="group",
    )

