
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY not found in .env file")

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
- If the disease identification is uncertain, mention that advice should be verified.
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        if not response.text:
            raise HTTPException(
                status_code=502,
                detail="Gemini returned an empty response. Please try again."
            )

        return {
            "answer": response.text
        }

    except HTTPException:
        raise

    except Exception as e:

        error_message = str(e)
        error_lower = error_message.lower()

        # Quota exceeded
        if "429" in error_message or "quota" in error_lower:
            raise HTTPException(
                status_code=429,
                detail="Gemini API quota exceeded. Please try again after some time."
            )

        # Temporary model/server overload
        elif "503" in error_message or "unavailable" in error_lower:
            raise HTTPException(
                status_code=503,
                detail="Gemini AI is temporarily unavailable. Please try again later."
            )

        # Invalid model or request
        elif "404" in error_message:
            raise HTTPException(
                status_code=502,
                detail="The configured Gemini model is unavailable."
            )

        # Other errors
        else:
            print("Gemini API Error:", error_message)

            raise HTTPException(
                status_code=500,
                detail="Unable to generate disease explanation. Please try again."
            )
