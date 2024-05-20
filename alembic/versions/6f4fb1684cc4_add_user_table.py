"""add user table

Revision ID: 6f4fb1684cc4
Revises: 2738c02b53b2
Create Date: 2024-05-20 15:49:17.216981

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f4fb1684cc4'
down_revision: Union[str, None] = '2738c02b53b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False),
    sa.Column('email',sa.String(),nullable=False),
    sa.Column('hashed_password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True) ,server_default=sa.text('now()'),nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    pass
def downgrade() -> None:
    op.drop_table('users')
    pass
