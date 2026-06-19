import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score
import joblib

df = pd.read_csv('data/sleep_data.csv')

def label_quality(score):
    if score >= 7: return 'Good'
    elif score >= 5: return 'Average'
    else: return 'Poor'

df['Label'] = df['Quality of Sleep'].apply(label_quality)

le_g = LabelEncoder(); le_b = LabelEncoder(); le_d = LabelEncoder()
df['Gender']        = le_g.fit_transform(df['Gender'])
df['BMI Category'] = le_b.fit_transform(df['BMI Category'])
df['Sleep Disorder'] = le_d.fit_transform(df['Sleep Disorder'].fillna('None'))

features = ['Sleep Duration', 'Physical Activity Level',
            'Stress Level', 'Heart Rate',
            'Daily Steps', 'Age', 'Gender', 'BMI Category']

X = df[features]
y = df['Label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2%}")
print(classification_report(y_test, y_pred))

joblib.dump(model, 'model/sleep_model.pkl')
print("Model saved!")