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
# Custom CSS - PREMIUM TEMPLATE
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
   PROJECT CARDS
------------------------------------------------------ */
.card {
    background: rgba(255,255,255,0.45);
    backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 26px;
    border: 1px solid rgba(255,255,255,0.35);
    margin-bottom: 25px;

    opacity: 0;
    animation: fadeCard 0.8s ease forwards;

    transition:
        transform 0.35s cubic-bezier(0.2, 0.6, 0.4, 1),
        box-shadow 0.35s ease,
        border-color 0.35s ease,
        background 0.35s ease;
}

@keyframes fadeCard {
    from { opacity: 0; transform: translateY(25px); }
    to   { opacity: 1; transform: translateY(0); }
}

.card:hover {
    transform: translateY(-10px) scale(1.025);
    border-color: rgba(255,255,255,0.6);
    background: rgba(255,255,255,0.55);
    box-shadow:
        0 12px 24px rgba(0,0,0,0.10),
        0 20px 40px rgba(0,0,0,0.07);
}

/* ------------------------------------------------------
   EXPERIENCE CARDS
------------------------------------------------------ */
.experience-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 20px;
    animation: fadeInUp 0.8s ease;
}

.experience-title {
    font-size: 20px;
    font-weight: 800;
    color: #4f46e5;
    margin-bottom: 6px;
}

.experience-role {
    font-size: 18px;
    font-weight: 600;
}

.experience-duration {
    font-size: 15px;
    color: #6b7280;
    margin-bottom: 12px;
}

.experience-desc {
    font-size: 15px;
    line-height: 1.55;
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
}

.btn:hover {
    background: linear-gradient(135deg, #4f46e5, #9333ea);
    transform: translateY(-2px) scale(1.03);
}

/* ------------------------------------------------------
   TYPEWRITER
------------------------------------------------------ */
.typewriter {
    overflow: hidden;
    border-right: 3px solid white;
    white-space: nowrap;
    animation: typing 3s steps(30), blink .75s step-end infinite;
    font-size: 26px;
}

@keyframes typing { from { width: 0 } to { width: 100% } }
@keyframes blink { 50% { border-color: transparent } }

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
# SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Skills", "Courses", "Projects", "Experience", "Resume", "Contact"]
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
        I specialize in building Machine Learning models, Deep Learning systems, and Data Analysis pipelines.<br><br>

        Interests:
        <ul>
            <li>🤖 Machine Learning</li>
            <li>🧠 Deep Learning</li>
            <li>📊 Data Analytics</li>
            <li>🏏 Sports Analytics</li>
            <li>🚀 AI for Healthcare</li>
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
        <h4>💻 Programming</h4>
        Python • R • SQL • Java • JavaScript • Bash • Git
        </div>
        <div class="card">
        <h4>📊 Data Science</h4>
        Pandas • NumPy • Matplotlib • Seaborn • Plotly • Tableau • Power BI
        </div>
        <div class="card">
        <h4>🧮 Math</h4>
        Linear Algebra • Probability • Statistics • Optimization
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
        <h4>🤖 Machine Learning</h4>
        Scikit-Learn • TensorFlow • PyTorch • CNN • LSTM • Transformers • XGBoost
        </div>
        <div class="card">
        <h4>🗄️ Databases</h4>
        PostgreSQL • MySQL • MongoDB • ETL Pipelines • Spark
        </div>
        <div class="card">
        <h4>☁️ Cloud / DevOps</h4>
        AWS • Docker • GitHub Actions • Streamlit Deployment
        </div>
        """, unsafe_allow_html=True)



# ---------------------------------------------------------
# COURSES
# ---------------------------------------------------------
elif choice == "Courses":
    st.markdown('<div class="section-header">🎓 Courses & Certifications</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <ul>
            <li>Python Data Analysis (Udemy)</li>
            <li>MySQL Certificate (Udemy)</li>
            <li>Google Data Analytics</li>
            <li>Machine Learning A-Z</li>
            <li>Deep Learning Specialization</li>
            <li>Computer Vision (Udemy)</li>
            <li>Power BI Certification</li>
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

        ("Used Car Price Predictor", "Regression model + UI",
         "https://github.com/wasayfaizan/Cars-Price-Predictor-ML",
         "XGBoost • Streamlit"),

        ("Netflix Data Insights", "Full EDA & dashboard",
         "https://github.com/wasayfaizan/Netflix-data-insights",
         "Pandas • Seaborn • Plotly"),
    ]

    for title, desc, link, tech in projects:
        st.markdown(f"""
        <div class="card">
            <h3>{title}</h3>
            <p>{desc}</p>
            <p><b>Tech:</b> {tech}</p>
            <a class="btn" href="{link}" target="_blank">🔗 View on GitHub</a>
        </div>
        """, unsafe_allow_html=True)



# ---------------------------------------------------------
# EXPERIENCE
# ---------------------------------------------------------
elif choice == "Experience":
    st.markdown('<div class="section-header">💼 Experience</div>', unsafe_allow_html=True)

    # Experience 1
    shipping_exp = """
    <div class="experience-card">
        <div class="experience-title">Customer Service & Data Support Assistant</div>
        <div class="experience-role">Infinity Shipping Services – Karachi, Pakistan</div>
        <div class="experience-duration">May 2021 – Aug 2021</div>
        <div class="experience-desc">
            • Delivered multi-channel customer support while resolving inquiries and service issues efficiently.<br>
            • Used Microsoft Excel to monitor service request trends, escalate recurring issues, and support process improvements.<br>
            • Organized and maintained structured customer data to enhance workflow and reporting accuracy.<br>
            • Contributed to weekly team reports analyzing customer feedback and performance metrics.
        </div>
    </div>
    """

    # Experience 2
    cyber_exp = """
    <div class="experience-card">
        <div class="experience-title">Data Analyst Intern (Cybersecurity)</div>
        <div class="experience-role">Rewterz – Pakistan</div>
        <div class="experience-duration">2024</div>
        <div class="experience-desc">
            • Built predictive models using Python + SQL.<br>
            • Automated data ingestion & cleaning pipelines improving data accuracy by 22%.<br>
            • Developed dashboards to uncover key security risk factors.<br>
            • Supported cybersecurity analysis workflows involving structured threat data.
        </div>
    </div>
    """

    st.markdown(shipping_exp, unsafe_allow_html=True)
    st.markdown(cyber_exp, unsafe_allow_html=True)



# ---------------------------------------------------------
# RESUME
# ---------------------------------------------------------
elif choice == "Resume":
    st.markdown('<div class="section-header">📄 Resume</div>', unsafe_allow_html=True)

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
        st.error("❌ Resume not found.")



# ---------------------------------------------------------
# CONTACT
# ---------------------------------------------------------
elif choice == "Contact":
    st.markdown('<div class="section-header">📬 Contact Me</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        📧 Email: <b>a.wasayfaizan@hotmail.com</b><br>
        🔗 LinkedIn: <a href="https://linkedin.com/in/wasayfaizan" target="_blank">linkedin.com/in/wasayfaizan</a><br>
        💻 GitHub: <a href="https://github.com/wasayfaizan" target="_blank">github.com/wasayfaizan</a><br><br>
        ✨ Thanks for visiting my portfolio!
    </div>
    """, unsafe_allow_html=True)
