import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# load dataset
data = pd.read_csv(
    "dataset/training.1600000.processed.noemoticon.csv",
    encoding="latin-1",
    header=None
)

# select only sentiment and text columns
data = data[[0,5]]

data.columns = ["sentiment","text"]

# convert 4 → positive(1)
data["sentiment"] = data["sentiment"].replace(4,1)

X = data["text"]
y = data["sentiment"]

vectorizer = TfidfVectorizer(stop_words="english")

X_vector = vectorizer.fit_transform(X)

X_train,X_test,y_train,y_test = train_test_split(
    X_vector,y,test_size=0.2
)

model = LogisticRegression()

model.fit(X_train,y_train)

# save model
pickle.dump(model,open("model.pkl","wb"))
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))

print("Model trained successfully")