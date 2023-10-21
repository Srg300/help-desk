from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, int64, int64_pk, str_256


class Division(Base):
    """Подразделение"""

    __tablename__ = "division"

    id: Mapped[int64_pk] = mapped_column()
    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()

    parent_id: Mapped[int64_pk | None] = mapped_column(ForeignKey("division.id"))

    parent: Mapped[Division | None] = relationship(
        back_populates="children",
        remote_side=id,
        lazy="raise",
    )
