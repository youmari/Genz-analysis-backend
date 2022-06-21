from typing import Optional
from pydantic import BaseModel

class YoungPeople(BaseModel):
  id: int
  date: str
  logits: float
  net_sent: float
  logits_mean: float
  net_sent_mean: float
  ma_logits: float
  ma_net_sent: float
  ma_net_sent_ema_alpha_0_1: float
  ma_net_sent_ema_alpha_0_3: float
  ma_net_sent_ema_alpha_0_5: float

class SentenceAnalysisBase(BaseModel):
  category: Optional[str]
  sentence: str
  sentence_short: str
  sentence_keywords: str
  sentence_semtiment: str
  sentence_semtiment_net: float
  sentence_sent_score: float
  sentence_sentiment_label: int 
  sentence_entities: str
  sentence_non_entities:str


class SentenceAnalysisCreate(SentenceAnalysisBase):
    ...


class SentenceAnalysis(SentenceAnalysisBase):
    id: int
    date: str
    class Config:
        orm_mode = True




class SentenceAnalysisAndYoung(SentenceAnalysis):
  ...

  
