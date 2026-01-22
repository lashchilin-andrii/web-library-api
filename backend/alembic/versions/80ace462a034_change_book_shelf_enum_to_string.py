"""change book_shelf enum to string

Revision ID: 80ace462a034
Revises: a8c88279f7aa
Create Date: 2026-01-22 18:53:39.674888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '80ace462a034'
down_revision: Union[str, None] = 'a8c88279f7aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
