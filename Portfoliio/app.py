import streamlit as st
from PIL import Image

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
    .project-box {
        background-color: #f9fafb;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        border: 1px solid #e5e7eb;
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

        I love transforming raw data into meaningful insights and building intelligent systems that make real impact.

        Over the past few years, I have worked on multiple high-impact projects:
        - 🧠 Sentiment Analysis with BERT  
        - 🔬 Breast Cancer Detection using CNNs  
        - 🏡 Airbnb Price Analysis and Modeling  
        - ❤️ Heart Disease Prediction  
        - 🏏 Cricket and sports analytics  
        - 🚗 Used Car Price Predictor (ML + Streamlit app)
        """
    )

# -------------------------
# Skills
# -------------------------
elif choice == "Skills":
    st.markdown('<p class="section-header">🧠 Skills</p>', unsafe_allow_html=True)

    st.subheader("Programming Languages")
    st.write("🐍 Python • 🐧 R • 🗄 SQL • ☕ Java • 🌐 JavaScript")

    st.subheader("Machine Learning & Deep Learning")
    st.write(
        "Scikit-Learn • TensorFlow/Keras • PyTorch • XGBoost • Random Forests • CNNs • LSTMs • BERT • Transformers"
    )

    st.subheader("Data Science & Analysis")
    st.write("Pandas • NumPy • Matplotlib • Seaborn • Plotly • EDA • Statistics • Feature Engineering")

    st.subheader("Cloud & Tools")
    st.write("AWS • Git/GitHub • Jupyter • Streamlit • VSCode • Google Colab")

    st.subheader("Math Foundations")
    st.write("Linear Algebra • Calculus • Probability • Optimization")

# -------------------------
# Projects
# -------------------------
elif choice == "Projects":
    st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

    # Project 1
    with st.container():
        
        st.markdown('<p class="project-title">1️⃣ Breast Cancer Prediction</p>', unsafe_allow_html=True)
        st.write(
            """
            Built ML classification models to predict malignant vs benign tissue using the IDC dataset.  
            Focus: feature engineering, model comparison (Logistic, RF, SVM), ROC-AUC, sensitivity/specificity.

            🔗 GitHub: https://github.com/wasayfaizan/Breast-Cancer-Prediction
            """
        )
        st.code("Tech: Python • Scikit-Learn • Pandas • Matplotlib • Jupyter Notebook")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 2
    with st.container():
        
        st.markdown('<p class="project-title">2️⃣ Sentiment Analysis on Tweets (LSTM)</p>', unsafe_allow_html=True)
        st.write(
            """
            Used Sentiment140 dataset. Developed and trained an LSTM model to classify tweets as positive, negative, neutral.  
            Special focus on text cleaning, embeddings, and hyperparameter tuning.

            🔗 GitHub: https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM
            """
        )
        st.code("Tech: Python • TensorFlow/Keras • NLP • LSTM • Text Preprocessing")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 3
    with st.container():
        
        st.markdown('<p class="project-title">3️⃣ Teen Smartphone Addiction Predictor</p>', unsafe_allow_html=True)
        st.write(
            """
            ML models trained to detect teen smartphone addiction levels based on behavioural, emotional, and usage data.

            🔗 GitHub: https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor
            """
        )
        st.code("Tech: Python • Pandas • Scikit-Learn • EDA • Streamlit")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 4
    with st.container():
        
        st.markdown('<p class="project-title">4️⃣ Netflix Data Insights</p>', unsafe_allow_html=True)
        st.write(
            """
            Performed full exploratory data analysis on Netflix dataset: genres, countries, durations, actors, release trends etc.

            🔗 GitHub: https://github.com/wasayfaizan/Netflix-data-insights
            """
        )
        st.code("Tech: Python • Pandas • Seaborn • Plotly • EDA")
        st.markdown('</div>', unsafe_allow_html=True)

    # Project 5
    with st.container():
        
        st.markdown('<p class="project-title">5️⃣ Used Car Price Predictor</p>', unsafe_allow_html=True)
        st.write(
            """
            End-to-end ML regression system for predicting used car prices (with a Streamlit interface).  
            Includes preprocessing, model comparison, and predictions.

            🔗 GitHub: https://github.com/wasayfaizan/Cars-Price-Predictor-ML
            """
        )
        st.code("Tech: Python • Regression • XGBoost • Data Cleaning • Streamlit")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# Resume
# -------------------------
elif choice == "Resume":
    st.markdown('<p class="section-header">📄 Resume</p>', unsafe_allow_html=True)

    st.write("You can download my resume below:")

    resume_file = "resume.pdf"
    try:
        with open(resume_file, "rb") as f:
            st.download_button("⬇️ Download My Resume", f, file_name="Abdul_Wasay_Resume.pdf")
    except:
        st.info("Upload a file named `resume.pdf` into your project folder.")

# -------------------------
# Contact
# -------------------------
elif choice == "Contact":
    st.markdown('<p class="section-header">📬 Contact Me</p>', unsafe_allow_html=True)

    st.write("Let's connect!")
    st.write("📧 Email: **a.wasayfaizan@hotmail.com**")
    st.write("🔗 LinkedIn: https://linkedin.com/in/abdul-wasay")
    st.write("💻 GitHub: https://github.com/wasayfaizan")
    st.write("---")
    st.write("✨ Thank you for visiting my portfolio!")
