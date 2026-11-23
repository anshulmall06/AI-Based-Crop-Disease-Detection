
import os
import asyncio
import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai

from .disease_advice import get_local_advice

load_dotenv()

router = APIRouter()
logger = logging.getLogger(__name__)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PRIMARY_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash"
)

FALLBACK_MODEL = "gemini-3.5-flash-lite"

client = (
    genai.Client(api_key=GEMINI_API_KEY)
    if GEMINI_API_KEY else None
)


class DiseaseRequest(BaseModel):
    disease: str
    confidence: float | None = None


def create_prompt(disease, confidence=None):

    return f"""
You are an agricultural disease advisory assistant.

Predicted Disease: {disease}
Prediction Confidence: {confidence if confidence is not None else "Not provided"}%

Generate practical advice for farmers using these headings:

1. Description
2. Symptoms
3. Causes
4. Treatment
5. Prevention
6. Farmer Tips

Instructions:
- Use simple language.
- Do not invent pesticide names or dosage.
- Recommend only locally approved treatments.
- Advise farmers to follow product labels.
- Mention when expert confirmation is needed.
- Explain uncertainty if confidence is low.
"""


def generate_gemini_answer(model_name, prompt):

    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )

    answer = response.text

    if not answer or not answer.strip():
        raise ValueError("Gemini returned an empty response")

    return answer.strip()


@router.post("/ai/explain")
async def explain_disease(request: DiseaseRequest):

    disease = request.disease.strip()

    if not disease:
        raise HTTPException(
            status_code=400,
            detail="Disease name cannot be empty"
        )

    confidence = request.confidence

    # Try Gemini AI first
    if client is not None:

        prompt = create_prompt(disease, confidence)

        models_to_try = list(dict.fromkeys([
            PRIMARY_MODEL,
            FALLBACK_MODEL
        ]))

        for model_name in models_to_try:

            try:
                logger.info(
                    "Trying Gemini model: %s",
                    model_name
                )

                answer = await asyncio.to_thread(
                    generate_gemini_answer,
                    model_name,
                    prompt
                )

                logger.info(
                    "Gemini advice generated successfully using %s",
                    model_name
                )

                return {
                    "answer": answer,
                    "source": "gemini"
                }

            except Exception:
                logger.exception(
                    "Gemini model %s failed",
                    model_name
                )

    else:
        logger.warning(
            "Gemini API key missing. Using local advice."
        )

    # Automatic local fallback
    logger.warning(
        "Using local disease advice for: %s",
        disease
    )

    local_answer = get_local_advice(
        disease,
        confidence
    )

    return {
        "answer": local_answer,
        "source": "local"
    }
