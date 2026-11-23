
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

client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None


class DiseaseRequest(BaseModel):
    disease: str


def create_prompt(disease: str) -> str:
    return f"""
You are an agricultural disease advisory assistant.

Explain the following plant disease in simple language for farmers.

Disease: {disease}

Give the answer using these headings:

1. Description
2. Symptoms
3. Causes
4. Treatment
5. Prevention
6. Farmer Tips

Important instructions:
- Give practical and easy-to-understand advice.
- Do not invent pesticide names or dosage.
- Recommend only locally approved treatments.
- Mention when expert confirmation is needed.
- If the plant is healthy, provide preventive care advice.
"""


def generate_gemini_answer(model_name: str, prompt: str) -> str:
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

    prompt = create_prompt(disease)

    # Try Gemini first
    if client is not None:

        models_to_try = list(dict.fromkeys([
            PRIMARY_MODEL,
            FALLBACK_MODEL
        ]))

        for model_name in models_to_try:
            try:
                logger.info("Trying Gemini model: %s", model_name)

                answer = await asyncio.to_thread(
                    generate_gemini_answer,
                    model_name,
                    prompt
                )

                logger.info(
                    "Gemini response generated successfully using %s",
                    model_name
                )

                return {"answer": answer}

            except Exception as error:
                logger.warning(
                    "Gemini model %s failed: %s",
                    model_name,
                    str(error)
                )

    else:
        logger.warning(
            "GEMINI_API_KEY is missing. Using local disease advice."
        )

    # Automatic local fallback
    logger.info("Using local disease advice for: %s", disease)

    local_answer = get_local_advice(disease)

    return {"answer": local_answer}
