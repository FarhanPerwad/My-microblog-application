"""new fields in user model

Revision ID: 61400b3e4118
Revises: d7bd51b4d966
Create Date: 2020-07-01 02:32:12.044704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61400b3e4118'
down_revision = 'd7bd51b4d966'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
