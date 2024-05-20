"""add foreign-key to post table

Revision ID: f6d05db2ab0d
Revises: 6f4fb1684cc4
Create Date: 2024-05-20 15:57:15.835452

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6d05db2ab0d'
down_revision: Union[str, None] = '6f4fb1684cc4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(),nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts',referent_table='users',local_cols=['owner_id'], remote_cols = ['id'],ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constrain('post_users_fk',table_name='posts')
    op.drop_columns('posts','owner_id')
    pass
