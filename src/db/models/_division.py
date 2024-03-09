from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, str_256

if TYPE_CHECKING:
    from ._user import User


class Division(Base):
    """Подразделение"""

    __tablename__ = "division"

    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()

    parent_id: Mapped[int | None] = mapped_column(ForeignKey("division.id"))

    parent: Mapped[Division | None] = relationship(
        back_populates="children",
        remote_side="Division.id",
    )
    children: Mapped[list[Division]] = relationship(back_populates="parent")
