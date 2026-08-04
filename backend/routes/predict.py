from fastapi import APIRouter, UploadFile, File, Depends
from database.database import prediction_collection
from middleware.auth_middleware import verify_token

import tensorflow as tf
import numpy as np
from PIL import Image
import json

router = APIRouter()

# Load model only once
model = tf.keras.models.load_model("ml_model/crop_disease_model.keras")

# Load class names
with open("ml_model/class_names.json", "r") as f:
    class_names = json.load(f)


@router.post("/predict")
async def predict(
    file: UploadFile = File(...),
    user=Depends(verify_token)
):

    # Read uploaded image
    image = Image.open(file.file).convert("RGB")

    # Resize to training size
    image = image.resize((180, 180))

    # Convert to NumPy array
    image = np.array(image)

    # Normalize
    image = image / 255.0

    # Add batch dimension
    image = np.expand_dims(image, axis=0)

    # Prediction
    prediction = model.predict(image)

    predicted_index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    disease = class_names[predicted_index]

    prediction_data = {
        "email": user["sub"],
        "filename": file.filename,
        "disease": disease,
        "confidence": round(confidence, 2)
    }

    result = prediction_collection.insert_one(prediction_data)

    prediction_data["_id"] = str(result.inserted_id)

    return prediction_data