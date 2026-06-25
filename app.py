import streamlit as st
import joblib
import numpy as np

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------

model = joblib.load("loan_prediction_model.pkl")

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

.main {
    background-color: #f4f7fc;
}

.hero {
    background: linear-gradient(135deg, #1e3c72, #2a5298);
    padding: 2rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.15);
}

.metric-card h3{
    color:#1e3c72;
}

.metric-card p{
    color:#444444;
}

.result-success {
    background: #d4edda;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: #155724;
    font-size: 24px;
    font-weight: bold;
}

.result-fail {
    background: #f8d7da;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: #721c24;
    font-size: 24px;
    font-weight: bold;
}

.stButton > button {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown("""
<div class="hero">
    <h1>🏦 Smart Loan Approval Prediction System</h1>
    <p>Machine Learning Powered Loan Eligibility Assessment</p>
</div>
""", unsafe_allow_html=True)

# ---------------- METRICS ----------------

m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class="metric-card">
        <h3>⚡ Fast Analysis</h3>
        <p>Instant Prediction</p>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="metric-card">
        <h3>🤖 AI Powered</h3>
        <p>SVM Model</p>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="metric-card">
        <h3>🔒 Secure</h3>
        <p>Private Processing</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- FORM ----------------

left, right = st.columns(2)

with left:

    st.subheader("Applicant Information")

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "Marital Status",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "Dependents",
        [0, 1, 2, 3, 4]
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes", "No"]
    )

with right:

    st.subheader("Financial Information")

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0,
        value=5000
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0,
        value=0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=120
    )

    loan_term = st.number_input(
        "Loan Amount Term",
        min_value=0,
        value=360
    )

    credit_history = st.selectbox(
        "Credit History",
        [1, 0]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Rural", "Semiurban", "Urban"]
    )

# ---------------- ENCODING ----------------

gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

property_area = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}[property_area]

# ---------------- PREDICTION ----------------

if st.button("Predict Loan Status"):

    features = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    prediction = model.predict(features)

    st.write("")

    if prediction[0] == 1:

        st.balloons()

        st.markdown("""
        <div class="result-success">
            ✅ LOAN APPROVED
        </div>
        """, unsafe_allow_html=True)

    else:

        st.markdown("""
        <div class="result-fail">
            ❌ LOAN REJECTED
        </div>
        """, unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

st.sidebar.title("Loan Predictor")

st.sidebar.info(
    "This application uses a Machine Learning SVM model "
    "to predict whether a loan application is likely "
    "to be approved or rejected."
)

st.sidebar.success("System Ready")