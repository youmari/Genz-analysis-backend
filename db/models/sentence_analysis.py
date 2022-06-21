from operator import index
from ..db_setup import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float
from sqlalchemy.orm import relationship


class SentenceAnalyis(Base):
  __tablename__ = "sentences_analysis"
  
  id = Column(Integer, primary_key=True, index=True)
  date = Column(String(50), nullable=False)
  category = Column(String(100), nullable=True)
  sentence = Column(Text, nullable=False, index=True)
  sentence_short = Column(String, nullable=False)
  sentence_keywords = Column(String, nullable=False)
  sentence_semtiment = Column(String, nullable=False)
  sentence_semtiment_net = Column(Float, nullable=False)
  sentence_sent_score = Column(Float, nullable=False)
  sentence_sentiment_label = Column(Integer, nullable=False)
  sentence_entities = Column(String, nullable=True)
  sentence_non_entities = Column(String, nullable=False)

  young_people = relationship("YoungPeople", back_populates="young_people_info", uselist=False)


class YoungPeople(Base):
  __tablename__ = "young_people_analysis"
   
  id = Column(Integer, primary_key=True, index=True)
  date = Column(String(50), nullable=False)
  logits = Column(Float, nullable=False)
  net_sent = Column(Float, nullable=False)
  logits_mean = Column(Float, nullable=False)
  net_sent_mean = Column(Float, nullable=False)
  ma_logits = Column(Float, nullable=False)
  ma_net_sent = Column(Float, nullable=False)
  ma_net_sent_ema_alpha_0_1 = Column(Float, nullable=False)
  ma_net_sent_ema_alpha_0_3 = Column(Float, nullable=False)
  ma_net_sent_ema_alpha_0_5 = Column(Float, nullable=False)

  sentence_id = Column(Integer, ForeignKey("sentences_analysis.id"), nullable=False)
  young_people_info = relationship("SentenceAnalyis", back_populates="young_people")