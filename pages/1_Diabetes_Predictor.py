import pickle 
import numpy as np
import streamlit as st 

st.set_page_config(page_title="Diabetes Prediction System", layout="wide") 

st.markdown(
    """
    <style>
    /* ---------- HEADER ---------- */
    .header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 110px;                 /* Reduced height */
        padding-top: 52px;
        background-color: #08f1e4;
        color: white;
        z-index: 1000;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .header-title {
        font-size: 28px;
        font-weight: 900;        
        color: black;
    }

    /* ---------- MAIN APP OFFSET ---------- */
    .stApp {
        margin-top: 110px;            /* Push content below header */
        padding-bottom: 70px;         /* Avoid footer overlap */
    }

    /* ---------- FOOTER ---------- */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 42px;
        background-color: #08f1e4;
        color: black;
        text-align: center;
        padding-top: 10px;
        font-size: 14px;
        z-index: 1000;
    }
    </style>

    <!-- HEADER -->
    <div class="header">
        <div class="header-title">
            Diabetes Prediction System
        </div>
    </div>

    <!-- FOOTER -->
    <div class="footer">
        Developed by Sarvesh Vengurlekar
    </div>
    """,
    unsafe_allow_html=True
)


st.header("Diabetes Predictor Model")
st.subheader("Enter the following parameters to Predict Diabetes :", divider=True)

#model loading
with open('model/diabetes_predict.pkl', 'rb') as f:
    model = pickle.load(f)

col1, col2 = st.columns(2)

#input param
with col1:
    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose (mg/dL)", 50, 300, 100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", 30, 150, 70)
    skin_thickness = st.number_input("Skin Thickness (mm)", 0, 100, 20)

with col2:
    insulin = st.number_input("Insulin Level (µU/mL)", 0, 900, 80)
    bmi = st.number_input("BMI (kg/m²)", 10.0, 70.0, 25.0)
    dpf = st.number_input("Diabetes Pedigree", 0.0, 3.0, 0.3)
    age = st.number_input("Age (Years)",10 ,100, 30)

st.markdown(
    """
    <style>
    div.stButton > button {
        display: block;
        margin: auto;
        border: 2px solid black;         
        border-radius: 10px;
        background-color: #ffff00;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 80vw;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .alert-box {
        font-size: 28px;
        font-weight: 800;
        text-align: center;
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
    }
    .danger {
        background-color: #ffdddd;
        color: #a70000;
        border: 3px solid #ff0000;
    }
    .safe {
        background-color: #ddffdd;
        color: #006400;
        border: 3px solid #00a000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#model predict
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)
    st.write(prediction)
    # Custom CSS for large, alarming alerts
    # Prediction result
    if prediction[0] == 1:
        st.markdown(
            "<div class='alert-box danger'>⚠️ HIGH RISK: DIABETES LIKELY</div>",
            unsafe_allow_html=True)
    else:
        st.markdown(
            "<div class='alert-box safe'>✅ LOW RISK: DIABETES NOT LIKELY</div>",
            unsafe_allow_html=True)
