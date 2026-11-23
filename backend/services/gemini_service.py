
import os
import logging

from dotenv import load_dotenv
from google import genai

load_dotenv()

logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


def generate_crop_advice(disease, confidence):

    if client is None:
        raise ValueError("GEMINI_API_KEY is missing")

    prompt = f"""
You are an agricultural disease advisory assistant.

Disease: {disease}
Prediction Confidence: {confidence}%

Provide advice using these headings:

1. Disease Description
2. Symptoms
3. Causes
4. Treatment
5. Prevention
6. Recommended Fungicide/Pesticide
7. Farmer Tips

Instructions:
- Use simple language for farmers.
- Do not invent pesticide names or dosage.
- Recommend only locally approved treatments.
- Always advise following product labels.
- Mention when expert confirmation is needed.
- If confidence is low, clearly explain that the prediction is uncertain.
"""

    try:
        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
            contents=prompt
        )

        if not response.text or not response.text.strip():
            raise ValueError("Gemini returned an empty response")

        return response.text.strip()

    except Exception:
        logger.exception("Gemini crop advice generation failed")
        raise
