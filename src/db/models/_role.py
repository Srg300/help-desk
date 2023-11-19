from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base, int64, int64_pk, str_256


class Role(Base):
    """Роли пользователя"""

    __tablename__ = "role"

    id: Mapped[int64_pk]
    name: Mapped[str_256] = mapped_column(unique=True)
    weight: Mapped[int] = mapped_column()
