from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router

app = FastAPI(title="Target Master", version="1.0")
