from pydantic import BaseModel
from typing import List

class PredictionRequest(BaseModel):
    data: List[List[float]]

class PredictionResponse(BaseModel):
    predictions: List[str]
