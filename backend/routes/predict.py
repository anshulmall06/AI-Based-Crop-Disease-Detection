from fastapi import APIRouter, UploadFile, File, HTTPException
from database.database import prediction_collection

from pathlib import Path
import shutil
import uuid

from ml.predictor import predict

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/predict")
async def predict_disease(file: UploadFile = File(...)):

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

    return {
        "filename": file.filename,
        "disease": disease,
        "confidence": confidence
    }