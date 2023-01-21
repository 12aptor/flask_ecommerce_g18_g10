"""categorias productos model

Revision ID: a93eb965157e
Revises: 385132c4043b
Create Date: 2023-01-21 11:41:36.354544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a93eb965157e'
down_revision = '385132c4043b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias_productos',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('categorias_productos')
    # ### end Alembic commands ###