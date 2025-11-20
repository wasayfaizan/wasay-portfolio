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
# Custom CSS Styling
# -------------------------
st.markdown("""
    <style>
    .big-title {
        font-size: 48px !important;
        font-weight: 700 !important;
        color: #1f2937 !important;
    }
    .sub-title {
        font-size: 22px !important;
        font-weight: 400 !important;
        color: #4b5563 !important;
    }
    .section-header {
        font-size: 32px !important;
        font-weight: 600 !important;
        margin-top: 20px;
        color: #111827;
        padding-bottom: 8px;
        border-bottom: 2px solid #e5e7eb;
    }
    .project-title {
        font-size: 22px !important;
        font-weight: 600 !important;
        margin-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# Header Section
# -------------------------
st.markdown('<p class="big-title">👋 Hi, I\'m <b>Abdul Wasay</b></p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Data Science • Machine Learning • Deep Learning • AI</p>',
            unsafe_allow_html=True)
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
    st.write(
        """
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
        - ❤️ Heart Disease Prediction Models  
        - 🏏 Cricket Analytics  
        - 🚗 Used Car Price Predictor (ML + Streamlit)
        """
    )

# -------------------------
# Skills
# -------------------------
elif choice == "Skills":
    st.markdown('<p class="section-header">🧠 Skills</p>', unsafe_allow_html=True)

    st.subheader("💻 Programming Languages & Tools")
    st.write(
        """
        - Python (NumPy, Pandas, Scikit-Learn)  
        - R  
        - SQL (PostgreSQL, MySQL)  
        - Java  
        - JavaScript (ES6+)  
        - Bash / Shell scripting  
        - Git & GitHub  
        """
    )

    st.subheader("🤖 Machine Learning & Deep Learning")
    st.write(
        """
        - Scikit-Learn (Regression, Classification, Clustering)  
        - TensorFlow / Keras  
        - PyTorch  
        - XGBoost • LightGBM • CatBoost  
        - Random Forests, Gradient Boosting Models  
        - CNNs, LSTMs, RNNs  
        - Transformers (BERT, HuggingFace)  
        - Feature engineering & selection  
        - Hyperparameter tuning (GridSearch, RandomSearch, Optuna)  
        - Model evaluation (ROC-AUC, precision, recall, sensitivity, specificity)  
        """
    )

    st.subheader("📊 Data Science, Analytics & Visualization")
    st.write(
        """
        - Data cleaning & preprocessing  
        - Exploratory Data Analysis (EDA)  
        - Time-series analysis  
        - Matplotlib, Seaborn, Plotly  
        - Power BI, Tableau  
        - Statistical inference, A/B testing  
        """
    )

    st.subheader("🗄️ Databases & Data Engineering")
    st.write(
        """
        - SQL queries, joins, window functions  
        - PostgreSQL, MySQL  
        - MongoDB  
        - Apache Spark (PySpark)  
        - ETL pipelines, data ingestion  
        """
    )

    st.subheader("☁️ Cloud, DevOps & MLOps")
    st.write(
        """
        - AWS (S3, EC2, Lambda, SageMaker)  
        - Docker  
        - CI/CD with GitHub Actions  
        - MLflow  
        - Streamlit deployment  
        - Flask API development  
        """
    )

    st.subheader("🎨 Web & App Development")
    st.write(
        """
        - Streamlit apps  
        - HTML / CSS basics  
        - JavaScript basics  
        """
    )

    st.subheader("🧮 Math & Foundation")
    st.write(
        """
        - Linear Algebra  
        - Multivariable Calculus  
        - Probability & Statistics  
        - Optimization  
        """
    )

    st.subheader("🧩 Soft Skills")
    st.write(
        """
        - Problem Solving  
        - Communication  
        - Team Collaboration  
        - Presentation Skills  
        - Self-Learning  
        """
    )

# -------------------------
# Projects
# -------------------------
elif choice == "Projects":
    st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

    st.markdown('<p class="project-title">1️⃣ Breast Cancer Prediction</p>', unsafe_allow_html=True)
    st.write(
        """
        Machine learning models to classify malignant vs benign cancer cells.

        🔗 GitHub: https://github.com/wasayfaizan/Breast-Cancer-Prediction
        """
    )
    st.code("Tech: Python • Scikit-Learn • Pandas • Matplotlib")

    st.markdown('<p class="project-title">2️⃣ Sentiment Analysis (LSTM)</p>', unsafe_allow_html=True)
    st.write(
        """
        Sentiment140 dataset with deep learning LSTM model for sentiment prediction.

        🔗 GitHub: https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM
        """
    )
    st.code("Tech: Python • TensorFlow • NLP • LSTM")

    st.markdown('<p class="project-title">3️⃣ Teen Smartphone Addiction Predictor</p>', unsafe_allow_html=True)
    st.write(
        """
        ML models predicting smartphone addiction levels in teenagers.

        🔗 GitHub: https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor
        """
    )
    st.code("Tech: Python • Pandas • Scikit-Learn • Streamlit")

    st.markdown('<p class="project-title">4️⃣ Netflix Data Insights</p>', unsafe_allow_html=True)
    st.write(
        """
        Full dataset analysis on Netflix shows and movies.

        🔗 GitHub: https://github.com/wasayfaizan/Netflix-data-insights
        """
    )
    st.code("Tech: Python • Pandas • Seaborn • Plotly")

    st.markdown('<p class="project-title">5️⃣ Used Car Price Predictor</p>', unsafe_allow_html=True)
    st.write(
        """
        ML regression model predicting used car prices.

        🔗 GitHub: https://github.com/wasayfaizan/Cars-Price-Predictor-ML
        """
    )
    st.code("Tech: Python • Regression • XGBoost • Streamlit")

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
    except FileNotFoundError:
        st.error("❌ Resume not found. Make sure `Portfoliio/resume.pdf` exists.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# -------------------------
# Contact
# -------------------------
elif choice == "Contact":
    st.markdown('<p class="section-header">📬 Contact Me</p>', unsafe_allow_html=True)

    st.write("📧 Email: **a.wasayfaizan@hotmail.com**")
    st.write("🔗 LinkedIn: https://linkedin.com/in/abdul-wasay")
    st.write("💻 GitHub: https://github.com/wasayfaizan")
    st.write("---")
    st.write("✨ Thank you for visiting my portfolio!")
