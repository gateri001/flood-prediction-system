# app/api.py
from fastapi import FastAPI
from pydantic import BaseModel, Field
from utils import FloodModel, FEATURES
from alerts import risk_level, recommendation
from locales import MESSAGES
from config import DEFAULT_LANG

app = FastAPI(title="Flood Prediction API", version="1.0.0")
model = FloodModel()

class InputPayload(BaseModel):
    rainfall: float = Field(..., description="mm")
    river_level: float = Field(..., description="meters")
    soil_moisture: float = Field(..., ge=0, le=1)
    runoff_rate: float = Field(..., description="mm/hr")
    catchment_slope: float = Field(..., description="degrees")
    upstream_release: float = Field(..., description="normalized anomaly")
    lang: str = Field(DEFAULT_LANG, description="en|sw|ki")

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/predict")
def predict(payload: InputPayload):
    prob = model.predict_proba(payload.dict())
    level = risk_level(prob)
    lang = payload.lang if payload.lang in MESSAGES else DEFAULT_LANG
    message = MESSAGES[lang][level]
    return {
        "probability": round(prob, 4),
        "risk_level": level,
        "message": message,
        "recommendation": recommendation(level)
    }
