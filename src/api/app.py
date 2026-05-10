import streamlit as st
import pandas as pd
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.models.predict import load_model

st.set_page_config(
    page_title="AttritionIQ — HR Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
  html, body, [class*="css"] { font-family: 'Inter', sans-serif !important; }

  .stApp { background: #eef0fb; }
  #MainMenu, footer, header { visibility: hidden; }
  .block-container {
    max-width: 860px !important;
    margin: 0 auto !important;
    padding: 2rem 1.5rem 4rem !important;
  }

  /* ── Hero ── */
  .hero {
    background: linear-gradient(135deg, #3730a3 0%, #6d28d9 100%);
    border-radius: 22px; padding: 2.25rem 2rem 1.75rem;
    margin-bottom: 1.5rem; color: white; text-align: center;
  }
  .hero-badge {
    display: inline-block;
    background: rgba(255,255,255,0.18);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 999px; padding: 0.28rem 1rem;
    font-size: 0.68rem; font-weight: 700;
    letter-spacing: 0.1em; text-transform: uppercase;
    margin-bottom: 0.9rem; color: rgba(255,255,255,0.95);
  }
  .hero h1 {
    font-size: clamp(1.4rem, 4vw, 2rem) !important;
    font-weight: 800 !important; color: #fff !important;
    margin: 0 0 0.4rem !important; line-height: 1.2 !important;
  }
  .hero p { font-size: 0.85rem; color: rgba(255,255,255,0.82); margin: 0; }
  .hero-stats {
    display: flex; justify-content: center;
    gap: clamp(1rem, 4vw, 2.5rem); margin-top: 1.25rem; flex-wrap: wrap;
  }
  .hero-stat-val { font-size: 1.3rem; font-weight: 800; color: #fff; line-height: 1; }
  .hero-stat-lbl {
    font-size: 0.62rem; color: rgba(255,255,255,0.75);
    text-transform: uppercase; letter-spacing: 0.07em; margin-top: 0.15rem;
  }

  /* ── Cards ── */
  .card {
    background: #fff; border-radius: 18px;
    padding: 1.5rem; margin-bottom: 1.1rem;
    border: 1px solid #c7cdf2;
    box-shadow: 0 2px 10px rgba(55,48,163,0.08);
  }
  .card-title {
    font-size: 0.65rem; font-weight: 800;
    text-transform: uppercase; letter-spacing: 0.1em;
    color: #3730a3; margin-bottom: 1.1rem;
  }

  /* ── Sliders ── */
  .stSlider > div > div > div > div { background: #4338ca !important; }
  .stSlider [data-testid="stThumbValue"] { color: #3730a3 !important; font-weight: 700 !important; }
  .stSlider label { color: #111827 !important; font-weight: 600 !important; }

  /* ── Selectbox ── */
  .stSelectbox > div > div {
    background: #eef0fb !important;
    border: 1.5px solid #a5aee8 !important;
    border-radius: 10px !important; color: #111827 !important;
  }
  .stSelectbox > div > div:hover { border-color: #4338ca !important; }
  .stSelectbox label { color: #111827 !important; font-weight: 600 !important; }

  /* ── Radio — pill buttons, dark text ── */
  div[data-testid="stRadio"] > label { display: none !important; }
  div[data-testid="stRadio"] > div {
    display: flex !important; flex-direction: row !important;
    gap: 0.5rem !important; flex-wrap: wrap !important;
  }
  div[data-testid="stRadio"] > div > label {
    background: #dde1f8 !important;
    border: 1.5px solid #a5aee8 !important;
    border-radius: 10px !important;
    padding: 0.45rem 1.3rem !important;
    color: #1e1660 !important;
    font-size: 0.86rem !important; font-weight: 700 !important;
    cursor: pointer !important; transition: all 0.15s !important; margin: 0 !important;
  }
  div[data-testid="stRadio"] > div > label:hover {
    border-color: #4338ca !important; background: #c7cdf2 !important; color: #1e1660 !important;
  }
  div[data-testid="stRadio"] > div > label:has(input:checked) {
    background: #4338ca !important; border-color: #3730a3 !important; color: #fff !important;
  }

  /* ── All labels dark ── */
  label { color: #111827 !important; font-size: 0.84rem !important; font-weight: 600 !important; }
  p { color: #1f2937 !important; }
  .stMarkdown p { color: #1f2937 !important; }

  /* ── Metric cards ── */
  div[data-testid="metric-container"] {
    background: #eef0fb !important;
    border: 1.5px solid #a5aee8 !important;
    border-radius: 12px !important; padding: 0.85rem 0.75rem !important;
  }
  div[data-testid="metric-container"] label {
    color: #3730a3 !important; font-size: 0.62rem !important;
    font-weight: 800 !important; text-transform: uppercase !important; letter-spacing: 0.07em !important;
  }
  div[data-testid="metric-container"] div[data-testid="metric-value"] {
    color: #111827 !important; font-size: 1.2rem !important; font-weight: 800 !important;
  }

  /* ── Button ── */
  div.stButton > button {
    background: linear-gradient(135deg, #3730a3, #6d28d9) !important;
    color: #fff !important; border: none !important;
    border-radius: 12px !important; padding: 0.8rem 2rem !important;
    font-size: 0.95rem !important; font-weight: 700 !important; width: 100% !important;
    box-shadow: 0 4px 18px rgba(55,48,163,0.35) !important; transition: all 0.2s !important;
  }
  div.stButton > button:hover {
    box-shadow: 0 8px 24px rgba(55,48,163,0.5) !important; transform: translateY(-1px) !important;
  }

  /* ── Result boxes ── */
  .result-box { border-radius: 18px; padding: 1.75rem 1.5rem; text-align: center; margin-bottom: 1.1rem; }
  .result-high { background: #fee2e2; border: 2px solid #f87171; }
  .result-low  { background: #dcfce7; border: 2px solid #4ade80; }
  .result-score { font-size: clamp(2.8rem, 10vw, 4.5rem); font-weight: 900; line-height: 1; margin: 0.4rem 0; }
  .result-title { font-size: clamp(0.95rem, 3vw, 1.2rem); font-weight: 700; margin-bottom: 0.3rem; }
  .result-sub   { font-size: 0.85rem; max-width: 340px; margin: 0 auto; line-height: 1.55; font-weight: 500; }

  .rpill { display:inline-block; padding:0.3rem 1.1rem; border-radius:999px; font-size:0.68rem; font-weight:800; letter-spacing:0.08em; text-transform:uppercase; margin-top:0.65rem; }
  .rpill-critical { background:#7f1d1d; color:#fff; border:1.5px solid #b91c1c; }
  .rpill-high     { background:#7c2d12; color:#fff; border:1.5px solid #c2410c; }
  .rpill-moderate { background:#713f12; color:#fff; border:1.5px solid #b45309; }
  .rpill-low      { background:#14532d; color:#fff; border:1.5px solid #15803d; }

  .bar-wrap { background:#c7cdf2; border-radius:999px; height:9px; overflow:hidden; margin:1rem auto 0.3rem; max-width:300px; }
  .bar-fill { height:100%; border-radius:999px; }

  /* ── Factor chips ── */
  .fgrid { display:grid; grid-template-columns:repeat(auto-fit,minmax(130px,1fr)); gap:0.65rem; margin-top:0.75rem; }
  .fchip { background:#eef0fb; border:1.5px solid #a5aee8; border-radius:12px; padding:0.8rem 0.6rem; text-align:center; }
  .fchip-val { font-size:1.15rem; font-weight:800; line-height:1; margin-bottom:0.15rem; }
  .fchip-lbl { font-size:0.62rem; color:#374151; text-transform:uppercase; letter-spacing:0.05em; font-weight:700; }
  .fchip-tag { font-size:0.62rem; font-weight:700; margin-top:0.25rem; padding:0.12rem 0.5rem; border-radius:999px; display:inline-block; }
  .tg { background:#14532d; color:#fff; }
  .tw { background:#713f12; color:#fff; }
  .tb { background:#7f1d1d; color:#fff; }

  /* ── Section label ── */
  .slabel { font-size:0.84rem; font-weight:700; color:#111827; margin:0.7rem 0 0.35rem; }

  /* ── Footer ── */
  .ft { text-align:center; font-size:0.72rem; color:#374151; padding-top:1.5rem; font-weight:500; }
  .ft a { color:#3730a3; text-decoration:none; font-weight:700; }

  /* ── Mobile ── */
  @media (max-width:600px) {
    .block-container { padding: 1rem 0.75rem 3rem !important; }
    .hero { padding: 1.5rem 1rem 1.25rem; border-radius: 16px; }
    .card { padding: 1.1rem 0.9rem; border-radius: 14px; }
  }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# ── Hero ───────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">HR Analytics Platform</div>
  <h1>Employee Attrition Predictor</h1>
  <p>Fill in the employee profile below to predict attrition risk instantly.</p>
  <div class="hero-stats">
    <div><div class="hero-stat-val">99%</div><div class="hero-stat-lbl">Accuracy</div></div>
    <div><div class="hero-stat-val">98.9%</div><div class="hero-stat-lbl">ROC-AUC</div></div>
    <div><div class="hero-stat-val">15K+</div><div class="hero-stat-lbl">Records</div></div>
    <div><div class="hero-stat-val">RF</div><div class="hero-stat-lbl">Algorithm</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Performance Signals ────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">📊 Performance Signals</div>', unsafe_allow_html=True)
col_a, col_b = st.columns(2, gap="large")
with col_a:
    satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5, step=0.01,
        help="0 = very dissatisfied · 1 = very satisfied")
    number_project = st.slider("Number of Projects", 1, 10, 3)
    time_spend_company = st.slider("Years at Company", 1, 10, 3)
with col_b:
    last_evaluation = st.slider("Last Evaluation Score", 0.0, 1.0, 0.5, step=0.01)
    average_montly_hours = st.slider("Average Monthly Hours", 50, 350, 200, step=5)
st.markdown('</div>', unsafe_allow_html=True)

# ── HR Factors ─────────────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">🏢 HR Factors</div>', unsafe_allow_html=True)
col_c, col_d = st.columns(2, gap="large")
with col_c:
    Work_accident = st.selectbox("Work Accident", options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes")
    st.markdown('<div class="slabel">Salary Level</div>', unsafe_allow_html=True)
    salary_option = st.radio("Salary Level", options=["Low", "Medium", "High"],
        horizontal=True, label_visibility="collapsed")
with col_d:
    promotion_last_5years = st.selectbox("Promotion in Last 5 Years", options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes")
    st.markdown('<div class="slabel">Department</div>', unsafe_allow_html=True)
    department = st.selectbox("Department",
        options=["Sales","Technical","Support","HR","Accounting","Management","R&D","Marketing","Product Management"],
        label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

salary_low    = 1 if salary_option == "Low"    else 0
salary_medium = 1 if salary_option == "Medium" else 0

dept_map = {
    "Sales":"Department_sales","Technical":"Department_technical","Support":"Department_support",
    "HR":"Department_hr","Accounting":"Department_accounting","Management":"Department_management",
    "R&D":"Department_RandD","Marketing":"Department_marketing","Product Management":"Department_product_mng",
}
dept_cols = {k: 0 for k in [
    "Department_RandD","Department_accounting","Department_hr","Department_management",
    "Department_marketing","Department_product_mng","Department_sales","Department_support","Department_technical",
]}
dept_cols[dept_map[department]] = 1

# ── Profile Summary ────────────────────────────────────────────────────────────
st.markdown('<div class="card"><div class="card-title">📋 Live Profile Summary</div>', unsafe_allow_html=True)
m1, m2, m3, m4, m5 = st.columns(5)
m1.metric("Satisfaction",  f"{satisfaction_level:.2f}")
m2.metric("Evaluation",    f"{last_evaluation:.2f}")
m3.metric("Projects",      number_project)
m4.metric("Avg Hours",     average_montly_hours)
m5.metric("Years",         time_spend_company)
st.markdown('</div>', unsafe_allow_html=True)

# ── DataFrame ──────────────────────────────────────────────────────────────────
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

# ── Predict ────────────────────────────────────────────────────────────────────
predict_clicked = st.button("🔍  Analyse Attrition Risk")

if predict_clicked:
    prediction  = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    pct         = round(probability * 100, 1)
    retain_pct  = round((1 - probability) * 100, 1)

    risk_level = (
        "Critical" if probability > 0.75 else
        "High"     if probability > 0.50 else
        "Moderate" if probability > 0.25 else
        "Low"
    )

    if prediction == 1:
        sc, bc = "#991b1b", "#ef4444"
        box, title = "result-high result-box", "⚠️ Attrition Risk Detected"
        sub = f"This employee has a {pct}% probability of leaving. Review workload, satisfaction, and career growth."
        tc, sc2 = "#7f1d1d", "#991b1b"
        rpill = f"rpill-{risk_level.lower()}"
    else:
        sc, bc = "#14532d", "#22c55e"
        box, title = "result-low result-box", "✅ Employee Likely to Stay"
        sub = f"This employee has a {retain_pct}% likelihood of staying. Continue current engagement practices."
        tc, sc2 = "#14532d", "#166534"
        rpill = "rpill-low"

    st.markdown(f"""
    <div class="{box}">
      <div class="result-title" style="color:{tc};">{title}</div>
      <div class="result-score" style="color:{sc};">{pct}%</div>
      <div class="result-sub"   style="color:{sc2};">{sub}</div>
      <div><span class="rpill {rpill}">{risk_level} Risk</span></div>
      <div class="bar-wrap">
        <div class="bar-fill" style="width:{pct}%;background:{bc};"></div>
      </div>
      <div style="font-size:0.72rem;color:{sc};font-weight:600;margin-top:0.2rem;">
        Attrition probability · {pct}%
      </div>
    </div>
    """, unsafe_allow_html=True)

    sat_t = ("tg","Healthy")     if satisfaction_level > 0.6   else ("tw","Moderate")   if satisfaction_level > 0.3 else ("tb","Risk Factor")
    hrs_t = ("tb","Overloaded")  if average_montly_hours > 270  else ("tw","Heavy Load") if average_montly_hours > 220 else ("tg","Healthy")
    prj_t = ("tb","Too Many")    if number_project > 6          else ("tw","High Load")  if number_project > 4        else ("tg","Balanced")
    evl_t = ("tg","Strong")      if last_evaluation > 0.7       else ("tw","Average")    if last_evaluation > 0.4     else ("tb","Needs Review")
    yr_t  = ("tw","Tenure Risk") if time_spend_company in [4,5] else ("tg","Stable")
    prm_t = ("tb","No Promotion") if not promotion_last_5years and time_spend_company >= 4 else ("tg","Promoted")

    def chip(val, lbl, tc, tt):
        color = "#991b1b" if tc=="tb" else "#713f12" if tc=="tw" else "#14532d"
        return f'<div class="fchip"><div class="fchip-val" style="color:{color};">{val}</div><div class="fchip-lbl">{lbl}</div><div class="fchip-tag {tc}">{tt}</div></div>'

    st.markdown(f"""
    <div class="card" style="margin-top:1.1rem;">
      <div class="card-title">💡 Key Factor Analysis</div>
      <div class="fgrid">
        {chip(f"{satisfaction_level:.2f}", "Satisfaction",   sat_t[0], sat_t[1])}
        {chip(average_montly_hours,        "Monthly Hrs",    hrs_t[0], hrs_t[1])}
        {chip(number_project,              "Projects",       prj_t[0], prj_t[1])}
        {chip(f"{last_evaluation:.2f}",    "Evaluation",     evl_t[0], evl_t[1])}
        {chip(f"{time_spend_company}yr",   "Tenure",         yr_t[0],  yr_t[1])}
        {chip("Yes" if promotion_last_5years else "No", "Promoted", prm_t[0], prm_t[1])}
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="ft">
  Built by <a href="https://github.com/aroraneel" target="_blank">Neel Arora</a> &nbsp;·&nbsp;
  Random Forest &nbsp;·&nbsp; 99% Accuracy &nbsp;·&nbsp; 98.9% ROC-AUC
</div>
""", unsafe_allow_html=True)