# 🌙 Sleep Quality Predictor

A Machine Learning–powered web application that analyzes daily lifestyle and physiological habits — sleep duration, stress level, physical activity, screen time, and more — to predict sleep quality as **Good**, **Average**, or **Poor**, and delivers personalized tips to help you sleep better.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?logo=flask&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📖 Overview

Sleep is essential for physical and mental well-being, and poor sleep quality is linked to stress, obesity, heart disease, and reduced productivity. This project applies supervised machine learning to lifestyle and health data to classify a person's sleep quality and surface actionable, personalized recommendations — turning raw daily habits into a clear, useful signal.

The model is trained on the **Sleep Health and Lifestyle Dataset**, learning the relationship between factors like sleep duration, stress, exercise, and heart rate, and the resulting quality of sleep.

---

## ✨ Features

- 🔮 Predicts sleep quality (Good / Average / Poor) from daily lifestyle inputs
- 📝 Captures sleep duration, bedtime, wake-up time, stress level, exercise, screen time, caffeine intake, mood, and more
- 🧠 Trained and benchmarked across four supervised ML algorithms
- 💡 Returns personalized, category-specific tips to improve sleep
- 📊 Displays prediction confidence as a live percentage
- 🎨 Clean, animated, dark-themed responsive web interface
- 🔌 Lightweight Flask REST API powering real-time predictions

---

## 🖥️ Screenshots

<img width="1361" height="717" alt="image" src="https://github.com/user-attachments/assets/8d6a16de-c420-4eb2-9742-ded9edd11581" />

<img width="1361" height="715" alt="image" src="https://github.com/user-attachments/assets/6f8917c4-d4b6-4776-92e7-68da4ad5d731" />

<img width="1365" height="718" alt="image" src="https://github.com/user-attachments/assets/d16197df-6925-44a7-a127-4dac7af19e93" />


## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| ML / Data | scikit-learn, pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Backend | Flask, Flask-CORS |
| Model Persistence | joblib |
| Frontend | HTML5, CSS3, vanilla JavaScript |

### Algorithms Evaluated
- Logistic Regression
- Random Forest *(deployed model)*
- Decision Tree
- Support Vector Machine (SVM)

---

## 📂 Dataset

**Sleep Health and Lifestyle Dataset** (374 records) — includes:

`Sleep Duration` · `Quality of Sleep` · `Physical Activity Level` · `Stress Level` · `Heart Rate` · `Daily Steps` · `BMI Category` · `Age` · `Gender` · `Sleep Disorder`

Source: [Kaggle – Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

---

## 📈 Model Performance

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Logistic Regression | 77.3% | 0.78 | 0.77 | 0.77 |
| **Random Forest** *(deployed)* | 73.3% | 0.74 | 0.73 | 0.73 |
| Decision Tree | 76.0% | 0.78 | 0.76 | 0.76 |
| SVM | 52.0% | 0.27 | 0.52 | 0.36 |

**Key insight:** Sleep Duration and Stress Level are the two strongest predictors of sleep quality, followed by Physical Activity Level and Daily Steps.

> Random Forest was selected for deployment for its robustness and built-in feature importance ranking, despite Logistic Regression scoring marginally higher on this dataset size.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/sleep-quality-predictor.git
cd sleep-quality-predictor

# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Train the model

```bash
python model/train_model.py
```

This trains a Random Forest classifier on `data/sleep_data.csv` and saves the model to `model/sleep_model.pkl`.

### Run the app

```bash
python app.py
```

Open your browser at **http://localhost:5000** 🎉

---

## 📁 Project Structure

```
sleep-quality-predictor/
├── model/
│   ├── train_model.py       # Model training script
│   └── sleep_model.pkl      # Trained model (generated)
├── data/
│   └── sleep_data.csv       # Training dataset
├── templates/
│   └── index.html           # Frontend UI
├── app.py                   # Flask backend & prediction API
├── requirements.txt
└── README.md
```

---

## 🔌 API Reference

**POST** `/predict`

```json
{
  "sleep_duration": 7.5,
  "physical_activity": 30,
  "stress_level": 5,
  "heart_rate": 72,
  "daily_steps": 7500,
  "age": 25,
  "gender": 1,
  "bmi_category": 1
}
```

**Response**

```json
{
  "quality": "Good",
  "confidence": 82.0,
  "tips": [
    "Excellent! Keep your current sleep routine.",
    "Maintain consistent bed and wake times."
  ]
}
```

---

## 🛣️ Roadmap

- [ ] Sleep history tracking & trend charts
- [ ] Wearable device integration (Fitbit / Apple Health)
- [ ] NLP-based sleep diary analysis
- [ ] Dark/light theme toggle
- [ ] Deploy to Render / Railway

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/your-username/sleep-quality-predictor/issues).


---

## 🙏 Acknowledgements

- [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset) on Kaggle
- Built with [scikit-learn](https://scikit-learn.org/) and [Flask](https://flask.palletsprojects.com/)# Sleep_quality_Predictor-
AI-powered sleep quality prediction system built with Flask, Scikit-Learn, and SQLite, featuring personalized recommendations and analytics dashboard

---
## Project Owner 
    BY Janani S

