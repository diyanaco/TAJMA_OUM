"""Added salut in user

Revision ID: 127f95bd4920
Revises: 2e71e382970d
Create Date: 2022-12-26 08:57:21.746868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127f95bd4920'
down_revision = '2e71e382970d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('psy_user', sa.Column('salut', sa.String(length=50), nullable=True))
    pass


def downgrade():
    op.drop_column('psy_user', 'salut')
    pass
