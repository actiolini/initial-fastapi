"""add content column to posts table

Revision ID: 796d306a1ffc
Revises: b43315a882f2
Create Date: 2025-11-12 10:17:28.539239

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '796d306a1ffc'
down_revision: Union[str, None] = 'b43315a882f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

