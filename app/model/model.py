import pickle
from pathlib import Path

import regex as re

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

with open(f"{BASE_DIR}/trained_pipeline-{__version__}.pkl", "rb") as file:
    model = pickle.load(file)

classes = [
    "Arabic",
    "Danish",
    "Dutch",
    "English",
    "French",
    "German",
    "Greek",
    "Hindi",
    "Italian",
    "Kannada",
    "Malayalam",
    "Portugeese",
    "Russian",
    "Spanish",
    "Sweedish",
    "Tamil",
    "Turkish",
]


def clean_text(text):
    text = re.sub(r'\P{L}', ' ', text)
    text = text.lower()
    return text


def predict_pipeline(text):
    text = clean_text(text)
    pred = model.predict([text])
    return classes[pred[0]]
