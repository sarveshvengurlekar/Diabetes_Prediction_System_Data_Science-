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


st.markdown(
    """
    <a href="https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database" target="_blank" style="text-decoration:none;">
        <div style="
            border:1px solid #ddd;
            border-radius:12px;
            padding:16px;
            max-width:2000px;
            background-color:#ffff00;
            box-shadow:2px 2px 8px rgba(0,0,0,0.1);
        ">
            <h4 style="margin-bottom:8px; color:#1f77b4;">
                📊 Pima Indians Diabetes Dataset
            </h4>
            <p style="margin:0; color:#333;">
                A widely used dataset for diabetes prediction containing diagnostic medical attributes.
                Hosted on Kaggle and sourced from the UCI Machine Learning Repository.
            </p>
            <p style="margin-top:8px; color:#555;">
                🔗 kaggle.com
            </p>
        </div>
    </a>
    """,
    unsafe_allow_html=True
)

st.subheader("")
st.subheader("Feature Description – Pima Indians Diabetes Dataset", divider=True)

st.markdown(
    """
### 🔹 Pregnancies
- Number of times the patient has been pregnant.  
- Higher counts may indicate increased risk due to hormonal and metabolic changes.
""")
st.image("media/dataset_stats/preg_pdf.png")

st.markdown("""
### 🔹 Glucose
- Plasma glucose concentration measured two hours after an oral glucose tolerance test.  
- One of the most important predictors of diabetes; higher values typically correlate with diabetic outcomes.
""")
st.image("media/dataset_stats/glu_pdf.png")
st.image("media/dataset_stats/glu_dist.png")

st.markdown("""
### 🔹 BloodPressure
- Diastolic blood pressure (mm Hg).  
- Chronic high or low blood pressure can be associated with metabolic health issues.
""")
st.image("media/dataset_stats/bp_pdf.png")

st.markdown("""
### 🔹 SkinThickness
- Triceps skinfold thickness (mm), indicating subcutaneous fat.  
- Used as a proxy for body fat; may influence insulin resistance.
""")
st.image("media/dataset_stats/sk_pdf.png")

st.markdown("""
### 🔹 Insulin
- 2-hour serum insulin (IU/mL) after glucose intake.  
- High variability and zero values indicate missing data or abnormal insulin response.
""")
st.image("media/dataset_stats/insulin_pdf.png")

st.markdown("""
### 🔹 BMI
- Body Mass Index (weight in kg ÷ height in m²).  
- Elevated BMI is a strong risk factor for type 2 diabetes.
""")
st.image("media/dataset_stats/bmi_pdf.png")

st.markdown("""
### 🔹 DiabetesPedigreeFunction
- Represents genetic predisposition based on family history of diabetes.  
- Higher values suggest a stronger hereditary risk.
""")
st.image("media/dataset_stats/pedi_pdf.png")

st.markdown("""
### 🔹 Age
- Age of the patient in years.  
- Diabetes risk increases with age, especially after the mid-30s.
""")
st.image("media/dataset_stats/age_pdf.png")

st.markdown("""
### 🔹 Outcome
- Binary target variable: **0 = Non-Diabetic, 1 = Diabetic**.  
- Used as the ground truth label for model training and evaluation.
    """
)
st.image("media/dataset_stats/age_pdf.png")

st.markdown("""
### 🔹 Correlation
- Correlates every Parameter to Outcome.
- It can find high impact parameters.
    """
)
st.image("media/dataset_stats/correlate.png")

