from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.predict import router as predict_router
from routes.auth import router as auth_router
from routes.history import router as history_router
from routes.ai import router as ai_router


app = FastAPI(
    title="AI Crop Disease Detection API"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,

    # Accept all Vercel preview deployments
    allow_origin_regex=r"https://ai-based-crop-disease-detection-[a-z0-9]+-tbi4\.vercel\.app",

    # Local development
    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Routes
app.include_router(auth_router)
app.include_router(predict_router)
app.include_router(history_router)
app.include_router(ai_router)


@app.api_route("/", methods=["GET", "HEAD"])
def home():
    return {
        "message": "AI Crop Disease Detection API Running Successfully"
    }