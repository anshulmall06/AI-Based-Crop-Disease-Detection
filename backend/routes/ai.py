
import os
import re
import asyncio
import logging

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is not configured")

# Initialize Gemini client
client = genai.Client(api_key=api_key)

# Gemini models
PRIMARY_MODEL = "gemini-3.5-flash-lite"
FALLBACK_MODEL = "gemini-3.8-flash"

MODELS = [PRIMARY_MODEL, FALLBACK_MODEL]

router = APIRouter()


class DiseaseRequest(BaseModel):
    disease: str


def get_error_code(error):
    """Extract HTTP error code from Gemini exception."""

    code = getattr(error, "code", None)

    if code is None:
        code = getattr(error, "status_code", None)

    if code is not None:
        try:
            return int(code)
        except (ValueError, TypeError):
            pass

    match = re.search(
        r"\b(400|401|403|404|429|500|502|503|504)\b",
        str(error)
    )

    return int(match.group(1)) if match else None


def generate_with_gemini(model, prompt):
    """Generate content using Gemini."""

    return client.models.generate_content(
        model=model,
        contents=prompt
    )


@router.post("/ai/explain")
async def explain_disease(request: DiseaseRequest):

    disease = request.disease.strip()

    if not disease:
        raise HTTPException(
            status_code=400,
            detail="Disease name cannot be empty."
        )

    prompt = f"""
You are an agricultural expert helping farmers.

A crop disease has been detected:

Disease: {disease}

Explain this disease in simple English.

Provide the following sections:

1. Disease Description
2. Symptoms
3. Causes
4. Treatment
5. Prevention
6. Farmer Tips

Instructions:
- Use simple and clear English.
- Give practical advice for farmers.
- Keep the explanation concise.
- Do not invent pesticide dosages.
- Recommend following product labels and local agricultural guidance.
- If disease identification is uncertain, mention that advice
  should be verified with a local agricultural expert.
"""

    # Try primary model and then fallback model
    for model in MODELS:

        logger.info("Trying Gemini model: %s", model)

        # Maximum two attempts for each model
        for attempt in range(2):

            try:
                logger.info(
                    "Gemini request: model=%s attempt=%s",
                    model,
                    attempt + 1
                )

                response = await asyncio.to_thread(
                    generate_with_gemini,
                    model,
                    prompt
                )

                if response and response.text:
                    logger.info(
                        "Gemini response generated successfully using %s",
                        model
                    )

                    return {
                        "answer": response.text
                    }

                logger.warning(
                    "Empty Gemini response from model: %s",
                    model
                )

                break

            except Exception as e:

                error_code = get_error_code(e)

                logger.exception(
                    "Gemini API error: model=%s code=%s",
                    model,
                    error_code
                )

                # API quota exceeded
                if error_code == 429:
                    raise HTTPException(
                        status_code=429,
                        detail="Gemini API quota exceeded. Please try again later."
                    )

                # Authentication error
                if error_code == 401:
                    raise HTTPException(
                        status_code=502,
                        detail="Gemini API authentication failed. Check API configuration."
                    )

                # Permission error
                if error_code == 403:
                    raise HTTPException(
                        status_code=502,
                        detail="Gemini API access denied. Check API permissions."
                    )

                # Invalid model
                if error_code == 404:
                    logger.warning(
                        "Model %s is unavailable. Trying next model.",
                        model
                    )
                    break

                # Temporary server errors
                if error_code in (500, 502, 503, 504):

                    if attempt == 0:
                        wait_time = 2

                        logger.warning(
                            "Temporary Gemini error. Retrying in %s seconds.",
                            wait_time
                        )

                        await asyncio.sleep(wait_time)
                        continue

                    logger.warning(
                        "Model %s failed after retries. Trying fallback.",
                        model
                    )

                    break

                # Unknown error
                raise HTTPException(
                    status_code=502,
                    detail="Unable to generate disease explanation."
                )

        logger.info(
            "Moving to next Gemini model if available."
        )

    # All Gemini models failed
    logger.error("All configured Gemini models are unavailable.")

    raise HTTPException(
        status_code=503,
        detail="AI service is temporarily unavailable. Please try again later."
    )
