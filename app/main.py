from fastapi import FastAPI
from app.api.v1 import pnl

app = FastAPI(title="Energy Trading API", version="1.0.0")

app.include_router(pnl.router, prefix="/v1")
