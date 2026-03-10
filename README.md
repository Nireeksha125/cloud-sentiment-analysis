# Cloud Sentiment Analysis System

This project is a **Cloud-Based Sentiment Analysis System** built using **Natural Language Processing (NLP)** and **Machine Learning (ML)**.
The system analyzes user text and predicts whether the sentiment is **Positive or Negative**.

The application is fully deployed using **cloud technologies**.

---

# Live Demo

Streamlit Cloud App
https://cloud-sentiment-analysis.streamlit.app

---

# Features

• Sentiment classification (Positive / Negative)
• Machine Learning model using Logistic Regression
• REST API using Flask
• Interactive Web Interface using Streamlit
• Cloud deployment using Render and Streamlit Cloud
• Prediction data stored in MongoDB Atlas

---

# Technologies Used

• Python
• Scikit-learn
• Flask
• Streamlit
• NLP (TF-IDF Vectorization)
• MongoDB Atlas
• Render Cloud
• GitHub

---

# Project Architecture

User → Streamlit Cloud (Frontend) → Flask API on Render → ML Model → MongoDB Atlas → Sentiment Result

---

# Dataset

Dataset: Sentiment140
Source: Kaggle
Link: https://www.kaggle.com/datasets/kazanova/sentiment140
Dataset contains tweets labeled as positive or negative sentiments.

---

# Cloud Deployment

Frontend
Streamlit Cloud

Backend API
Render Cloud

Database
MongoDB Atlas

Version Control
GitHub

---

# Project Workflow

1. User enters text in the Streamlit web interface
2. The request is sent to the Flask API hosted on Render
3. The API processes the text using the trained ML model
4. The model predicts the sentiment (Positive / Negative)
5. The result is returned to the user interface
6. The prediction is stored in MongoDB Atlas

---

# Installation (Local Setup)

Clone the repository

git clone https://github.com/Nireeksha125/cloud-sentiment-analysis.git

Navigate to project directory

cd cloud-sentiment-analysis

Install dependencies

pip install -r requirements.txt

Run Streamlit app

streamlit run frontend/streamlit_app.py

---

# Author

Nireeksha B V
