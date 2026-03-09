import streamlit as st
import requests

st.title("Cloud Sentiment Analysis System")

st.write("Enter a sentence to analyze sentiment")

text = st.text_input("Your text:")

if st.button("Predict Sentiment"):

    if text.strip() != "":

        response = requests.post(
            "https://cloud-sentiment-analysis.onrender.com/predict",
            json={"text": text}
        )

        result = response.json()

        st.success("Sentiment: " + result["sentiment"])