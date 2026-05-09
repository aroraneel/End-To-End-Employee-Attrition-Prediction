import joblib

from src.config.config import MODEL_PATH


def load_model():
    return joblib.load(MODEL_PATH)


def predict(model, input_data):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)
    return prediction, proba
