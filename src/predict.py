import joblib

def load_model():
    return joblib.load("models/model.pkl")

def predict(model, input_data):
    prediction = model.predict(input_data)
    proba = model.predict_proba(input_data)
    return prediction, proba
