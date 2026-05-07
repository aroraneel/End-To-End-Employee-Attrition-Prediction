import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

from src.config.config import DATA_PATH, MODEL_PATH
from src.utils.logger import logging


def train_model():
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    df = pd.read_csv(DATA_PATH)
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("left", axis=1)
    y = df["left"]

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    logging.info("Model trained and saved at %s", MODEL_PATH)


if __name__ == "__main__":
    train_model()
