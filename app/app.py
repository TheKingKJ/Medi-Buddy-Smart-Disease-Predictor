from flask import Flask, render_template, request, jsonify
import pickle
import os
import numpy as np
from pathlib import Path

app = Flask(__name__, 
            template_folder='../static/html',
            static_folder='../static')

# Load models
base_dir = Path(__file__).resolve().parent.parent / "models"

try:
    diabetes_model = pickle.load(open(base_dir / "diabetes_model.sav", 'rb'))
    heart_disease_model = pickle.load(open(base_dir / "heart_disease_model.sav", 'rb'))
    parkinsons_model = pickle.load(open(base_dir / "parkinsons_model.sav", 'rb'))
    breast_cancer_model = pickle.load(open(base_dir / "breast_cancer_model.sav", 'rb'))
except FileNotFoundError as e:
    print(f"Model files not found: {e}. Please ensure model files are in the 'models' directory.")
    # Initialize models as None to handle cases where they might not be loaded
    diabetes_model = None
    heart_disease_model = None
    parkinsons_model = None
    breast_cancer_model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/static/html/index.html')
def home_html():
    return render_template('index.html')

@app.route('/static/html/diabetes.html')
def diabetes():
    return render_template('diabetes.html')

@app.route('/static/html/heart.html')
def heart():
    return render_template('heart.html')

@app.route('/static/html/parkinsons.html')
def parkinsons():
    return render_template('parkinsons.html')

@app.route('/static/html/breast-cancer.html')
def breast_cancer():
    return render_template('breast-cancer.html')

@app.route('/predict/diabetes', methods=['POST'])
def predict_diabetes():
    if diabetes_model is None:
        return jsonify({"error": "Diabetes model not loaded. Please check server logs."})
    
    try:
        # Get values from form
        features = [
            float(request.form['pregnancies']),
            float(request.form['glucose']),
            float(request.form['bloodpressure']),
            float(request.form['skinthickness']),
            float(request.form['insulin']),
            float(request.form['bmi']),
            float(request.form['diabetespedigree']),
            float(request.form['age'])
        ]
        
        # Log the features for debugging
        print(f"Features received: {features}")
        
        # Make prediction
        prediction = diabetes_model.predict([features])
        
        # Log the prediction
        print(f"Prediction result: {prediction}")
        
        result = "The person is diabetic" if prediction[0] == 1 else "The person is not diabetic"
        
        return jsonify({"result": result})
    except Exception as e:
        import traceback
        print(f"Error in predict_diabetes: {str(e)}")
        print(traceback.format_exc())
        return jsonify({"error": str(e)})

@app.route('/predict/heart', methods=['POST'])
def predict_heart():
    try:
        features = [
            float(request.form['age']),
            float(request.form['sex']),
            float(request.form['cp']),
            float(request.form['trestbps']),
            float(request.form['chol']),
            float(request.form['fbs']),
            float(request.form['restecg']),
            float(request.form['thalach']),
            float(request.form['exang']),
            float(request.form['oldpeak']),
            float(request.form['slope']),
            float(request.form['ca']),
            float(request.form['thal'])
        ]
        
        prediction = heart_disease_model.predict([features])
        
        result = "The person is having heart disease" if prediction[0] == 1 else "The person does not have any heart disease"
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/predict/parkinsons', methods=['POST'])
def predict_parkinsons():
    try:
        features = [
            float(request.form['fo']),
            float(request.form['fhi']),
            float(request.form['flo']),
            float(request.form['jitter_percent']),
            float(request.form['jitter_abs']),
            float(request.form['rap']),
            float(request.form['ppq']),
            float(request.form['ddp']),
            float(request.form['shimmer']),
            float(request.form['shimmer_db']),
            float(request.form['apq3']),
            float(request.form['apq5']),
            float(request.form['apq']),
            float(request.form['dda']),
            float(request.form['nhr']),
            float(request.form['hnr']),
            float(request.form['rpde']),
            float(request.form['dfa']),
            float(request.form['spread1']),
            float(request.form['spread2']),
            float(request.form['d2']),
            float(request.form['ppe'])
        ]
        
        prediction = parkinsons_model.predict([features])
        
        result = "The person has Parkinson's disease" if prediction[0] == 1 else "The person does not have Parkinson's disease"
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/predict/breast-cancer', methods=['POST'])
def predict_breast_cancer():
    try:
        features = [
            float(request.form['mean_radius']),
            float(request.form['mean_texture']),
            float(request.form['mean_perimeter']),
            float(request.form['mean_area']),
            float(request.form['mean_smoothness']),
            float(request.form['mean_compactness']),
            float(request.form['mean_concavity']),
            float(request.form['mean_concave_points']),
            float(request.form['mean_symmetry']),
            float(request.form['mean_fractal_dimension']),
            float(request.form['radius_error']),
            float(request.form['texture_error']),
            float(request.form['perimeter_error']),
            float(request.form['area_error']),
            float(request.form['smoothness_error']),
            float(request.form['compactness_error']),
            float(request.form['concavity_error']),
            float(request.form['concave_points_error']),
            float(request.form['symmetry_error']),
            float(request.form['fractal_dimension_error']),
            float(request.form['worst_radius']),
            float(request.form['worst_texture']),
            float(request.form['worst_perimeter']),
            float(request.form['worst_area']),
            float(request.form['worst_smoothness']),
            float(request.form['worst_compactness']),
            float(request.form['worst_concavity']),
            float(request.form['worst_concave_points']),
            float(request.form['worst_symmetry']),
            float(request.form['worst_fractal_dimension'])
        ]
        
        prediction = breast_cancer_model.predict([features])
        
        result = "Breast Cancer is Malignant" if prediction[0] == 0 else "Breast Cancer is Benign"
        
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
    