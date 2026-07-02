from fastapi import FastAPI
from campeonato_service import router as campeonato_router

app = FastAPI(
    title="API futbet",
    version="0.0.1"
)

app.include_router(campeonato_router, prefix="/campeonatos")