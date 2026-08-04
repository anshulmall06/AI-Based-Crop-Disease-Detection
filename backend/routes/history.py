from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId

from database.database import prediction_collection
from middleware.auth_middleware import verify_token


router = APIRouter()


# Get only logged-in user's predictions
@router.get("/predictions")
async def get_predictions(
    user=Depends(verify_token)
):

    user_email = user["sub"]

    predictions = []

    cursor = prediction_collection.find(
        {
            "email": user_email
        }
    ).sort("_id", -1)


    for item in cursor:

        item["_id"] = str(item["_id"])
        predictions.append(item)


    return predictions



# Update only user's own prediction
@router.put("/predictions/{prediction_id}")
async def update_prediction(
    prediction_id: str,
    data: dict,
    user=Depends(verify_token)
):

    result = prediction_collection.update_one(
        {
            "_id": ObjectId(prediction_id),
            "email": user["sub"]
        },
        {
            "$set": {
                "disease": data["disease"],
                "confidence": data["confidence"]
            }
        }
    )


    if result.modified_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found"
        )


    return {
        "message": "Prediction updated successfully"
    }



# Delete only user's own prediction
@router.delete("/predictions/{prediction_id}")
async def delete_prediction(
    prediction_id: str,
    user=Depends(verify_token)
):

    result = prediction_collection.delete_one(
        {
            "_id": ObjectId(prediction_id),
            "email": user["sub"]
        }
    )


    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Prediction not found"
        )


    return {
        "message": "Prediction deleted successfully"
    }