from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
texts = [
    "There is garbage on the road",
    "Huge pothole in street",
    "Water leakage from pipeline",
    "Street light not working",
    "Garbage not collected"
]

labels = [
    "Garbage",
    "Pothole",
    "Water Issue",
    "Electric Issue",
    "Garbage"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_category(text):
    text_vector = vectorizer.transform([text])
    prediction = model.predict(text_vector)
    return prediction[0]