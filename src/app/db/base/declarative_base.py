import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, MetaData
from sqlalchemy.orm import DeclarativeBase, registry

meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    },
)


class Base(DeclarativeBase):
    metadata = meta
    registry = registry(
        type_annotation_map={
            enum.Enum: Enum(native_enum=False),
            datetime: DateTime(timezone=True),
        },
    )
