"""
Init

Revision ID: b2b415d07bbd
Revises: 
Create Date: 2024-05-16 17:28:05.044417

"""
from typing import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'b2b415d07bbd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'shorten_url',
        sa.Column('full_url', sa.String(length=100), nullable=False),
        sa.Column('short_url', sa.String(length=100), nullable=False),
        sa.Column('is_deleted', sa.Boolean(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('full_url'),
        sa.UniqueConstraint('short_url')
    )
    op.create_index(op.f('ix_shorten_url_created_at'), 'shorten_url', ['created_at'], unique=False)
    op.create_table(
        'link_click',
        sa.Column('shorten_url_id', sa.Integer(), nullable=False),
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['shorten_url_id'], ['shorten_url.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_link_click_created_at'), 'link_click', ['created_at'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_link_click_created_at'), table_name='link_click')
    op.drop_table('link_click')
    op.drop_index(op.f('ix_shorten_url_created_at'), table_name='shorten_url')
    op.drop_table('shorten_url')
