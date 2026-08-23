from flask import Flask, render_template, request
import pickle
import os
import nltk

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

from preprocess import preprocess

# ---------------------------------------
# Flask Configuration
# ---------------------------------------

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

# ---------------------------------------
# Load Model Files
# ---------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models", "svm_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "models", "tfidf_vectorizer.pkl")
LABEL_MAP_PATH = os.path.join(BASE_DIR, "models", "label_map.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

with open(VECTORIZER_PATH, "rb") as f:
    vectorizer = pickle.load(f)

with open(LABEL_MAP_PATH, "rb") as f:
    label_map = pickle.load(f)

print("Model Classes :", model.classes_)
print("Label Map     :", label_map)
print(model)

# ---------------------------------------
# Home Route
# ---------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------------------------------
# Prediction Route
# ---------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    user_text = request.form["text"]

    cleaned_text = preprocess(user_text)

    vector = vectorizer.transform([cleaned_text])

    # Prediction
    predicted_class = model.predict(vector)[0]
    predicted_emotion = label_map[predicted_class]

    # Probabilities
    import numpy as np

    scores = model.decision_function(vector)[0]

    # Convert decision scores into percentages
    exp_scores = np.exp(scores - np.max(scores))
    probabilities = exp_scores / exp_scores.sum()

    print("\n-----------------------------")
    print("Predicted Class :", predicted_class)
    print("Predicted Emotion :", predicted_emotion)
    print("Model Classes :", model.classes_)
    print("Probabilities :", probabilities)

    probability_dict = {}

    # IMPORTANT: use model.classes_
    for class_id, prob in zip(model.classes_, probabilities):

        emotion = label_map[class_id]

        probability_dict[emotion] = round(prob * 100, 2)

        print(
            f"{class_id} -> {emotion} : {round(prob*100,2)}%"
        )

    # sort highest first
    probability_dict = dict(
        sorted(
            probability_dict.items(),
            key=lambda x: x[1],
            reverse=True
        )
    )

    confidence = round(max(probabilities) * 100, 2)

    return render_template(
        "index.html",
        input_text=user_text,
        prediction=predicted_emotion,
        confidence=confidence,
        probabilities=probability_dict
    )


# ---------------------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)