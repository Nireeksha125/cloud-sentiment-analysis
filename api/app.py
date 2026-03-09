import sys
import os

# allow Python to find predict.py in parent folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from predict import predict_sentiment

# MongoDB import
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb+srv://Nireeksha:Niru%402005@cluster0.y48uz7m.mongodb.net/?appName=Cluster0")
db = client["sentiment_db"]
collection = db["predictions"]

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    text = data["text"]

    result = predict_sentiment(text)

    # Save prediction to MongoDB
    collection.insert_one({
        "text": text,
        "sentiment": result
    })

    return jsonify({
        "sentiment": result
    })


if __name__ == "__main__":
    app.run(debug=True)