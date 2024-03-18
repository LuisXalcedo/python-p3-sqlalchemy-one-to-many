"""Create Game Model

Revision ID: 7dc7b65ecb2a
Revises: faebd12f9523
Create Date: 2024-03-17 19:18:21.694960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7dc7b65ecb2a'
down_revision = 'faebd12f9523'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('genre', sa.String(), nullable=True),
    sa.Column('platform', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###