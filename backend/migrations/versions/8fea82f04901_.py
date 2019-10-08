"""empty message

Revision ID: 8fea82f04901
Revises: 
Create Date: 2019-10-08 16:38:54.751431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fea82f04901'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('mac_address', sa.String(length=50), nullable=True),
    sa.Column('location', sa.String(length=50), nullable=True),
    sa.Column('token', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('devices')
    # ### end Alembic commands ###
