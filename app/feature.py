from fastapi import APIRouter
from app.schemas import FeatureRequest, FeatureResponse
from app.ai_service import analyze_text_with_ai
from app.logging_config import logger

router = APIRouter()

@router.post("/feature/", response_model=FeatureResponse)
async def feature_endpoint(input: FeatureRequest):
    logger.info(f"POST /feature request: {input.text[:60]}...")

    ai_result = analyze_text_with_ai(input.text)

    logger.info(
        f"AI result → summary='{ai_result.get('summary')}', "
        f"sentiment='{ai_result.get('sentiment')}'"
    )

    return FeatureResponse(
        summary=ai_result.get("summary", "AI unavailable."),
        sentiment=ai_result.get("sentiment", "neutral")
    )
