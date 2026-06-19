from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib, numpy as np
import webbrowser
from threading import Timer

app = Flask(__name__)
CORS(app)
model = joblib.load('model/sleep_model.pkl')

tips = {
  'Good': [
    "Excellent! Keep your current sleep routine.",
    "Maintain consistent bed and wake times."
  ],
  'Average': [
    "Reduce screen time 30 mins before bed.",
    "Aim for 7–9 hours of sleep consistently.",
    "Try a short evening walk to wind down."
  ],
  'Poor': [
    "Avoid caffeine after 2 PM.",
    "Try meditation or deep breathing before bed.",
    "Increase physical activity during the day.",
    "Keep your bedroom cool and dark."
  ]
}

@app.route('/')
def home(): return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    d = request.get_json()
    x = np.array([[float(d['sleep_duration']),
                   float(d['physical_activity']),
                   float(d['stress_level']),
                   float(d['heart_rate']),
                   float(d['daily_steps']),
                   float(d['age']),
                   int(d['gender']),
                   int(d['bmi_category'])]])
    pred = model.predict(x)[0]
    conf = round(float(max(model.predict_proba(x)[0])) * 100, 1)
    return jsonify({'quality': pred, 'confidence': conf, 'tips': tips[pred]})

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True)