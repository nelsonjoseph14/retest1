# app.py
from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    # Example: if dataset has 4 features
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text=f'Prediction: {prediction[0]}')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
