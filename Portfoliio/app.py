import streamlit as st
from PIL import Image
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Abdul Wasay | Data Science Portfolio",
    page_icon="📊",
    layout="wide",
)

# -------------------------
# VIEW COUNTER
# -------------------------
VIEW_FILE = "Portfoliio/views.txt"

def add_view():
    if not os.path.exists(VIEW_FILE):
        with open(VIEW_FILE, "w") as f:
            f.write("0")

    with open(VIEW_FILE, "r") as f:
        count = int(f.read().strip())

    count += 1

    with open(VIEW_FILE, "w") as f:
        f.write(str(count))

    return count

views = add_view()

# -------------------------
# CUSTOM CSS + ANIMATIONS
# -------------------------
st.markdown("""
    <style>

    @keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
    @keyframes fadeInUp { from {opacity:0; transform:translateY(12px);} to {opacity:1; transform:translateY(0);} }
    @keyframes slideIn { from {opacity:0; transform:translateX(-20px);} to {opacity:1; transform:translateX(0);} }

    .big-title {
        font-size:48px; font-weight:700; color:#1f2937;
        animation: fadeIn 1s ease-in-out;
    }
    .sub-title {
        font-size:22px; color:#4b5563;
        animation: fadeIn 1.3s ease-in-out;
    }
    .section-header {
        font-size:32px; font-weight:600; margin-top:20px;
        border-bottom:2px solid #e5e7eb;
        animation: slideIn .8s ease-out;
    }

    .project-box {
        background:#f9fafb;
        padding:18px; border-radius:12px;
        border:1px solid #e5e7eb;
        transition:.25s;
        animation: fadeInUp .8s ease-out;
    }
    .project-box:hover {
        transform:translateY(-6px);
        box-shadow:0 8px 18px rgba(0,0,0,.12);
    }

    </style>
""", unsafe_allow_html=True)

# -------------------------
# HEADER
# -------------------------
st.markdown('<p class="big-title">👋 Hi, I\'m <b>Abdul Wasay</b></p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Data Science • Machine Learning • Deep Learning • AI</p>',
            unsafe_allow_html=True)

st.sidebar.write(f"👁️ Views: **{views}**")

st.write("---")

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("📌 Navigation")
pages = ["About Me", "Skills", "Projects", "Resume", "Contact"]
choice = st.sidebar.radio("Select a section:", pages)

# -------------------------
# ABOUT
# -------------------------
if choice == "About Me":
    st.markdown('<p class="section-header">📌 About Me</p>', unsafe_allow_html=True)
    st.write("""
        I'm a 5th-year Computer Science student at **York University**  
        specializing in **Machine Learning, Data Science, and Deep Learning**.
    """)

# -------------------------
# SKILLS
# -------------------------
elif choice == "Skills":
    st.markdown('<p class="section-header">🧠 Skills</p>', unsafe_allow_html=True)
    st.write("""
        - Python, R, SQL  
        - TensorFlow, PyTorch, Scikit-Learn  
        - Data Visualization, EDA  
        - AWS, Docker, GitHub Actions  
        - Streamlit, Flask  
        - Math skills: Linear Algebra, Probability, Optimization  
    """)

# -------------------------
# PROJECTS (WITH THUMBNAILS)
# -------------------------
elif choice == "Projects":
    st.markdown('<p class="section-header">📂 Featured Projects</p>', unsafe_allow_html=True)

    # Load images
    def load_img(path):
        return Image.open(path)

    projects = [
        ("Breast Cancer Prediction", 
         "assets/breast.png",
         "https://github.com/wasayfaizan/Breast-Cancer-Prediction",
         "Python • Scikit-Learn • Pandas"),
        
        ("Sentiment Analysis (LSTM)", 
         "assets/sentiment.png",
         "https://github.com/wasayfaizan/Sentiment-Analysis-on-Tweets-using-LSTM",
         "TensorFlow • NLP • LSTM"),

        ("Teen Smartphone Addiction Predictor",
         "assets/teen.png",
         "https://github.com/wasayfaizan/Teen-Phone-Addiction-Predictor",
         "Python • Scikit-Learn • Streamlit"),

        ("Netflix Data Insights",
         "assets/netflix.png",
         "https://github.com/wasayfaizan/Netflix-data-insights",
         "Python • Plotly • Pandas"),

        ("Used Car Price Predictor",
         "assets/cars.png",
         "https://github.com/wasayfaizan/Cars-Price-Predictor-ML",
         "XGBoost • Regression • Streamlit")
    ]

    for title, img_path, link, tech in projects:
        st.markdown('<div class="project-box">', unsafe_allow_html=True)
        try:
            st.image(load_img(img_path), use_column_width=True)
        except:
            st.warning(f"⚠️ Missing image: {img_path}")

        st.markdown(f"### {title}")
        st.write(f"🔗 GitHub: {link}")
        st.code(tech)
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# RESUME
# -------------------------
elif choice == "Resume":
    st.markdown('<p class="section-header">📄 Resume</p>', unsafe_allow_html=True)

    st.write("Download my resume below:")
    resume_file = "Portfoliio/resume.pdf"

    try:
        with open(resume_file, "rb") as f:
            st.download_button("⬇️ Download Resume",
                               f,
                               file_name="Abdul_Wasay_Resume.pdf",
                               mime="application/pdf")
    except:
        st.error("❌ Resume not found. Upload `resume.pdf` inside Portfoliio/")

# -------------------------
# CONTACT
# -------------------------
elif choice == "Contact":
    st.markdown('<p class="section-header">📬 Contact Me</p>', unsafe_allow_html=True)
    st.write("📧 Email: **a.wasayfaizan@hotmail.com**")
    st.write("🔗 LinkedIn: https://linkedin.com/in/abdul-wasay")
    st.write("💻 GitHub: https://github.com/wasayfaizan")
