
🚀 Project Overview

The Spam Email Classifier is a machine learning-powered web application that automatically classifies emails as Spam or Not Spam using Natural Language Processing (NLP) techniques.

The model is trained on a labeled email dataset using TF-IDF vectorization and a supervised learning algorithm, achieving an accuracy of 97.96%.
A clean and interactive Streamlit UI allows users to paste email content and get instant predictions with confidence.

✨ Features

📩 Classifies emails as Spam / Not Spam

🧠 NLP preprocessing (tokenization, stopword removal, stemming)

📊 Model accuracy: 97.96%

📏 Email length & word count analysis

🌙 Dark / Light mode toggle

⚡ Fast and responsive Streamlit UI

☁️ Deployed on Streamlit Cloud

🛠️ Tech Stack
Category	Technologies
Language	Python 3.12
NLP	NLTK
ML	TF-IDF Vectorizer, Naive Bayes
Web UI	Streamlit
Deployment	Streamlit Cloud
Version Control	Git & GitHub
🧠 Machine Learning Workflow

Text Preprocessing

Lowercasing

Tokenization

Stopword removal

Stemming (Porter Stemmer)

Feature Extraction

TF-IDF Vectorization

Model Training

Supervised classification model

Evaluation

Accuracy: 97.96%

📸 Application Preview
<p align="center"> <img src="preview.png" width="700"> </p>
🌐 Live Demo

🔗 Streamlit App:
👉 https://safarwithak-spam-email-detector.streamlit.app/

📦 Installation & Usage
1️⃣ Clone the Repository
git clone https://github.com/SafarwithAK/spam-email-detection.git
cd spam-email-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download NLTK Data
import nltk
nltk.download('punkt')
nltk.download('stopwords')

4️⃣ Run the Application
streamlit run app.py

📁 Project Structure
spam-email-detection/
│
├── app.py                # Streamlit application
├── model.pkl             # Trained ML model
├── vectorizer.pkl        # TF-IDF vectorizer
├── requirements.txt      # Project dependencies
├── preview.png           # App screenshot
└── README.md

🎯 Resume-Ready Description

Developed a Machine Learning based Spam Email Classifier using NLP and TF-IDF vectorization. Built an interactive Streamlit web application for real-time email classification. Achieved 97.96% accuracy and deployed the model on Streamlit Cloud for public access.

👨‍💻 Author

Ajit Kumar
Computer Science Engineer | Full Stack Developer | ML Enthusiast

🔗 GitHub: https://github.com/SafarwithAK

🔗 LinkedIn: https://www.linkedin.com/in/ajit-kumar-36729328a/

📧 Email: ajitkumar09112005@gmail.com

⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork it

🧠 Suggest improvements
