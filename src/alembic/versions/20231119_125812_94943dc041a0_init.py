"""init

Revision ID: 94943dc041a0
Revises:
Create Date: 2023-11-19 12:58:12.838096

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "94943dc041a0"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "division",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(
                always=False,
                start=1,
                increment=1,
                minvalue=1,
                maxvalue=9223372036854775807,
                cycle=False,
                cache=1,
            ),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("weight", sa.BigInteger(), nullable=False),
        sa.Column("parent_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["division.id"],
            name=op.f("fk_division_parent_id_division"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_division")),
        sa.UniqueConstraint("name", name=op.f("uq_division_name")),
    )
    op.create_table(
        "group",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(
                always=False,
                start=1,
                increment=1,
                minvalue=1,
                maxvalue=9223372036854775807,
                cycle=False,
                cache=1,
            ),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("weight", sa.BigInteger(), nullable=False),
        sa.Column("parent_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["parent_id"],
            ["group.id"],
            name=op.f("fk_group_parent_id_group"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_group")),
        sa.UniqueConstraint("name", name=op.f("uq_group_name")),
    )
    op.create_table(
        "role",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(
                always=False,
                start=1,
                increment=1,
                minvalue=1,
                maxvalue=9223372036854775807,
                cycle=False,
                cache=1,
            ),
            nullable=False,
        ),
        sa.Column("name", sa.String(length=256), nullable=False),
        sa.Column("weight", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_role")),
        sa.UniqueConstraint("name", name=op.f("uq_role_name")),
    )
    op.create_table(
        "user",
        sa.Column(
            "id",
            sa.BigInteger(),
            sa.Identity(
                always=False,
                start=1,
                increment=1,
                minvalue=1,
                maxvalue=9223372036854775807,
                cycle=False,
                cache=1,
            ),
            nullable=False,
        ),
        sa.Column("username", sa.String(length=256), nullable=False),
        sa.Column("full_name", sa.String(length=256), nullable=False),
        sa.Column("email", sa.String(length=256), nullable=False),
        sa.Column("phone", sa.String(length=256), nullable=True),
        sa.Column("telegram_id", sa.String(length=256), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("is_superuser", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("division_id", sa.BigInteger(), nullable=True),
        sa.Column("group_id", sa.BigInteger(), nullable=True),
        sa.Column("role_id", sa.BigInteger(), nullable=True),
        sa.ForeignKeyConstraint(
            ["division_id"],
            ["division.id"],
            name=op.f("fk_user_division_id_division"),
        ),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["group.id"],
            name=op.f("fk_user_group_id_group"),
        ),
        sa.ForeignKeyConstraint(
            ["role_id"],
            ["role.id"],
            name=op.f("fk_user_role_id_role"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
        sa.UniqueConstraint("email", name=op.f("uq_user_email")),
        sa.UniqueConstraint("phone", name=op.f("uq_user_phone")),
        sa.UniqueConstraint("telegram_id", name=op.f("uq_user_telegram_id")),
        sa.UniqueConstraint("username", name=op.f("uq_user_username")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    op.drop_table("role")
    op.drop_table("group")
    op.drop_table("division")
    # ### end Alembic commands ###
