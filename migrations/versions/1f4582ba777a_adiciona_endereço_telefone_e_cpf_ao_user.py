"""Adiciona endereço, telefone e CPF ao User

Revision ID: 1f4582ba777a
Revises: 0c13dd785bea
Create Date: 2024-08-16 15:17:57.162930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f4582ba777a'
down_revision = '0c13dd785bea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('endereco', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('cidade', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('estado', sa.String(length=255), nullable=True))
        batch_op.add_column(sa.Column('telefone', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('cpf', sa.String(length=11), nullable=True))
        batch_op.create_unique_constraint(None, ['cpf'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('cpf')
        batch_op.drop_column('telefone')
        batch_op.drop_column('estado')
        batch_op.drop_column('cidade')
        batch_op.drop_column('endereco')

    # ### end Alembic commands ###
