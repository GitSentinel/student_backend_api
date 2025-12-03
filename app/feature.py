from fastapi import APIRouter
from pydantic import BaseModel
from app.ai_service import analyze_text_with_ai

router = APIRouter()

class InputText(BaseModel):
    text: str

class AIResponse(BaseModel):
    summary: str
    sentiment: str


@router.post("/feature/", response_model=AIResponse)
async def feature_endpoint(input: InputText):

    ai_result = analyze_text_with_ai(input.text)

    return AIResponse(
        summary=ai_result.get("summary", "AI unavailable."),
        sentiment=ai_result.get("sentiment", "neutral")
    )
