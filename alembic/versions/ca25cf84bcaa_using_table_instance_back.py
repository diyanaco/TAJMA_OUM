"""Using table instance back

Revision ID: ca25cf84bcaa
Revises: 628620f3d891
Create Date: 2022-10-08 15:26:06.348278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca25cf84bcaa'
down_revision = '628620f3d891'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('psy_user_role_link', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('psy_user_role_link', sa.Column('id', mysql.VARCHAR(length=50), nullable=False))
    # ### end Alembic commands ###