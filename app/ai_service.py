import json
from google import genai
from app.config import settings

client = genai.Client(api_key=settings.GEMINI_API_KEY)

# Use stable + correct model
MODEL_NAME = "models/gemini-flash-latest"


def analyze_text_with_ai(text: str) -> dict:
    """
    Calls Gemini to get:
    - summary
    - sentiment
    Returns: dict
    """
    prompt = f"""
    Analyze the following text:

    "{text}"

    1. Give a one-line summary.
    2. Give sentiment as: positive / negative / neutral.

    Return ONLY valid JSON like this:
    {{
      "summary": "...",
      "sentiment": "..."
    }}
    """

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        ai_text = response.text.strip()

        # Try parsing JSON
        try:
            return json.loads(ai_text)
        except:
            print("AI returned non-JSON:", ai_text)
            return {
                "summary": "AI unavailable.",
                "sentiment": "neutral"
            }

    except Exception as e:
        print("Gemini Error:", e)
        return {
            "summary": "AI unavailable.",
            "sentiment": "neutral"
        }
