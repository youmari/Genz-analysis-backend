"""empty message

Revision ID: 653d409d2819
Revises: 
Create Date: 2022-06-13 12:20:34.345161

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '653d409d2819'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sentences_analysis',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('category', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('sentence', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('sentence_short', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('sentence_keywords', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('sentence_semtiment', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('sentence_semtiment_net', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sentence_sent_score', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sentence_sentiment_label', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('sentence_entities', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('sentence_non_entities', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='sentences_analysis_pkey')
    )
    op.create_index('ix_sentences_analysis_id', 'sentences_analysis', ['id'], unique=False)
    op.create_index('ix_sentences_analysis_category', 'sentences_analysis', ['category'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   pass
    # ### end Alembic commands ###
