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

st.subheader("📈 Regression in Data Science")
st.markdown(
    """
**Regression** is a supervised machine learning technique used to model the relationship 
between a dependent variable (output) and one or more independent variables (inputs).

It helps in understanding how changes in input features affect the output and is widely 
used in prediction and trend analysis.

### Key Points
- Used to predict outcomes based on input features  
- Helps identify relationships between variables  
- Commonly applied in healthcare, finance, and forecasting  
- Forms the foundation of many machine learning models  
"""
)

st.subheader("📊 Relevance of Regression in Data Science")
st.markdown(
    """
Regression plays a crucial role in data science as it enables:
- Predictive modeling and decision-making  
- Feature impact analysis and interpretability  
- Statistical understanding of real-world data  
- Reliable solutions for data-driven problems  
"""
)

st.subheader(" Logistic Regression")
st.image("media/model_stats/logi_reg.png")
st.markdown(
    """
**Logistic Regression** is a supervised machine learning algorithm used for 
**binary classification problems**, where the output variable has two possible classes 
(e.g., diabetic or non-diabetic).

Unlike linear regression, logistic regression uses a **sigmoid (logistic) function** 
to map predictions into a probability range between **0 and 1**.

The model outputs the probability of a given input belonging to the positive class.
"""
)

st.subheader(" Why Logistic Regression for Diabetes Prediction")
st.markdown(
    """
- Diabetes prediction is a **binary classification problem**  
- Logistic regression provides **probability-based predictions**  
- Easy to interpret and explain, especially for medical data  
- Efficient for small to medium-sized datasets  
- Widely accepted in healthcare analytics  
"""
)

st.subheader(" Working of Logistic Regression in This System")
st.markdown(
    """
- Medical parameters such as glucose level, BMI, age, and insulin are taken as inputs  
- The model learns optimal weights during training  
- A sigmoid function converts the weighted sum into probability  
- A threshold (commonly 0.5) is used to classify diabetic or non-diabetic  
"""
)

st.subheader(" Application in Diabetes Prediction System")
st.markdown(
    """
- Identifies individuals at risk of diabetes  
- Supports early diagnosis and preventive healthcare  
- Produces fast and reliable predictions    
- Suitable for academic and real-world healthcare applications  
"""
)

st.subheader(" Confusion Matrix")
st.image(r"media/model_stats/confusion_mat.png")

st.subheader(" Model Evaluation")
st.image(r"media/model_stats/model_eval.png")

st.subheader(" ROC Curve")
st.image(r"media/model_stats/roc_curve.png")
