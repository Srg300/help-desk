from __future__ import annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, int64_pk, str_256


class Role(Base):
    """Роли пользователя"""

    __tablename__ = "role"

    id: Mapped[int64_pk]
    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int64] = mapped_column()
