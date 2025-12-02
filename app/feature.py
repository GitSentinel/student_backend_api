from fastapi import APIRouter
from app.schemas import FeatureRequest, FeatureResponse

router = APIRouter(prefix="/feature", tags=["Feature"])

def simple_sentiment(text: str) -> str:
    text_lower = text.lower()

    if any(word in text_lower for word in ["happy", "great", "excited", "good"]):
        return "positive"
    elif any(word in text_lower for word in ["sad", "stressed", "bad", "tired"]):
        return "negative"
    else:
        return "neutral"


@router.post("/", response_model=FeatureResponse)
def process_feature(payload: FeatureRequest):
    text = payload.text

    summary = text[:50] + "..." if len(text) > 50 else text
    sentiment = simple_sentiment(text)

    return FeatureResponse(
        summary=summary,
        sentiment=sentiment
    )
