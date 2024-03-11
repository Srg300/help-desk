from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, str_256
from db.models._group import user_group
from db.models._task import Task
from db.models._ticket import Group, Ticket

if TYPE_CHECKING:
    from db.models import Message


class User(Base):
    __tablename__ = "user"

    username: Mapped[str_256] = mapped_column(unique=True)
    hashed_password: Mapped[str]
    email: Mapped[str_256] = mapped_column(unique=True)
    full_name: Mapped[str_256 | None]
    weight: Mapped[int | None] = mapped_column()

    phone: Mapped[str_256 | None] = mapped_column(unique=True)
    telegram_id: Mapped[str_256 | None] = mapped_column(unique=True)
    last_login: Mapped[datetime | None]

    is_active: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_verified: Mapped[bool] = mapped_column(default=False)

    group_leader: Mapped[list[Group]] = relationship(back_populates="leader")
    messages: Mapped[list["Message"]] = relationship(back_populates="author")
    author_tasks: Mapped[list[Task]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Task.author_id == User.id),
    )
    worker_tasks: Mapped[list[Task]] = relationship(
        back_populates="worker",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Task.worker_id == User.id),
    )
    author_tickets: Mapped[list[Ticket]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Ticket.author_id == User.id),
    )
    worker_tickets: Mapped[list[Ticket]] = relationship(
        back_populates="worker",
        cascade="all, delete-orphan",
        primaryjoin=lambda: (Ticket.worker_id == User.id),
    )
    group: Mapped[list[Group]] = relationship(
        secondary=user_group,
        back_populates="users",
    )
