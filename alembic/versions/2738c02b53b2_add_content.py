"""add content

Revision ID: 2738c02b53b2
Revises: 5e966cec7e82
Create Date: 2024-05-20 15:44:45.459441

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2738c02b53b2'
down_revision: Union[str, None] = '5e966cec7e82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass