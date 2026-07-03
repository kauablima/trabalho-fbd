from fastapi import FastAPI
from crud_aposta import router as aposta_router

app = FastAPI(
    title="API futbet",
    version="0.0.1"
)

app.include_router(aposta_router, prefix="/apostas")