from fastapi import FastAPI
from .schemas import PredictionRequest, PredictionResponse
from .model import model

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML-Docker API"}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    predictions = model.predict(request.data)
    return PredictionResponse(predictions=predictions)
