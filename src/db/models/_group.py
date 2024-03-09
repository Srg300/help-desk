from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, str_256

if TYPE_CHECKING:
    from db.models import User


class Group(Base):
    """Группы пользователя"""

    __tablename__ = "group"

    name: Mapped[str_256] = mapped_column(unique=True)

    leader_id: Mapped[int64 | None] = mapped_column(ForeignKey("user.id"))
