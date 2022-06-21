from fastapi import FastAPI
from api import sentences_analysis
from db.db_setup import engine
from db.models import sentence_analysis
from fastapi.middleware.cors import CORSMiddleware

sentence_analysis.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GenZ analysis backend",
    description="this is a backend of sentences sentiments anaylsis"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(sentences_analysis.router)
