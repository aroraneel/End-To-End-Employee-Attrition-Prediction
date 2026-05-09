import pandas as pd

from src.models.predict import load_model, predict
from src.utils.logger import logging


def run_inference(input_data: dict) -> dict:
    """
    Run end-to-end inference for a single employee record.

    Parameters
    ----------
    input_data : dict
        Raw feature values keyed by column name.

    Returns
    -------
    dict with keys:
        - prediction  : int  (0 = Stayed, 1 = Left)
        - probability : float  (probability of attrition)
        - risk_level  : str   (Low / Moderate / High / Critical)
    """
    logging.info("Starting inference pipeline")

    # ── Load model ───────────────────────────────────────────────────────────
    model = load_model()
    logging.info("Model loaded successfully")

    # ── Build DataFrame ──────────────────────────────────────────────────────
    df = pd.DataFrame([input_data])

    # ── Predict ──────────────────────────────────────────────────────────────
    prediction, proba = predict(model, df)
    attrition_prob = float(proba[0][1])

    # ── Risk label ───────────────────────────────────────────────────────────
    if attrition_prob > 0.75:
        risk_level = "Critical"
    elif attrition_prob > 0.50:
        risk_level = "High"
    elif attrition_prob > 0.25:
        risk_level = "Moderate"
    else:
        risk_level = "Low"

    result = {
        "prediction": int(prediction[0]),
        "probability": round(attrition_prob, 4),
        "risk_level": risk_level,
    }

    logging.info(
        "Inference complete — prediction: %d, probability: %.4f, risk: %s",
        result["prediction"],
        result["probability"],
        result["risk_level"],
    )

    return result


if __name__ == "__main__":
    # Example usage
    sample = {
        "satisfaction_level": 0.4,
        "last_evaluation": 0.6,
        "number_project": 3,
        "average_montly_hours": 220,
        "time_spend_company": 4,
        "Work_accident": 0,
        "promotion_last_5years": 0,
        "Department_RandD": 0,
        "Department_accounting": 0,
        "Department_hr": 0,
        "Department_management": 0,
        "Department_marketing": 0,
        "Department_product_mng": 0,
        "Department_sales": 1,
        "Department_support": 0,
        "Department_technical": 0,
        "salary_low": 1,
        "salary_medium": 0,
    }
    result = run_inference(sample)
    print(result)
