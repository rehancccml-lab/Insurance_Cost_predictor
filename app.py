
import streamlit as st
import pandas as pd
import joblib

# Load saved files
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# Page configuration
st.set_page_config(
    page_title="Medical Insurance Cost Prediction",
    page_icon="💙",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Center prediction button with 50px top margin */
div.st-key-predict_btn {
    display: flex;
    justify-content: center;
    margin-top: 50px;
}

div.st-key-predict_btn .stButton {
    width: auto;
}

div.st-key-predict_btn .stButton > button {
    width: 250px;
}

/* Main background */
.stApp {
    background-color: #000000;
    color: white;
}

/* Neon blue border around page */
.block-container {
    border: 2px solid #00bfff;
    border-radius: 20px;
    box-shadow:
        0 0 15px #00bfff,
        0 0 35px #0077ff,
        inset 0 0 15px #003cff;
    padding: 35px;
    margin-top: 25px;
    max-width: 1400px;
}

/* Main heading */
.main-title {
    color: #ff2020;
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    text-shadow:
        2px 2px 5px #90ee90,
        0 0 15px #90ee90;
    margin-bottom: 35px;
}

/* Section headings */
.section-title {
    color: #00d9ff;
    font-size: 26px;
    font-weight: bold;
    text-shadow: 0 0 10px #00bfff;
    margin-bottom: 20px;
}

/* Input labels */
.stNumberInput label,
.stSelectbox label {
    color: white !important;
    font-size: 17px;
    font-weight: bold;
}

/* Input boxes */
.stNumberInput input {
    background-color: #101827;
    color: white;
    border: 1px solid #00bfff;
    border-radius: 10px;
    box-shadow: 0 0 8px #0077ff;
}

/* Dropdowns */
div[data-baseweb="select"] > div {
    background-color: #101827;
    border: 1px solid #00bfff;
    border-radius: 10px;
    box-shadow: 0 0 8px #0077ff;
}

/* Prediction button */
.stButton > button {
    background-color: #000000;
    color: #00d9ff;
    border: 2px solid #00bfff;
    border-radius: 12px;
    font-size: 20px;
    font-weight: bold;
    padding: 12px 30px;
    box-shadow: 0 0 15px #00bfff;
    width: 100%;
}

.stButton > button:hover {
    background-color: #00bfff;
    color: black;
    box-shadow: 0 0 30px #00bfff;
}

/* Prediction result box */
.result-box {
    background-color: #08121f;
    border: 2px solid #00bfff;
    border-radius: 18px;
    padding: 35px;
    text-align: center;
    box-shadow:
        0 0 20px #00bfff,
        inset 0 0 12px #004cff;
    margin-top: 30px;
}

/* Result amount */
.result-amount {
    color: #90ee90;
    font-size: 40px;
    font-weight: bold;
    text-shadow: 0 0 15px #90ee90;
}

/* Vertical divider */
div[data-testid="column"]:first-child {
    border-right: 2px solid #00bfff;
    padding-right: 30px;
}

div[data-testid="column"]:last-child {
    padding-left: 30px;
}

</style>
""", unsafe_allow_html=True)

# Main heading
st.markdown(
    '<h1 class="main-title">Medical Insurance Cost Prediction</h1>',
    unsafe_allow_html=True
)

# Two equal columns
left, right = st.columns(2, gap="large")

# LEFT SIDE - INPUTS
with left:

    st.markdown(
        '<div class="section-title">Patient Information</div>',
        unsafe_allow_html=True
    )

    age = st.number_input("Age", 18, 100, 30)

    sex = st.selectbox("Sex", ["male", "female"])

    bmi = st.number_input("BMI", 10.0, 60.0, 25.0)

    children = st.number_input("Children", 0, 10, 0)

    smoker = st.selectbox("Smoker", ["yes", "no"])

    region = st.selectbox(
        "Region",
        ["southwest", "southeast", "northwest", "northeast"]
    )

    


with right:

    


    st.markdown(
        '<div class="section-title">Prediction Result</div>',
        unsafe_allow_html=True
    )

    
    result = st.empty()

    
    predict = st.button("Predict Insurance Cost", key="predict_btn")

    if predict:

        data = pd.DataFrame(0, index=[0], columns=columns)

        data["age"] = age
        data["bmi"] = bmi
        data["children"] = children

        for col in [f"sex_{sex}", f"smoker_{smoker}", f"region_{region}"]:
            if col in data.columns:
                data[col] = 1

        data = scaler.transform(data)

        prediction = model.predict(data)

        result.markdown(f"""
        <div class="result-box">
            <h2 style="color:white;">
                Estimated Insurance Cost
            </h2>
            <div class="result-amount">
                ${prediction[0]:,.2f}
            </div>
            <p style="color:#00d9ff;">
                Prediction Completed Successfully
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:

        result.markdown("""
        <div class="result-box">
            <h2 style="color:#00d9ff;">
                Awaiting Prediction
            </h2>
            <p style="color:white;">
                Enter patient details on the left
                and click Predict Insurance Cost.
            </p>
        </div>
        """, unsafe_allow_html=True)
