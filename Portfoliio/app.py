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
# Custom CSS - PREMIUM $300 TEMPLATE
# ---------------------------------------------------------
st.markdown("""
<style>

/* ------------------------------------------------------
   GLOBAL
------------------------------------------------------ */
body {
    background: #f5f7fa;
    font-family: 'Inter', sans-serif;
    animation: fadeBody 0.8s ease-in-out;
}

@keyframes fadeBody {
    from { opacity: 0; }
    to   { opacity: 1; }
}

/* ------------------------------------------------------
   HERO SECTION
------------------------------------------------------ */
.hero {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    padding: 70px 40px;
    border-radius: 25px;
    color: white;
    animation: fadeUp 1s ease-in-out;
    box-shadow: 0 20px 40px rgba(0,0,0,0.22);
    position: relative;
    overflow: hidden;
}

/* Animated gradient shine */
.hero::after {
    content: "";
    position: absolute;
    top: -50%;
    left: -30%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        135deg,
        rgba(255,255,255,0.25),
        rgba(255,255,255,0)
    );
    transform: rotate(25deg);
    animation: shine 4s infinite ease-in-out;
}

@keyframes shine {
    0% { transform: translateX(-60%) rotate(25deg); }
    50% { transform: translateX(10%) rotate(25deg); }
    100% { transform: translateX(-60%) rotate(25deg); }
}

.hero h1 {
    font-size: 54px;
    font-weight: 900;
    text-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

/* ------------------------------------------------------
   SECTION HEADER
------------------------------------------------------ */
.section-header {
    font-size: 34px;
    font-weight: 800;
    margin-top: 40px;
    color: #111827;
    padding-bottom: 10px;
    border-bottom: 3px solid #e5e7eb;
    animation: fadeUp 0.7s ease;
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ------------------------------------------------------
   PROJECT CARDS - PREMIUM
------------------------------------------------------ */
.card {
    background: rgba(255,255,255,0.45);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 26px;
    border: 1px solid rgba(255,255,255,0.35);
    position: relative;
    overflow: hidden;

    transform-style: preserve-3d;
    transition: 
        transform 0.45s cubic-bezier(0.2, 0.6, 0.4, 1),
        box-shadow 0.45s ease,
        border-color 0.35s ease;
    box-shadow: 0 12px 28px rgba(0,0,0,0.1);

    /* Staggered fade-in */
    opacity: 0;
    animation: fadeCard 0.9s ease forwards;
}

.card:nth-child(1) { animation-delay: 0.1s; }
.card:nth-child(2) { animation-delay: 0.25s; }
.card:nth-child(3) { animation-delay: 0.4s; }
.card:nth-child(4) { animation-delay: 0.55s; }
.card:nth-child(5) { animation-delay: 0.7s; }
.card:nth-child(6) { animation-delay: 0.85s; }

@keyframes fadeCard {
    from { opacity: 0; transform: translateY(25px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* 3D Hover Tilt + Lift */
.card:hover {
    transform: translateY(-12px) scale(1.04) rotateX(6deg);
    box-shadow: 0 25px 55px rgba(0,0,0,0.18);
    border-color: rgba(255,255,255,0.6);
}

/* Neon sweep glow */
.card:hover::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 220%;
    height: 220%;
    background: radial-gradient(
        circle at center,
        rgba(255,255,255,0.55),
        transparent 75%
    );
    opacity: 0.18;
    animation: neonSweep 1.4s ease-out forwards;
}

@keyframes neonSweep {
    from { transform: translate(-20%, -20%) scale(0.5); opacity: 0.2; }
    to   { transform: translate(20%, 20%) scale(1); opacity: 0; }
}

/* Animated border glow */
.card::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: 22px;
    padding: 2px;
    background: linear-gradient(135deg, #7c3aed, #6366f1, #3b82f6);
    mask: linear-gradient(#fff 0 0) content-box,
          linear-gradient(#fff 0 0);
    mask-composite: exclude;
    animation: borderGlow 5s infinite linear;
}

@keyframes borderGlow {
    0% { filter: hue-rotate(0deg); }
    100% { filter: hue-rotate(360deg); }
}

/* ------------------------------------------------------
   BUTTONS
------------------------------------------------------ */
.btn {
    padding: 10px 20px;
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white !important;
    font-weight: 700;
    border-radius: 12px;
    text-decoration: none;
    transition: 0.25s ease;
    box-shadow: 0 5px 15px rgba(99,102,241,0.3);
}

.btn:hover {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 10px 20px rgba(147,51,234,0.35);
}

/* ------------------------------------------------------
   TYPING TEXT
------------------------------------------------------ */
.typewriter {
    overflow: hidden;
    border-right: 3px solid white;
    white-space: nowrap;
    animation: typing 3s steps(30), blink .75s step-end infinite;
    font-size: 26px;
}

@keyframes typing {
    from { width: 0 }
    to   { width: 100% }
}
@keyframes blink {
    50% { border-color: transparent }
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HERO
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
# SIDEBAR
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Skills", "Courses", "Projects", "Resume", "Contact"]
choice = st.sidebar.radio("Select a section:", pages)

# ---------------------------------------------------------
# ABOUT ME
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
            <li>🔬 Breast Cancer Detection using CNNs</li>
            <li>🏡 Airbnb Price Analysis</li>
            <li>❤️ Heart Disease Prediction</li>
            <li>🏏 Cricket Analytics</li>
            <li>🚗 Used Car Price Predictor (ML + Streamlit)</li>
        </ul>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# SKILLS
# ---------------------------------------------------------
elif choice == "Skills":
    st.markdown('<div class="section-header">🧠 Skills</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
        <h4>💻 Programming Languages & Tools</h4>
        Python (NumPy, Pandas, Scikit-Learn) • R • SQL (PostgreSQL, MySQL) • Java •  
        JavaScript (ES6+) • Bash / Shell • Git & GitHub
        </div><br>

        <div class="card">
        <h4>📊 Data Science & Visualization</h4>
        Data Cleaning • EDA • Time-Series Analysis • Matplotlib • Seaborn • Plotly •  
        Power BI • Tableau • A/B Testing
        </div><br>

        <div class="card">
        <h4>🧮 Math Foundation</h4>
        Linear Algebra • Calculus • Probability & Statistics • Optimization
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🤖 Machine Learning & Deep Learning</h4>
        Scikit-Learn • TensorFlow • Keras • PyTorch •  
        XGBoost • LightGBM • CatBoost •  
        CNNs • LSTMs • RNNs •  
        BERT & Transformers •  
        Hyperparameter Tuning (GridSearchCV, Optuna)
        </div><br>

        <div class="card">
        <h4>🗄️ Databases & Data Engineering</h4>
        SQL (joins, CTEs, window functions) • PostgreSQL • MySQL • MongoDB •  
        Apache Spark (PySpark) • ETL Pipelines
        </div><br>

        <div class="card">
        <h4>☁️ Cloud & MLOps</h4>
        AWS (S3, EC2, Lambda, SageMaker) •  
        Docker • GitHub Actions (CI/CD) •  
        MLflow • Streamlit Deployment
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# COURSES
# ---------------------------------------------------------
elif choice == "Courses":
    st.markdown('<div class="section-header">🎓 Courses & Certifications</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h4>📜 Completed Courses</h4>
        <ul>
            <li>Python Data Analysis Certificate (Udemy)</li>
            <li>MySQL Certificate (Udemy)</li>
            <li>Google Data Analytics Professional Certificate</li>
            <li>Machine Learning A-Z (Udemy)</li>
            <li>Deep Learning Specialization</li>
            <li>Computer Vision Training (Udemy)</li>
            <li>Power BI Data Visualization Certification</li>
            <li>OpenAI & Generative AI Developer Course</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# PROJECTS
# ---------------------------------------------------------
elif choice == "Projects":
    st.markdown('<div class="section-header">📂 Featured Projects</div>', unsafe_allow_html=True)

    projects = [
        ("Breast Cancer Prediction", "Predict malignant vs benign cells",
         "https://github.com/wasayfaizan/Breast-Cancer-Prediction",
         "Python • Scikit-Learn • Pandas"),

        ("Sentiment Analysis (BERT + LSTM)", "NLP deep learning on tweets",
         "https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM",
         "TensorFlow • NLP • Transformers"),

        ("Teen Smartphone Addiction Predictor", "Predict addiction severity",
         "https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor",
         "Python • ML • Streamlit"),

        ("Netflix Data Insights", "Full EDA & visualization",
         "https://github.com/wasayfaizan/Netflix-data-insights",
         "Pandas • Seaborn • Plotly"),

        ("Used Car Price Predictor", "ML regression + UI",
         "https://github.com/wasayfaizan/Cars-Price-Predictor-ML",
         "Python • XGBoost • Streamlit"),

        ("Heart Disease Prediction", "Regression analysis and ML",
         "https://github.com/wasayfaizan/Heart-Disease-Prediction",
         "Python • Scikit-Learn")
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
# RESUME
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
# CONTACT
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
