from fastapi import FastAPI
from app import health, feature
from app.logging_config import logger

app = FastAPI()

logger.info("Starting Student Backend API...")

app.include_router(health.router)
app.include_router(feature.router)