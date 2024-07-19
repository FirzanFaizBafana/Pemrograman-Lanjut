from fastapi import FastAPI
from app.routes import buku

app = FastAPI()

app.include_router(buku.router)
