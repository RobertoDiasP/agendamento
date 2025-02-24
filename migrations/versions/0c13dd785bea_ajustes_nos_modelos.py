"""Ajustes nos modelos

Revision ID: 0c13dd785bea
Revises: af646b0c0ae4
Create Date: 2024-08-16 14:49:13.389930

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0c13dd785bea'
down_revision = 'af646b0c0ae4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agenda', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hora', sa.String(length=4), nullable=False))
        batch_op.drop_index('email')
        batch_op.drop_column('senha')
        batch_op.drop_column('atualizado_em')
        batch_op.drop_column('email')
        batch_op.drop_column('nome')
        batch_op.drop_column('tipo')
        batch_op.drop_column('criado_em')
        batch_op.drop_column('hota')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('agenda', schema=None) as batch_op:
        batch_op.add_column(sa.Column('hota', mysql.VARCHAR(collation='utf8_unicode_ci', length=4), nullable=False))
        batch_op.add_column(sa.Column('criado_em', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('tipo', mysql.VARCHAR(collation='utf8_unicode_ci', length=10), nullable=False))
        batch_op.add_column(sa.Column('nome', mysql.VARCHAR(collation='utf8_unicode_ci', length=100), nullable=False))
        batch_op.add_column(sa.Column('email', mysql.VARCHAR(collation='utf8_unicode_ci', length=120), nullable=False))
        batch_op.add_column(sa.Column('atualizado_em', mysql.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('senha', mysql.VARCHAR(collation='utf8_unicode_ci', length=128), nullable=False))
        batch_op.create_index('email', ['email'], unique=True)
        batch_op.drop_column('hora')

    # ### end Alembic commands ###
