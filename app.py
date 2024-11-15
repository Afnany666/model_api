from flask import Flask, request, jsonify
import joblib
import numpy as np

# Inisialisasi Flask app
app = Flask(__name__)

# Muat model dari file
model = joblib.load("model_rekomendasi_olahraga.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        # Misalnya data input berupa list
        input_data = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(input_data)
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
