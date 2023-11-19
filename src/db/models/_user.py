from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, created_datetime, int64_pk, str_256, updated_datetime
from db.models import Division


class User(Base):
    __tablename__ = "user"

    id: Mapped[int64_pk]
    username: Mapped[str_256] = mapped_column(unique=True)
    full_name: Mapped[str_256]

    email: Mapped[str_256] = mapped_column(unique=True)
    phone: Mapped[str_256 | None] = mapped_column(unique=True)
    telegram_id: Mapped[str_256 | None] = mapped_column(unique=True)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_superuser: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[created_datetime]
    updated_at: Mapped[updated_datetime]

    division_id: Mapped[int | None] = mapped_column(ForeignKey("division.id"))
    group_id: Mapped[int | None] = mapped_column(ForeignKey("group.id"))
    role_id: Mapped[int | None] = mapped_column(ForeignKey("role.id"))

    division: Mapped[Division | None] = relationship(back_populates="user")
