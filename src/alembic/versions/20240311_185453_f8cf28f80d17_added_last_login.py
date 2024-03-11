"""Added last login

Revision ID: f8cf28f80d17
Revises: ad4160f7eb58
Create Date: 2024-03-11 18:54:53.971892

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f8cf28f80d17"
down_revision: str | None = "ad4160f7eb58"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user",
        sa.Column("last_login", sa.DateTime(timezone=True), nullable=True),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "last_login")
    # ### end Alembic commands ###