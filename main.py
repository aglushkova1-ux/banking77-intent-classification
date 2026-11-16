from fastapi import FastAPI
from pydantic import BaseModel
from distilbert_prediction import distilbert_predict
from database import save_prediction
import time
import psycopg
import logging

app = FastAPI()

class Query(BaseModel):
    text: str
logger = logging.getLogger(__name__)
@app.post("/predict")
def predict(query: Query):
    start_time = time.perf_counter()
    predicted_class = distilbert_predict(query.text)
    inference_time = (time.perf_counter() - start_time) * 1000
    try:
        save_prediction(query.text, predicted_class, inference_time)
    except psycopg.Error:
        logger.exception("Failed to save prediction")
    return {"predicted class": predicted_class}