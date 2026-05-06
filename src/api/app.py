
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/artifacts/model.pkl")

# Page Config
st.set_page_config(
    page_title="AI Employee Attrition Predictor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #111827, #1e1b4b);
    color: white;
}

/* Title Styling */
.main-title {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(to right, #38bdf8, #818cf8, #ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5e1;
    margin-bottom: 40px;
}

/* Glassmorphism Cards */
.glass {
    background: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}

/* Buttons */
.stButton>button {
    width: 100%;
    background: linear-gradient(to right, #06b6d4, #8b5cf6, #ec4899);
    color: white;
    border: none;
    border-radius: 14px;
    height: 60px;
    font-size: 22px;
    font-weight: bold;
    transition: 0.3s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 20px rgba(236,72,153,0.7);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111827, #1e293b);
}

/* Metrics */
.metric-box {
    background: linear-gradient(135deg, #1d4ed8, #7c3aed);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    box-shadow: 0 6px 20px rgba(0,0,0,0.3);
}

/* Slider Label */
label {
    color: white !important;
    font-weight: 600 !important;
}

</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("<div class='main-title'>🚀 AI Employee Attrition Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Predict employee turnover risk using Machine Learning & HR Analytics</div>", unsafe_allow_html=True)

# Top Metrics
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class='metric-box'>
        <h2>⚡ Model</h2>
        <h1>Random Forest</h1>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class='metric-box'>
        <h2>📊 Prediction</h2>
        <h1>Real-Time</h1>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class='metric-box'>
        <h2>🤖 Accuracy</h2>
        <h1>ML Powered</h1>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")

# Main Layout
left, right = st.columns([2, 1])

# LEFT SECTION
with left:

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("👨 Employee Performance Information")

    satisfaction_level = st.slider(
        "Satisfaction Level",
        0.0, 1.0, 0.5
    )

    last_evaluation = st.slider(
        "Last Evaluation Score",
        0.0, 1.0, 0.5
    )

    number_project = st.slider(
        "Number of Projects",
        1, 10, 3
    )

    average_montly_hours = st.slider(
        "Average Monthly Hours",
        50, 350, 200
    )

    time_spend_company = st.slider(
        "Years at Company",
        1, 10, 3
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("🏢 Company & Department Information")

    col1, col2 = st.columns(2)

    with col1:

        Work_accident = st.selectbox(
            "Work Accident",
            [0, 1]
        )

        promotion_last_5years = st.selectbox(
            "Promotion in Last 5 Years",
            [0, 1]
        )

        salary_low = st.selectbox(
            "Low Salary",
            [0, 1]
        )

        salary_medium = st.selectbox(
            "Medium Salary",
            [0, 1]
        )

    with col2:

        Department_RandD = st.selectbox("R&D", [0, 1])
        Department_accounting = st.selectbox("Accounting", [0, 1])
        Department_hr = st.selectbox("HR", [0, 1])
        Department_management = st.selectbox("Management", [0, 1])
        Department_marketing = st.selectbox("Marketing", [0, 1])
        Department_product_mng = st.selectbox("Product Management", [0, 1])
        Department_sales = st.selectbox("Sales", [0, 1])
        Department_support = st.selectbox("Support", [0, 1])
        Department_technical = st.selectbox("Technical", [0, 1])

    st.markdown("</div>", unsafe_allow_html=True)

# RIGHT SECTION
with right:

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("📈 HR Insights")

    st.info("✔ Higher overtime and low satisfaction can increase attrition risk.")
    st.warning("⚠ Long working hours may impact employee retention.")
    st.success("✅ Promotions improve retention probability.")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.subheader("🤖 AI Prediction Engine")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/4712/4712109.png",
        width=180
    )

    st.markdown("</div>", unsafe_allow_html=True)

# Input Data
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

st.write("")

# Prediction Button
if st.button("🚀 Predict Employee Attrition"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.write("")
    st.write("---")

    if prediction == 1:

        st.error("⚠ Employee is likely to leave the company")

        st.progress(float(probability))

        st.markdown(f"""
        <div class='glass'>
            <h2 style='color:#f87171;'>🔥 Attrition Risk Score</h2>
            <h1>{probability*100:.2f}%</h1>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.success("✅ Employee is likely to stay in the company")

        st.progress(float(1 - probability))

        st.markdown(f"""
        <div class='glass'>
            <h2 style='color:#4ade80;'>🎯 Retention Confidence</h2>
            <h1>{(1-probability)*100:.2f}%</h1>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.write("---")

st.markdown(
    """
    <center>
        <h4 style='color:#94a3b8;'>Built with ❤️ using Streamlit, Machine Learning & Random Forest</h4>
    </center>
    """,
    unsafe_allow_html=True
)

