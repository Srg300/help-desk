from sqlalchemy import ForeignKey
from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, created_datetime, int64, str_256, updated_datetime
from db.models._task import Task
if TYPE_CHECKING:
    from db.models import Task, Message, Ticket

class User(Base):
    __tablename__ = "user"

    username: Mapped[str_256] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    email: Mapped[str_256] = mapped_column(unique=True)
    full_name: Mapped[str_256 | None]
    weight: Mapped[int | None] = mapped_column()

    phone: Mapped[str_256 | None] = mapped_column(unique=True)
    telegram_id: Mapped[str_256 | None] = mapped_column(unique=True)

    is_active: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[created_datetime]
    updated_at: Mapped[updated_datetime]

    messages: Mapped[list["Message"]] = relationship(back_populates="author")

    author_tasks: Mapped[list[Task]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Task.author_id == User.id)
    )
    worker_tasks: Mapped[list[Task]] = relationship(
        back_populates="worker",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Task.worker_id == User.id)
    )
    # tickets: Mapped[list["Ticket"]] = relationship(back_populates="user_tickets")
