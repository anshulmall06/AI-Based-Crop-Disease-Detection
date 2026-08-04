from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from database.database import prediction_collection
from middleware.auth_middleware import verify_token

import tensorflow as tf
import numpy as np
from PIL import Image
import json
import os

router = APIRouter()

# -------------------------------------------------
# Load Model and Class Names (Only Once)
# -------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "ml_model", "crop_disease_model.h5")
CLASS_PATH = os.path.join(BASE_DIR, "ml_model", "class_names.json")

try:
    model = tf.keras.models.load_model(MODEL_PATH)

    with open(CLASS_PATH, "r") as f:
        class_names = json.load(f)

    print("✅ Crop disease model loaded successfully.")
    print(f"✅ Loaded {len(class_names)} classes.")

except Exception as e:
    print(f"❌ Error loading model: {e}")
    raise e


# -------------------------------------------------
# Prediction API
# -------------------------------------------------

@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    user=Depends(verify_token)
):

    # Check uploaded file type
    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a valid image file."
        )

    # Read image
    try:
        image = Image.open(file.file).convert("RGB")
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid image file."
        )

    # Preprocess image
    image = image.resize((180, 180))
    image = np.array(image, dtype=np.float32)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image, verbose=0)

    predicted_index = int(np.argmax(prediction))
    confidence = round(float(np.max(prediction)) * 100, 2)

    disease = class_names[predicted_index]

    # Save prediction
    prediction_data = {
        "email": user["sub"],
        "filename": file.filename,
        "disease": disease,
        "confidence": confidence
    }

    result = prediction_collection.insert_one(prediction_data)

    prediction_data["_id"] = str(result.inserted_id)

    return prediction_data