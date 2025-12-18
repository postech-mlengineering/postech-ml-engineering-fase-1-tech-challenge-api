"""Renomeando campos de original para inputed

Revision ID: bfc43736777d
Revises: 70e21ca065c1
Create Date: 2025-12-18 22:55:21.976154

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfc43736777d'
down_revision: Union[str, Sequence[str], None] = '70e21ca065c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_column('book_recommendation', 'original_title', 'inputed_book_title')
    op.rename_column('book_recommendation', 'original_book_id', 'inputed_book_id')


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_column('book_recommendation', 'inputed_book_title', 'original_title')
    op.rename_column('book_recommendation', 'inputed_book_id', 'original_book_id')
