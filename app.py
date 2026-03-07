from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return "AI Symptom Analyzer API Running"

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Please provide symptom text"}), 400

    text = data["text"]

    # Transform text using NLP
    text_vec = vectorizer.transform([text])

    # Predict category
    prediction = model.predict(text_vec)[0]

    return jsonify({
        "symptoms": text,
        "predicted_category": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)