import streamlit as st
import pandas as pd
import sys
from pathlib import Path

# Ensure project root is in path for imports
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.predict import load_model

# Load model
model = load_model()

st.title("🚀 Employee Attrition Predictor")

# Input fields
col1, col2 = st.columns(2)

with col1:
    satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
    last_evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5)
    number_project = st.slider("Number of Projects", 1, 10, 3)
    average_montly_hours = st.slider("Average Monthly Hours", 50, 350, 200)
    time_spend_company = st.slider("Years at Company", 1, 10, 3)

with col2:
    Work_accident = st.selectbox("Work Accident", [0, 1])
    promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])
    salary_low = st.selectbox("Low Salary", [0, 1])
    salary_medium = st.selectbox("Medium Salary", [0, 1])

st.subheader("Department")
dept_col1, dept_col2, dept_col3 = st.columns(3)
with dept_col1:
    Department_RandD = st.selectbox("R&D", [0, 1])
    Department_accounting = st.selectbox("Accounting", [0, 1])
    Department_hr = st.selectbox("HR", [0, 1])
with dept_col2:
    Department_management = st.selectbox("Management", [0, 1])
    Department_marketing = st.selectbox("Marketing", [0, 1])
    Department_product_mng = st.selectbox("Product Management", [0, 1])
with dept_col3:
    Department_sales = st.selectbox("Sales", [0, 1])
    Department_support = st.selectbox("Support", [0, 1])
    Department_technical = st.selectbox("Technical", [0, 1])

# Create input data
input_data = pd.DataFrame({
    'satisfaction_level': [satisfaction_level],
    'last_evaluation': [last_evaluation],
    'number_project': [number_project],
    'average_montly_hours': [average_montly_hours],
    'time_spend_company': [time_spend_company],
    'Work_accident': [Work_accident],
    'promotion_last_5years': [promotion_last_5years],
    'Department_RandD': [Department_RandD],
    'Department_accounting': [Department_accounting],
    'Department_hr': [Department_hr],
    'Department_management': [Department_management],
    'Department_marketing': [Department_marketing],
    'Department_product_mng': [Department_product_mng],
    'Department_sales': [Department_sales],
    'Department_support': [Department_support],
    'Department_technical': [Department_technical],
    'salary_low': [salary_low],
    'salary_medium': [salary_medium]
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ Attrition Risk: {probability*100:.2f}%")
    else:
        st.success(f"✅ Retention Confidence: {(1-probability)*100:.2f}%")
