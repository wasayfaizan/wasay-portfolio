import streamlit as st
from PIL import Image

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abdul Wasay | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
)

# ---------------------------------------------------------
# Custom CSS
# ---------------------------------------------------------
st.markdown("""
<style>

body {
    background: #f5f7fa;
    font-family: 'Inter', sans-serif;
}

/* ----------- Hero Section ----------- */
.hero {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    padding: 70px 40px;
    border-radius: 20px;
    color: white;
    animation: fadeIn 1s ease-in-out;
    margin-bottom: 30px;
}
.hero h1 {
    font-size: 52px;
    font-weight: 800;
}
.hero p {
    font-size: 20px;
    opacity: 0.95;
}

/* ----------- Section Header ----------- */
.section-header {
    font-size: 32px;
    font-weight: 700;
    margin-top: 30px;
    color: #1f2937;
    padding-bottom: 8px;
    border-bottom: 3px solid #e5e7eb;
}

/* ----------- Cards (Glassmorphism) ----------- */
.card {
    background: rgba(255, 255, 255, 0.55);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 22px;
    border: 1px solid rgba(255,255,255,0.35);
    transition: 0.25s ease;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 26px rgba(0,0,0,0.12);
}

/* ----------- Buttons ----------- */
.btn {
    padding: 10px 18px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white !important;
    text-decoration: none;
    border-radius: 10px;
    font-weight: 600;
    transition: 0.25s;
}
.btn:hover {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
}

/* ----------- Typing Animation ----------- */
.typewriter {
  overflow: hidden;
  border-right: 3px solid white;
  white-space: nowrap;
  animation: typing 3s steps(30), blink .75s step-end infinite;
  font-size: 26px;
}

@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}
@keyframes blink {
  50% { border-color: transparent }
}

@keyframes fadeIn {
  from { opacity:0; transform: translateY(10px); }
  to   { opacity:1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Hero Section
# ---------------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>👋 Hi, I'm <b>Abdul Wasay</b></h1>
    <p class="typewriter">Data Science • Machine Learning • Deep Learning • AI</p>
    <p style="margin-top:10px;">
        I'm a Computer Science student at York University with a strong passion for Data Science, Machine Learning,
        Deep Learning, and Applied Mathematics.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Skills", "Projects", "Resume", "Contact"]
choice = st.sidebar.radio("Select a section:", pages)

# ---------------------------------------------------------
# About Me
# ---------------------------------------------------------
if choice == "About Me":
    st.markdown('<div class="section-header">📌 About Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
        I'm a 5th-year Computer Science student at <b>York University</b> with a minor in Applied Mathematics.<br><br>
        
        My main interests include:
        <ul>
            <li>🤖 Machine Learning</li>
            <li>📊 Data Analysis</li>
            <li>🧠 Deep Learning</li>
            <li>📈 Predictive Modeling</li>
            <li>🏥 AI for Healthcare</li>
            <li>🏏 Sports Analytics</li>
        </ul>
        
        High-impact projects I've worked on:
        <ul>
            <li>🧠 Sentiment Analysis with BERT</li>
            <li>🔬 Breast Cancer Detection (CNN)</li>
            <li>🏡 Airbnb Price Analysis</li>
            <li>❤️ Heart Disease Prediction</li>
            <li>🏏 Cricket Analytics</li>
            <li>🚗 Used Car Price Predictor (ML + Streamlit)</li>
        </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Skills
# ---------------------------------------------------------
elif choice == "Skills":
    st.markdown('<div class="section-header">🧠 Skills</div>', unsafe_allow_html=True)

    cols = st.columns(2)

    with cols[0]:
        st.markdown("""
        <div class="card">
        <h4>💻 Programming Languages & Tools</h4>
        Python • R • SQL • Java • JS • Bash • Git
        </div><br>
        
        <div class="card">
        <h4>📊 Data Science & Visualization</h4>
        Pandas • NumPy • EDA • Plotly • Seaborn • Power BI
        </div>
        """, unsafe_allow_html=True)

    with cols[1]:
        st.markdown("""
        <div class="card">
        <h4>🤖 Machine Learning & Deep Learning</h4>
        Scikit-Learn • TensorFlow • Keras • PyTorch • XGBoost • CNNs • BERT
        </div><br>

        <div class="card">
        <h4>☁️ Cloud & MLOps</h4>
        AWS • Docker • GitHub Actions • MLflow • Streamlit
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Projects
# ---------------------------------------------------------
elif choice == "Projects":
    st.markdown('<div class="section-header">📂 Featured Projects</div>', unsafe_allow_html=True)

    projects = [
        ("Breast Cancer Prediction", "Predict malignant vs benign cells", 
         "https://github.com/wasayfaizan/Breast-Cancer-Prediction",
         "Python • Scikit-Learn • Pandas"),

        ("Sentiment Analysis (LSTM)", "Deep Learning on tweets", 
         "https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM",
         "TensorFlow • NLP • LSTM"),

        ("Teen Smartphone Addiction Predictor", "Predicting addiction levels using ML",
         "https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor",
         "Python • ML • EDA"),

        ("Netflix Data Insights", "Full EDA on Netflix dataset",
         "https://github.com/wasayfaizan/Netflix-data-insights",
         "Pandas • Seaborn • Plotly"),

        ("Used Car Price Predictor", "Regression ML models with Streamlit",
         "https://github.com/wasayfaizan/Cars-Price-Predictor-ML",
         "Python • XGBoost • Streamlit")
    ]

    for title, desc, link, tech in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
            <p><b>Tech:</b> {tech}</p>
            <a class="btn" href="{link}" target="_blank">🔗 View on GitHub</a>
        </div><br>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Resume
# ---------------------------------------------------------
elif choice == "Resume":
    st.markdown('<div class="section-header">📄 Resume</div>', unsafe_allow_html=True)
    st.write("Download my resume:")

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
        st.error("❌ Resume not found. Ensure the file exists.")

# ---------------------------------------------------------
# Contact
# ---------------------------------------------------------
elif choice == "Contact":
    st.markdown('<div class="section-header">📬 Contact Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <p>
        📧 Email: <b>a.wasayfaizan@hotmail.com</b><br>
        🔗 LinkedIn: <a href="https://linkedin.com/in/wasayfaizan" target="_blank">linkedin.com/in/wasayfaizan</a><br>
        💻 GitHub: <a href="https://github.com/wasayfaizan" target="_blank">github.com/wasayfaizan</a><br><br>
        ✨ Thanks for visiting my portfolio!
        </p>
    </div>
    """, unsafe_allow_html=True)
