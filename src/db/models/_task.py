from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base, int64, str_256, text
from db.constants.task import TaskStatus

if TYPE_CHECKING:
    from db.models._user import Message, User


class Task(Base):
    """Задачи"""

    __tablename__ = "task"

    name: Mapped[str_256] = mapped_column(unique=True)
    description: Mapped[text]
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, native_enum=False, length=20),
    )

    author_id: Mapped[int64] = mapped_column(ForeignKey("user.id"))
    worker_id: Mapped[int64] = mapped_column(ForeignKey("user.id"))

    author: Mapped[User] = relationship(
        back_populates="author_tasks",
        primaryjoin="foreign(Task.author_id)==User.id",
    )
    worker: Mapped[User] = relationship(
        back_populates="worker_tasks",
        primaryjoin="foreign(Task.worker_id)==User.id",
    )
    messages: Mapped[list[Message]] = relationship(back_populates="task")
