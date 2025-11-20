import streamlit as st
from PIL import Image
import os

# -------------------------
# Page Config
# -------------------------
st.set_page_config(
    page_title="Abdul Wasay | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
)

# -------------------------
# Custom CSS Styling (WITH ANIMATIONS)
# -------------------------
st.markdown("""
    <style>

    /* ---------- Animations ---------- */
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes slideIn {
        from { opacity: 0; transform: translateX(-20px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    /* ---------- NEW Typing Effect ---------- */
    .typewriter {
        width: 0;
        overflow: hidden;
        white-space: nowrap;
        border-right: 3px solid #4b5563;
        font-size: 22px !important;
        font-weight: 400 !important;
        color: #4b5563;
        animation: typing 3s steps(40, end), blink .75s step-end infinite;
    }

    @keyframes typing {
        from { width: 0; }
        to   { width: 100%; }
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }

    /* ---------- Title Styles ---------- */
    .big-title {
        font-size: 48px !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
        animation: fadeIn 1s ease-in-out;
    }

    /* ---------- Section Header ---------- */
    .section-header {
        font-size: 32px !important;
        font-weight: 600 !important;
        margin-top: 20px;
        color: #111827;
        padding-bottom: 8px;
        border-bottom: 2px solid #e5e7eb;
        animation: slideIn 0.8s ease-out;
    }

    /* ---------- Project Cards ---------- */
    .project-box {
        background-color: #f9fafb;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #e5e7eb;
        transition: transform 0.25s, box-shadow 0.25s;
        animation: fadeInUp 0.8s ease-out;
    }
    .project-box:hover {
        transform: translateY(-6px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.12);
    }

    .project-title {
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 5px;
        animation: fadeInUp 0.6s ease-out;
    }

    </style>
""", unsafe_allow_html=True)

# -------------------------
# Header Section
# -------------------------
st.markdown('<p class="big-title">👋 Hi, I\'m <b>Abdul Wasay</b></p>', unsafe_allow_html=True)

# ⭐ REPLACED SUBTITLE WITH TYPING ANIMATION
st.markdown(
    '<p class="typewriter">Data Science • Machine Learning • Deep Learning • AI</p>',
    unsafe_allow_html=True
)

st.write(
    "I'm a Computer Science student at York University with a strong passion for Data Science, Machine Learning, "
    "Deep Learning, and Applied Mathematics."
)
st.write("---")

# -------------------------
# Sidebar Navigation
# -------------------------
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Skills", "Projects", "Resume", "Contact"]
choice = st.sidebar.radio("Select a section:", pages)

# -------------------------
# About Me
# -------------------------
if choice == "About Me":
    st.markdown('<p class="section-header">📌 About Me</p>', unsafe_allow_html=True)
    st.write("""
        I'm a 5th-year Computer Science student at **York University** with a minor in Applied Mathematics.  
        My main interests include:

        - 🤖 Machine Learning  
        - 📊 Data Analysis  
        - 🧠 Deep Learning  
        - 📈 Predictive Modeling  
        - 🏥 AI for Healthcare  
        - 🏏 Sports Analytics  

        Over the past few years, I have worked on multiple high-impact projects:
        - 🧠 Sentiment Analysis with BERT  
        - 🔬 Breast Cancer Detection using CNNs  
        - 🏡 Airbnb Price Analysis  
        - ❤️ Heart Disease Prediction  
        - 🏏 Cricket Analytics  
        - 🚗 Used Car Price Predictor (ML + Streamlit)
    """)

# -------------------------
# Skills
# -------------------------
elif choice == "Skills":
    st.markdown('<p class="section-header">🧠 Skills</p>', unsafe_allow_html=True)

    st.subheader("💻 Programming Languages & Tools")
    st.write("""
        - Python (NumPy, Pandas, Scikit-Learn)  
        - R  
        - SQL (PostgreSQL, MySQL)  
        - Java  
        - JavaScript (ES6+)  
        - Bash / Shell  
        - Git & GitHub  
    """)

    st.subheader("🤖 Machine Learning & Deep Learning")
    st.write("""
        - Scikit-Learn  
        - TensorFlow / Keras  
        - PyTorch  
        - XGBoost, LightGBM, CatBoost  
        - CNNs, LSTMs, RNNs  
        - BERT & Transformers  
        - Hyperparameter tuning (GridSearch, Optuna)  
    """)

    st.subheader("📊 Data Science & Visualization")
    st.write("""
        - Data Cleaning  
        - EDA  
        - Time-Series Analysis  
        - Matplotlib, Seaborn, Plotly  
        - Power BI, Tableau  
        - A/B Testing  
    """)

    st.subheader("🗄️ Databases & Data Engineering")
    st.write("""
        - SQL (joins, CTEs, window functions)  
        - PostgreSQL, MySQL  
        - MongoDB  
        - Apache Spark (PySpark)  
        - ETL pipelines  
    """)

    st.subheader("☁️ Cloud & DevOps / MLOps")
    st.write("""
        - AWS (S3, EC2, Lambda, SageMaker)  
        - Docker  
        - GitHub Actions (CI/CD)  
        - MLflow  
        - Streamlit deployment  
    """)

    st.subheader("🧮 Math Foundation")
    st.write("""
        - Linear Algebra  
        - Calculus  
        - Probability & Statistics  
        - Optimization  
    """)

# -------------------------
# Projects
# -------------------------
elif choice == "Projects":
    st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

    
    st.markdown('<p class="project-title">1️⃣ Breast Cancer Prediction</p>', unsafe_allow_html=True)
    st.write("""
        ML model predicting malignant vs benign cancer cells.  
        🔗 GitHub: https://github.com/wasayfaizan/Breast-Cancer-Prediction
    """)
    st.code("Tech: Python • Scikit-Learn • Pandas • Matplotlib")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<p class="project-title">2️⃣ Sentiment Analysis (LSTM)</p>', unsafe_allow_html=True)
    st.write("""
        Deep learning LSTM model on Sentiment140 dataset.  
        🔗 GitHub: https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM
    """)
    st.code("Tech: Python • TensorFlow • NLP • LSTM")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<p class="project-title">3️⃣ Teen Smartphone Addiction Predictor</p>', unsafe_allow_html=True)
    st.write("""
        Predicting addiction levels using ML.  
        🔗 GitHub: https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor
    """)
    st.code("Tech: Python • Scikit-Learn • EDA • Streamlit")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<p class="project-title">4️⃣ Netflix Data Insights</p>', unsafe_allow_html=True)
    st.write("""
        Full EDA on Netflix dataset.  
        🔗 GitHub: https://github.com/wasayfaizan/Netflix-data-insights
    """)
    st.code("Tech: Python • Pandas • Seaborn • Plotly")
    st.markdown('</div>', unsafe_allow_html=True)

    
    st.markdown('<p class="project-title">5️⃣ Used Car Price Predictor</p>', unsafe_allow_html=True)
    st.write("""
        ML regression model predicting used car prices.  
        🔗 GitHub: https://github.com/wasayfaizan/Cars-Price-Predictor-ML
    """)
    st.code("Tech: Python • Regression • XGBoost • Streamlit")
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Resume
# -------------------------
elif choice == "Resume":
    st.markdown('<p class="section-header">📄 Resume</p>', unsafe_allow_html=True)
    st.write("You can download my resume below:")

    resume_file = "Portfoliio/resume.pdf"

    try:
        with open(resume_file, "rb") as f:
            st.download_button(
                label="⬇️ Download My Resume",
                data=f,
                file_name="Abdul_Wasay_Resume.pdf",
                mime="application/pdf"
            )
    except:
        st.error("❌ Resume not found. Ensure it exists at: Portfoliio/resume.pdf")

# -------------------------
# Contact
# -------------------------
elif choice == "Contact":
    st.markdown('<p class="section-header">📬 Contact Me</p>', unsafe_allow_html=True)

    st.write("📧 Email: **a.wasayfaizan@hotmail.com**")
    st.write("🔗 LinkedIn: https://linkedin.com/in/wasayfaizan")
    st.write("💻 GitHub: https://github.com/wasayfaizan")
    st.write("---")
    st.write("✨ Thank you for visiting my portfolio!")
