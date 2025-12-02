from fastapi import APIRouter
from app.schemas import FeatureRequest, FeatureResponse

router = APIRouter(prefix="/feature", tags=["Feature"])

@router.post("/", response_model=FeatureResponse)
def process_feature(payload: FeatureRequest):
    # temporary placeholder logic
    return FeatureResponse(
        summary=f"Received text of length {len(payload.text)}",
        sentiment="neutral"
    )