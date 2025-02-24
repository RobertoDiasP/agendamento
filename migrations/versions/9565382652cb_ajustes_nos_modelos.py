"""Ajustes nos modelos

Revision ID: 9565382652cb
Revises: 1f4582ba777a
Create Date: 2024-08-16 15:40:12.564510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9565382652cb'
down_revision = '1f4582ba777a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('preco', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('fornecedor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fornecedor_id'], ['fornecedor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servico',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=100), nullable=False),
    sa.Column('descricao', sa.Text(), nullable=True),
    sa.Column('preco', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('fornecedor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fornecedor_id'], ['fornecedor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('produtos_agendamentos',
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('agendamento_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agendamento_id'], ['agendamento.id'], ),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], ),
    sa.PrimaryKeyConstraint('produto_id', 'agendamento_id')
    )
    op.create_table('servicos_agendamentos',
    sa.Column('servico_id', sa.Integer(), nullable=False),
    sa.Column('agendamento_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['agendamento_id'], ['agendamento.id'], ),
    sa.ForeignKeyConstraint(['servico_id'], ['servico.id'], ),
    sa.PrimaryKeyConstraint('servico_id', 'agendamento_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('servicos_agendamentos')
    op.drop_table('produtos_agendamentos')
    op.drop_table('servico')
    op.drop_table('produto')
    # ### end Alembic commands ###
