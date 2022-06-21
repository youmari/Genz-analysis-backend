from typing import Dict, List
import fastapi
from api.utils.crud import get_analysis, get_sentences
from db.db_setup import get_db
from sqlalchemy.orm import Session

from pydantic_schemas.sentence_analysis import SentenceAnalysis

router = fastapi.APIRouter()


@router.get(
    "/api/v1/sentences",
    response_model=List[SentenceAnalysis],
    description="Get all the sentences with All the analysis"
)
def read_sentences(db: Session = fastapi.Depends(get_db)):
    sentences = get_sentences(db)
    return sentences

@router.get(
    "/api/v1/young_people_analysis",
    description="Get all the sentences with All the analysis and also with young people sentiment scores"
)
def read_analysis_with_young_people(db: Session = fastapi.Depends(get_db)):
    sentences = get_analysis(db)
    return sentences
