
import streamlit as st

st.set_page_config(
    page_title="Diabetes Prediction System",
    layout="wide"
)

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

st.header("Model API", divider=True)

st.markdown(
    """
    <a href="https://diabetes-prediction-system-api-data.onrender.com" target="_blank" style="text-decoration:none;">
        <div style="
            border:1px solid #ddd;
            border-radius:12px;
            padding:16px;
            max-width:2000px;
            background-color:#ffff00;
            box-shadow:2px 2px 8px rgba(0,0,0,0.1);
        ">
            <h4 style="margin-bottom:8px; color:#1f77b4;">
                Diabetes Logistical Regression Model API
            </h4>
            <p style="margin:0; color:#333;">
            </p>
            <p style="margin-top:8px; color:#555;">
                🔗 render.com
            </p>
        </div>
    </a>
    """,
    unsafe_allow_html=True
)

st.subheader("API Docs", divider=True)

st.write("###  - Input Parameters")
st.write("""
- **pregnancies**: datatype = int, min = 0, max = 20
- **glucose**: datatype = int, min = 50, max = 300
- **blood_pressure**: datatype = int, min = 30, max = 150
- **skin_thickness**: datatype = int, min = 0, max = 100
- **insulin**: datatype = int, min = 0, max = 900
- **bmi**: datatype = float, min = 10.0, max = 70.0
- **dpf**: datatype = float, min = 0.0, max = 3.0
- **age**: datatype = int, min = 10, max = 100
""")

st.write("###  - Output Parameters")

st.write('- **Diabetic :-**')
st.write(
    {
    "" : {
        "prediction": 1,
        "result": "Diabetic"
    },
    })

st.write('- **Non-Diabetic :-**')
st.write({
    "": {
        "prediction": 0,
        "result": "Non-Diabetic"
    }
    })

