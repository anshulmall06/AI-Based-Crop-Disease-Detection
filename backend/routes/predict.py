from fastapi import APIRouter, UploadFile, File, HTTPException, Request
from database.database import prediction_collection

from pathlib import Path
import shutil
import uuid

from jose import jwt, JWTError
from dotenv import load_dotenv
import os

from ml.predictor import predict

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = "HS256"

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/predict")
async def predict_disease(
    request: Request,
    file: UploadFile = File(...)
):

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image."
        )

    file_extension = Path(file.filename).suffix
    filename = f"{uuid.uuid4()}{file_extension}"
    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = predict(file_path)

        disease = result["disease"]
        confidence = result["confidence"]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

    # Save prediction only if user is logged in
    auth = request.headers.get("Authorization")

    if auth and auth.startswith("Bearer "):
        token = auth.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=[ALGORITHM]
            )

            prediction_collection.insert_one({
                "email": payload["sub"],
                "filename": file.filename,
                "disease": disease,
                "confidence": confidence
            })

        except JWTError:
            # Ignore invalid token and still return prediction
            pass

    return {
        "filename": file.filename,
        "disease": disease,
        "confidence": confidence
    }