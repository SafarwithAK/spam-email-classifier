📧 Spam Email Classifier

A Machine Learning based Spam Email Detection System that classifies emails as Spam or Not Spam using Natural Language Processing (NLP) techniques.
The model is trained on labeled email data and deployed with a simple Streamlit web interface for real-time predictions.

🚀 Features

Detects Spam / Ham (Not Spam) emails

Uses NLP text preprocessing

Trained Machine Learning model

Real-time prediction using Streamlit UI

Displays prediction confidence

Lightweight and easy to deploy

🛠️ Technologies Used

Python

Scikit-learn

NLTK

Pandas & NumPy

Streamlit

Pickle (Model Serialization)

🧠 Machine Learning Workflow

Data Cleaning

Text Preprocessing

Lowercasing

Tokenization

Stopword Removal

Stemming

Feature Extraction (TF-IDF Vectorizer)

Model Training

Model Evaluation

Web App Deployment

📊 Model Performance

Accuracy: 97.96%

Optimized for high precision in spam detection

Reliable classification on unseen emails

📂 Project Structure
spam-email-classifier/
│
├── app.py                  # Streamlit web application
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # TF-IDF vectorizer
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
└── dataset/                # Training dataset (optional)

▶️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/SafarwithAK/spam-email-detection.git
cd spam-email-detection

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Download NLTK Resources
import nltk
nltk.download('punkt')
nltk.download('stopwords')

4️⃣ Run the Application
streamlit run app.py

🌐 Live Demo

👉 Live App:
https://safarwithak-spam-email-detector.streamlit.app/

📸 Application Preview

Text input for email content

Predict button

Spam / Not Spam result

Confidence score displayed

👨‍💻 Author

Ajit Kumar
Computer Science Student | Full Stack Developer

GitHub: SafarwithAK

LinkedIn: Ajit Kumar

Email: ajitkumar09112005@gmail.com

⭐ Acknowledgements

Scikit-learn Documentation

NLTK Library

Streamlit Community
