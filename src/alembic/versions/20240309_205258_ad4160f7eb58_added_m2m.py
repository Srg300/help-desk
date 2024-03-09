"""Added M2m

Revision ID: ad4160f7eb58
Revises: a94fc749f07e
Create Date: 2024-03-09 20:52:58.577823

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ad4160f7eb58"
down_revision: str | None = "a94fc749f07e"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user_group",
        sa.Column("group_id", sa.BigInteger(), nullable=False),
        sa.Column("user_id", sa.BigInteger(), nullable=False),
        sa.ForeignKeyConstraint(
            ["group_id"],
            ["group.id"],
            name=op.f("fk_user_group_group_id_group"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name=op.f("fk_user_group_user_id_user"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("group_id", "user_id", name=op.f("pk_user_group")),
    )
    op.drop_constraint("fk_message_task_id_ticket", "message", type_="foreignkey")
    op.create_foreign_key(
        op.f("fk_message_task_id_task"),
        "message",
        "task",
        ["task_id"],
        ["id"],
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f("fk_message_task_id_task"), "message", type_="foreignkey")
    op.create_foreign_key(
        "fk_message_task_id_ticket",
        "message",
        "ticket",
        ["task_id"],
        ["id"],
    )
    op.drop_table("user_group")
    # ### end Alembic commands ###
