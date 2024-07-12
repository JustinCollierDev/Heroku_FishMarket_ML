# Lab 4 Heroku - Fish Classification
# By: Justin Collier | 100345263
# Date: 7/12/2024
# Purpose: Creating a simple Python classification model for our fish dataset and exporting it as a usable pickle file.

# [Loading our Libraries]
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier # Library for Random Forest Classification Model
from sklearn.metrics import accuracy_score          # Library for accuracy metrics

# Load the dataset
fish_data = pd.read_csv('Fish.csv')

# Encode the target variable
le = LabelEncoder()
fish_data['Species'] = le.fit_transform(fish_data['Species'])

# Split the data
X = fish_data.drop('Species', axis=1)
y = fish_data['Species']

# Creating the train/test splits (20% test, 80% train)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')

# Save the model (We are going to use this exported pickle file to call the model from our Flask API later)
import joblib
joblib.dump(model, 'fish_classification_model.pkl') # .pkl or pickle file of the model