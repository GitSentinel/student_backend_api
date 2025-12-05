import json
from google import genai
from app.config import settings
from app.logging_config import logger

client = genai.Client(api_key=settings.GEMINI_API_KEY)
model_name = "models/gemini-2.5-flash"

def analyze_text_with_ai(text: str) -> dict:
    logger.info(f"AI request received. Text length={len(text)} characters")

    prompt = f"""
    Analyze the following text strictly and return ONLY valid JSON.

    Text: "{text}"

    Respond in exactly this JSON format:

    {{
      "summary": "one sentence summary",
      "sentiment": "positive/negative/neutral"
    }}

    Do not include explanations, markdown, or extra text.
    """

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        ai_text = response.text.strip()
        logger.info("AI response received.")

        try:
            parsed = json.loads(ai_text)
            logger.info("AI JSON parsed successfully.")
            return parsed

        except Exception as e:
            logger.error(f"Failed to parse AI JSON: {e}")
            logger.error(f"Raw AI output: {ai_text}")
            return {
                "summary": "AI unavailable.",
                "sentiment": "neutral"
            }

    except Exception as e:
        logger.error(f"Gemini API call failed: {e}")
        return {
            "summary": "AI unavailable.",
            "sentiment": "neutral"
        }