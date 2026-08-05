from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.predict import router as predict_router
from routes.auth import router as auth_router
from routes.history import router as history_router
from routes.ai import router as ai_router

app = FastAPI(
    title="AI Crop Disease Detection API"
)

app.add_middleware(
    CORSMiddleware,
    app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ai-based-crop-disease-detection-git-main-tbi4.vercel.app",
        "https://ai-based-crop-disease-detection-2xh7jr4m1-tbi4.vercel.app",
        "http://localhost:3000"
    ],
   
)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(auth_router)
app.include_router(predict_router)
app.include_router(history_router)
app.include_router(ai_router)


@app.api_route("/", methods=["GET", "HEAD"])
def home():
    return {
        "message": "AI Crop Disease Detection API Running Successfully"
    }