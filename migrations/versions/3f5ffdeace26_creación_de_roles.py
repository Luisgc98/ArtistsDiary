"""Creación de roles.

Revision ID: 3f5ffdeace26
Revises: 880cfb64c22b
Create Date: 2023-05-01 02:23:14.578706

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '3f5ffdeace26'
down_revision = '880cfb64c22b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xxart_user_role', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.String(length=1), nullable=True))
        batch_op.drop_constraint('xxart_user_role_role_id_key', type_='unique')
        batch_op.drop_constraint('xxart_user_role_user_id_key', type_='unique')

    # ### end Alembic commands ###
    
    role_table = table(
        "xxart_role",
        column("created_date", sa.Date),
        column("created_by", sa.Integer),
        column("updated_date", sa.Date),
        column("updated_by", sa.Integer),
        column("ovn", sa.Integer),
        column("id", sa.Integer),
        column("name", sa.String),
        column("description", sa.String),
        column("is_active", sa.String)
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('xxart_user_role', schema=None) as batch_op:
        batch_op.create_unique_constraint('xxart_user_role_user_id_key', ['user_id'])
        batch_op.create_unique_constraint('xxart_user_role_role_id_key', ['role_id'])
        batch_op.drop_column('is_active')

    # ### end Alembic commands ###
