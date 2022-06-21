"""empty message

Revision ID: 1a969288b598
Revises: 27f99a3bfaa3
Create Date: 2022-06-18 13:22:52.362752

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1a969288b598'
down_revision = '27f99a3bfaa3'
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
    op.create_index('ix_sentences_analysis_sentence', 'sentences_analysis', ['sentence'], unique=False)    
    op.create_index('ix_sentences_analysis_sentence_short', 'sentences_analysis', ['sentence_short'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_keywords', 'sentences_analysis', ['sentence_keywords'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_semtiment', 'sentences_analysis', ['sentence_semtiment'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_semtiment_net', 'sentences_analysis', ['sentence_semtiment_net'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_sent_scoret', 'sentences_analysis', ['sentence_sent_score'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_sentiment_label', 'sentences_analysis', ['sentence_sentiment_label'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_entities', 'sentences_analysis', ['sentence_entities'], unique=False)
    op.create_index('ix_sentences_analysis_sentence_non_entities', 'sentences_analysis', ['sentence_non_entities'], unique=False)
    op.create_table('young_people_analysis',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('logits', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('net_sent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('logits_mean', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('net_sent_mean', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('ma_logits', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('ma_net_sent', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('ma_net_sent_ema_alpha_0_1', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('ma_net_sent_ema_alpha_0_3', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('ma_net_sent_ema_alpha_0_5', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sentence_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['sentence_id'], ['sentences_analysis.id'], name='young_people_analysis_sentence_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='young_people_analysis_pkey')
    )
    op.create_index('ix_young_people_analysis_net_sent_mean', 'young_people_analysis', ['net_sent_mean'], unique=False)
    op.create_index('ix_young_people_analysis_net_sent', 'young_people_analysis', ['net_sent'], unique=False)
    op.create_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_5', 'young_people_analysis', ['ma_net_sent_ema_alpha_0_5'], unique=False)
    op.create_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_3', 'young_people_analysis', ['ma_net_sent_ema_alpha_0_3'], unique=False)
    op.create_index('ix_young_people_analysis_ma_net_sent_ema_alpha_0_1', 'young_people_analysis', ['ma_net_sent_ema_alpha_0_1'], unique=False)
    op.create_index('ix_young_people_analysis_ma_net_sent', 'young_people_analysis', ['ma_net_sent'], unique=False)
    op.create_index('ix_young_people_analysis_ma_logits', 'young_people_analysis', ['ma_logits'], unique=False)
    op.create_index('ix_young_people_analysis_logits_mean', 'young_people_analysis', ['logits_mean'], unique=False)
    op.create_index('ix_young_people_analysis_logits', 'young_people_analysis', ['logits'], unique=False)
    op.create_index('ix_young_people_analysis_id', 'young_people_analysis', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   pass
    # ### end Alembic commands ###