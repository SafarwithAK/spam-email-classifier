import streamlit as st
import pickle
import string
nltk.download('punkt')
nltk.download('stopwords')

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

# ---------------- NLP SETUP ----------------
ps = PorterStemmer()
stop_words = set(stopwords.words('english'))

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stop_words and i not in string.punctuation]
    y = [ps.stem(i) for i in y]
    return " ".join(y)

# ---------------- LOAD MODEL ----------------
tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model.pkl", "rb"))

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Settings")
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

st.sidebar.markdown("---")
st.sidebar.metric("🎯 Model Accuracy", "97.97%")

st.sidebar.markdown("""
🛠 **Tech Stack**
- Python  
- NLTK  
- TF-IDF  
- Machine Learning  

👨‍💻 **Developer:** Ajit Kumar
""")

# ---------------- CUSTOM CSS ----------------
if dark_mode:
    bg = "#0f172a"
    card = "#1e293b"
    text = "#e5e7eb"
else:
    bg = "#f9fafb"
    card = "#ffffff"
    text = "#111827"

st.markdown(f"""
<style>
.main {{
    background-color: {bg};
}}
.card {{
    background: {card};
    padding: 30px;
    border-radius: 18px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    color: {text};
}}
.footer {{
    text-align:center;
    margin-top:30px;
    color:gray;
}}
.badge {{
    background-color:#22c55e;
    color:white;
    padding:6px 14px;
    border-radius:20px;
    font-size:14px;
}}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(f"""
<div style="text-align:center; color:{text};">
    <h1>📧 Spam Email Classifier</h1>
    <span class="badge">ML + NLP Project</span>
    <p style="font-size:17px; margin-top:12px;">
        Detect whether an email is <b>Spam</b> or <b>Not Spam</b>
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------- MAIN CARD ----------------
st.markdown("<div class='card'>", unsafe_allow_html=True)

input_email = st.text_area(
    "✉️ Paste your email content below",
    height=180,
    placeholder="Example: Congratulations! You have won a free gift card..."
)

# Email stats
if input_email.strip():
    words = len(input_email.split())
    chars = len(input_email)
    col1, col2 = st.columns(2)
    col1.metric("📝 Word Count", words)
    col2.metric("🔤 Character Count", chars)

st.markdown("<br>", unsafe_allow_html=True)

# Predict button
if st.button("🔍 Predict Email", use_container_width=True):
    if input_email.strip() == "":
        st.warning("⚠️ Please enter an email first.")
    else:
        transformed = transform_text(input_email)
        vectorized = tfidf.transform([transformed])
        prediction = model.predict(vectorized)
        probability = model.predict_proba(vectorized)[0]

        st.markdown("---")

        if prediction[0] == 1:
            st.error("🚨 **SPAM EMAIL DETECTED**")
            st.progress(probability[1])
            st.caption(f"Spam Confidence: **{probability[1]*100:.2f}%**")
        else:
            st.success("✅ **THIS EMAIL IS SAFE (NOT SPAM)**")
            st.progress(probability[0])
            st.caption(f"Not Spam Confidence: **{probability[0]*100:.2f}%**")

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
    © 2026 | Spam Email Classifier | NLP & ML Project
</div>
""", unsafe_allow_html=True)
