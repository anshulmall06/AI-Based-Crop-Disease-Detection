from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from database.database import prediction_collection
from middleware.auth_middleware import verify_token

from pathlib import Path
import shutil
import uuid

from ml.predictor import predict

router = APIRouter()

# Upload folder
BASE_DIR = Path(__file__).resolve().parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

UPLOAD_DIR.mkdir(exist_ok=True)


@router.post("/predict")
async def predict_disease(
    file: UploadFile = File(...),
    user=Depends(verify_token)
):

    # Check file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload an image."
        )

    # Save uploaded image
    file_extension = Path(file.filename).suffix
    filename = f"{uuid.uuid4()}{file_extension}"
    file_path = UPLOAD_DIR / filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Predict using ONNX
    try:
        result = predict(file_path)

        disease = result["disease"]
        confidence = result["confidence"]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

    # Save prediction to MongoDB
    prediction_data = {
        "email": user["sub"],
        "filename": file.filename,
        "disease": disease,
        "confidence": confidence
    }

    inserted = prediction_collection.insert_one(prediction_data)

    prediction_data["_id"] = str(inserted.inserted_id)

    return prediction_data