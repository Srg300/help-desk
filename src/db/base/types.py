import datetime
from typing import Annotated

from sqlalchemy import (
    BigInteger,
    Identity,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import mapped_column

int32_pk = Annotated[
    int,
    mapped_column(
        Integer,
        Identity(always=True),
        primary_key=True,
    ),
]

int64_pk = Annotated[
    int,
    mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True,
        unique=True,
    ),
]

int64 = Annotated[int, mapped_column(BigInteger)]

str_16 = Annotated[str, mapped_column(String(16))]
str_32 = Annotated[str, mapped_column(String(32))]
str_64 = Annotated[str, mapped_column(String(64))]
str_128 = Annotated[str, mapped_column(String(128))]
str_256 = Annotated[str, mapped_column(String(256))]

text = Annotated[str, mapped_column(Text)]

created_datetime = Annotated[
    datetime.datetime,
    mapped_column(insert_default=datetime.datetime.utcnow),
]

updated_datetime = Annotated[
    datetime.datetime,
    mapped_column(
        insert_default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    ),
]
