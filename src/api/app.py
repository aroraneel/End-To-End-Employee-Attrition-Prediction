import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Ensure project root is in path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.models.predict import load_model

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="🚀",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0a0a0f; color: #e8e6f0; }

    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #12121a; }

    /* Headers */
    h1, h2, h3 { font-family: 'Segoe UI', sans-serif; color: #ffffff !important; }

    /* Metric cards */
    div[data-testid="metric-container"] {
        background: #12121a;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 12px;
        padding: 1rem;
    }

    /* Sliders */
    .stSlider > div > div > div { background: #7c6fff !important; }

    /* Select boxes */
    .stSelectbox > div > div {
        background: #12121a !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #e8e6f0 !important;
        border-radius: 8px;
    }

    /* Predict button */
    div.stButton > button {
        background: linear-gradient(135deg, #7c6fff, #a855f7);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 16px;
        font-weight: 700;
        width: 100%;
        transition: opacity 0.2s;
    }
    div.stButton > button:hover { opacity: 0.9; }

    /* Section dividers */
    hr { border-color: rgba(255,255,255,0.07); }

    /* Label text */
    label, .stMarkdown p { color: #9896b0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────────────────────
@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# ── Title ─────────────────────────────────────────────────────────────────────
st.title("🚀 Employee Attrition Predictor")
st.markdown("---")

# ── Input layout ──────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Performance Signals")
    satisfaction_level = st.slider(
        "Satisfaction Level", 0.0, 1.0, 0.5, step=0.01,
        help="Employee self-reported satisfaction (0 = very dissatisfied, 1 = very satisfied)"
    )
    last_evaluation = st.slider(
        "Last Evaluation Score", 0.0, 1.0, 0.5, step=0.01,
        help="Most recent performance review score"
    )
    number_project = st.slider(
        "Number of Projects", 1, 10, 3,
        help="Total number of projects the employee is involved in"
    )
    average_montly_hours = st.slider(
        "Average Monthly Hours", 50, 350, 200, step=5,
        help="Average hours worked per month"
    )
    time_spend_company = st.slider(
        "Years at Company", 1, 10, 3,
        help="Number of years the employee has been with the company"
    )

with col2:
    st.subheader("🏢 HR Factors")
    Work_accident = st.selectbox(
        "Work Accident",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
        help="Whether the employee had a workplace accident"
    )
    promotion_last_5years = st.selectbox(
        "Promotion in Last 5 Years",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes",
        help="Whether the employee was promoted in the last 5 years"
    )

    st.markdown("**Salary Level**")
    salary_option = st.radio(
        "Salary Level",
        options=["Low", "Medium", "High"],
        horizontal=True,
        label_visibility="collapsed",
    )
    salary_low    = 1 if salary_option == "Low"    else 0
    salary_medium = 1 if salary_option == "Medium" else 0

    st.markdown("**Department**")
    department = st.selectbox(
        "Department",
        options=[
            "Sales", "Technical", "Support", "HR",
            "Accounting", "Management", "R&D",
            "Marketing", "Product Management"
        ],
        label_visibility="collapsed",
    )

    dept_map = {
        "Sales":              "Department_sales",
        "Technical":          "Department_technical",
        "Support":            "Department_support",
        "HR":                 "Department_hr",
        "Accounting":         "Department_accounting",
        "Management":         "Department_management",
        "R&D":                "Department_RandD",
        "Marketing":          "Department_marketing",
        "Product Management": "Department_product_mng",
    }
    dept_cols = {
        "Department_RandD":       0,
        "Department_accounting":  0,
        "Department_hr":          0,
        "Department_management":  0,
        "Department_marketing":   0,
        "Department_product_mng": 0,
        "Department_sales":       0,
        "Department_support":     0,
        "Department_technical":   0,
    }
    dept_cols[dept_map[department]] = 1

# ── Live summary metrics ───────────────────────────────────────────────────────
st.markdown("---")
st.subheader("📋 Profile Summary")

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Satisfaction",    f"{satisfaction_level:.2f}")
m2.metric("Evaluation",      f"{last_evaluation:.2f}")
m3.metric("Projects",        number_project)
m4.metric("Monthly Hours",   average_montly_hours)
m5.metric("Years",           time_spend_company)

# ── Build input DataFrame ──────────────────────────────────────────────────────
input_data = pd.DataFrame({
    "satisfaction_level":    [satisfaction_level],
    "last_evaluation":       [last_evaluation],
    "number_project":        [number_project],
    "average_montly_hours":  [average_montly_hours],
    "time_spend_company":    [time_spend_company],
    "Work_accident":         [Work_accident],
    "promotion_last_5years": [promotion_last_5years],
    **{k: [v] for k, v in dept_cols.items()},
    "salary_low":            [salary_low],
    "salary_medium":         [salary_medium],
})

# ── Prediction ─────────────────────────────────────────────────────────────────
st.markdown("---")
_, btn_col, _ = st.columns([1, 2, 1])

with btn_col:
    predict_clicked = st.button("🔍 Predict Attrition Risk")

if predict_clicked:
    prediction  = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("---")
    res_col1, res_col2 = st.columns([2, 1])

    with res_col1:
        if prediction == 1:
            st.error(f"### ⚠️ High Attrition Risk\n**Probability: {probability*100:.1f}%**")
            st.markdown(
                f"This employee has a **{probability*100:.1f}% chance** of leaving. "
                "Review workload, satisfaction drivers, and career growth opportunities."
            )
        else:
            st.success(f"### ✅ Low Attrition Risk\n**Retention Confidence: {(1-probability)*100:.1f}%**")
            st.markdown(
                f"This employee has a **{(1-probability)*100:.1f}% likelihood** of staying. "
                "Continue current engagement practices to maintain this positive outlook."
            )

    with res_col2:
        st.metric(
            label="Risk Score",
            value=f"{probability*100:.1f}%",
            delta=f"{'↑ At Risk' if prediction == 1 else '↓ Retained'}",
            delta_color="inverse",
        )
        risk_level = (
            "Critical" if probability > 0.75 else
            "High"     if probability > 0.50 else
            "Moderate" if probability > 0.25 else
            "Low"
        )
        st.info(f"**Risk Level:** {risk_level}")