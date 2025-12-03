from pydantic import BaseModel

class FeatureRequest(BaseModel):
    text: str   # student's input text


class FeatureResponse(BaseModel):
    summary: str
    sentiment: str