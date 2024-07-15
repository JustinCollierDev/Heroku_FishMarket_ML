# Lab 4 Heroku - Fish Classification
# By: Justin Collier | 100345263
# Date: 7/12/2024
# Purpose: Flask App/Backend for our fish classifcation web app.

# [Loading our Libraries]
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the model and LabelEncoder
model = joblib.load('fish_classification_model.pkl') # (This is where we load our model's pickle file)
le = joblib.load('label_encoder.pkl')                # We also load a label encoder from 'joblib' to encode the species labels.

# Handling the landing page of our web app
@app.route('/')
def home():
    return render_template('index.html')

# Handle the /predict route of our web app
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(request.form['Weight']),   # We pull the form submission data by requesting the variable via name ex. 'Weight'
            float(request.form['Vertical Length']),
            float(request.form['Diagonal Length']),
            float(request.form['Cross Length']),
            float(request.form['Height']),
            float(request.form['Width'])]
    # Running our classification model with the data.
    prediction = model.predict([data]) 
    species = le.inverse_transform(prediction)
    return jsonify({'prediction': species[0]}) # Return the outcome

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
