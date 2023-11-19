from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, int64_pk, str_256


class Division(Base):
    """Подразделение"""

    __tablename__ = "division"

    id: Mapped[int64_pk]
    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("division.id"))

    parent: Mapped[Division | None] = relationship(
        back_populates="children",
        remote_side="Division.id",
    )
    children: Mapped[list[Division]] = relationship(back_populates="parent")
    user: Mapped[list["User"]] = relationship(back_populates="division")
