from fastapi import FastAPI
from app.controllers import pnl_controller

app = FastAPI(title="Energy Trading API", version="1.0.0")

app.include_router(pnl_controller.router, prefix="/v1")

