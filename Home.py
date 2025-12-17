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
    <style>
    div.stLinkButton > a {
        display: block;
        margin: auto;
        border: 2px solid black;         
        border-radius: 10px;
        background-color: #08f1e4;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("Diabetes Prediction System", divider=True)

st.markdown(
    """
    Diabetes has emerged as one of the most serious public health challenges in India. 
    Due to rapid urbanization, sedentary lifestyles, unhealthy dietary habits, and increasing stress levels, 
    India is often referred to as the **“Diabetes Capital of the World.”** Early detection plays a crucial role 
    in preventing severe complications such as heart disease, kidney failure, nerve damage, and vision loss.

    This **Diabetes Prediction System** utilizes **Machine Learning and Data Science techniques** to help identify 
    individuals who may be at risk of developing diabetes at an early stage. The system is powered by a 
    **Logistic Regression model**, a reliable and interpretable classification algorithm widely used in healthcare analytics.

    The application features a **user-friendly web interface built using Streamlit**, enabling users to input 
    basic medical parameters and receive instant diabetes risk predictions. The model is trained using the 
    **Pima Indians Diabetes Dataset**, a standard benchmark dataset for diabetes prediction research.
    """
)

st.subheader("Key Features")

st.markdown(
    """
    -  Focuses on India’s growing diabetes burden and preventive healthcare  
    -  Machine Learning model based on **Logistic Regression**  
    -  Trained on the **Pima Indians Diabetes Dataset (Kaggle / UCI ML Repository)**  
    -  Uses medical attributes such as glucose level, BMI, blood pressure, insulin, and age  
    -  Simple and interactive **Streamlit-based GUI**  
    -  Provides fast and real-time diabetes risk prediction  
    -  Encourages early diagnosis and health awareness  
    """
)



st.link_button("Predict Diabetes", "https://diabetespredictionsystemds.streamlit.app/Diabetes_Predictor", use_container_width=True)

st.header("")

st.header("</> Developer", divider="blue")

linkedin_sarvesh = "https://www.linkedin.com/in/sarvesh-vengurlekar-"
email_sarvesh = "mailto:sarveshvengurlekarwork@gmail.com?subject=Sharing Feedback and Connection Request Regarding Diabetes Prediction System"


# UI Design
col1, col2, col3 = st.columns(3)

with col2:
    with st.container():
        st.markdown(
            f"""
        <style>
            .profile-card {{
                text-align: center;
                background: #08f1e4;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                display: inline-block;
            }}
            .name {{
                font-size: 24px;
                font-weight: bold;
                margin-top: 10px;
                color: black;
            }}
            .title {{
                font-size: 16px;
                color: black;
                margin-top: 5px;
            }}
            .button-container {{
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-top: 10px;
            }}
            .button {{
                background-color: white;
                border: none;
                padding: 10px 15px;
                text-align: center;
                font-size: 16px;
                border-radius: 5px;
                cursor: pointer;
                text-decoration: none;
                margin: 5px;
                display: inline-flex;
                align-items: center;
                gap: 10px;
            }}
            .linkedin-button {{
                color: black;
            }}
            .icon {{
                width: 20px;
                height: 20px;
            }}
        </style>
        <div class="profile-card">
            <div class="name">Sarvesh Vengurlekar</div>
            <div class="title">Developer</div>
                <a href="{linkedin_sarvesh}" target="_blank" class="button linkedin-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" class="icon">
                </a>
                <a href="{email_sarvesh}" class="button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" class="icon">
                </a>
            </div>
        </div>
            """,
        unsafe_allow_html=True)



