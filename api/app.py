import sys
import os

# allow Python to find predict.py in parent folder
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from predict import predict_sentiment

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()
    text = data["text"]

    result = predict_sentiment(text)

    return jsonify({
        "sentiment": result
    })


if __name__ == "__main__":
    app.run(debug=True)