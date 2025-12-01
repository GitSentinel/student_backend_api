from fastapi import FastAPI
from app import health, feature

app = FastAPI(
    title="Student Journey AI Service",
    description="A simple backend showcasing AI integration for student support."
)

app.include_router(health.router)
app.include_router(feature.router)
