"""adding seeking talent

Revision ID: c8978ff57847
Revises: 722ed00c082c
Create Date: 2022-10-22 13:33:05.121075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8978ff57847'
down_revision = '722ed00c082c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_talent')
    # ### end Alembic commands ###