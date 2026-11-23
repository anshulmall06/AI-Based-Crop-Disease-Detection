
import os
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

# Gemini model
MODEL_NAME = "gemini-3.5-flash-lite"

router = APIRouter()


class DiseaseRequest(BaseModel):
    disease: str


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

Provide these sections:

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
- Mention uncertainty if identification is not reliable.
"""

    try:
        logger.info("Sending Gemini request for disease: %s", disease)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if not response.text:
            logger.error("Gemini returned an empty response")

            raise HTTPException(
                status_code=502,
                detail="Gemini returned an empty response."
            )

        logger.info("Gemini response generated successfully")

        return {
            "answer": response.text
        }

    except HTTPException:
        raise

    except Exception as e:

        # Print the actual error in Render Logs
        logger.exception("GEMINI API ERROR")

        error_message = str(e).lower()

        if "429" in error_message or "quota" in error_message:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded."
            )

        if "401" in error_message or "api key" in error_message:
            raise HTTPException(
                status_code=502,
                detail="Gemini API authentication failed. Check server configuration."
            )

        if "403" in error_message:
            raise HTTPException(
                status_code=502,
                detail="Gemini API access denied. Check API permissions."
            )

        if "404" in error_message:
            raise HTTPException(
                status_code=502,
                detail="Gemini model or API endpoint not found."
            )

        if "503" in error_message or "unavailable" in error_message:
            raise HTTPException(
                status_code=503,
                detail="Gemini service is temporarily unavailable."
            )

        raise HTTPException(
            status_code=502,
            detail="Unable to generate disease explanation."
        )
