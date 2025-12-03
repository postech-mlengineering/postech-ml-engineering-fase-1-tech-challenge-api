"""adição da coluna image_url na tabela books

Revision ID: 12ecb55a18a8
Revises: 3f1c12f2395d
Create Date: 2025-12-02 22:14:47.080272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '12ecb55a18a8'
down_revision: Union[str, Sequence[str], None] = '3f1c12f2395d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
