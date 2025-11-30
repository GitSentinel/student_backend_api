from fastapi import FastAPI
from app import health, feature

app = FastAPI(title="Student AI API")

app.include_router(health.router)
app.include_router(feature.router)