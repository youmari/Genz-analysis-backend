from sqlalchemy.orm import Session, joinedload
from db.models.sentence_analysis import SentenceAnalyis


def get_sentences(db: Session):
    return db.query(SentenceAnalyis).limit(300).all()

def get_analysis(db: Session):
    return db.query(SentenceAnalyis).options(joinedload(SentenceAnalyis.young_people)).all()

