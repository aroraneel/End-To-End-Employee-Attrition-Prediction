import os

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix,
)

from src.config.config import DATA_PATH, MODEL_PATH
from src.utils.logger import logging


def train_model():
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    # ── Load & preprocess ────────────────────────────────────────────────────
    df = pd.read_csv(DATA_PATH)
    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("left", axis=1)
    y = df["left"]

    # ── Train / test split ───────────────────────────────────────────────────
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    logging.info(
        "Data split — train: %d rows, test: %d rows", len(X_train), len(X_test)
    )

    # ── Train ────────────────────────────────────────────────────────────────
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    logging.info("Model training complete")

    # ── Evaluate ─────────────────────────────────────────────────────────────
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_proba)

    logging.info("Accuracy : %.4f", acc)
    logging.info("F1 Score : %.4f", f1)
    logging.info("ROC-AUC  : %.4f", auc)

    print("\n===== Model Evaluation =====")
    print(f"Accuracy : {acc:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC-AUC  : {auc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=["Stayed", "Left"]))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("============================\n")

    # ── Save ─────────────────────────────────────────────────────────────────
    joblib.dump(model, MODEL_PATH)
    logging.info("Model saved at %s", MODEL_PATH)

    return model


if __name__ == "__main__":
    train_model()
