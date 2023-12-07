from fastapi import FastAPI

from app.model.model import __version__ as model_version
from app.model.model import predict_pipeline

app = FastAPI()


@app.get("/")
def root():
    return {"message": "language detection model", "model_version": model_version}


@app.post("/predict")
def predict(text: str):
    language = predict_pipeline(text)
    return {"language": language}
