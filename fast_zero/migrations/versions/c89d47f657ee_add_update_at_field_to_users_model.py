"""add update_at field to users model

Revision ID: c89d47f657ee
Revises: 2e66bc55ffbb
Create Date: 2024-09-20 16:37:26.083509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c89d47f657ee'
down_revision: Union[str, None] = '2e66bc55ffbb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
