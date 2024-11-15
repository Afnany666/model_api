from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model_rekomendasi_olahraga.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        prediction = model.predict([data])
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
