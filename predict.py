import pickle

# load model
model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def predict_sentiment(text):

    text_vector = vectorizer.transform([text])

    prediction = model.predict(text_vector)

    if prediction[0] == 1:
        return "Positive"
    else:
        return "Negative"


# test prediction
if __name__ == "__main__":
    
    user_input = input("Enter a sentence: ")

    result = predict_sentiment(user_input)

    print("Sentiment:", result)