# Medi-Buddy: Smart Disease Predictor

A machine learning-powered web application that predicts the risk of multiple diseases including breast cancer, diabetes, heart disease, and Parkinson's disease. Medi-Buddy leverages trained ML models to provide quick and accessible health risk assessments based on user-provided medical parameters.

## Features

- 🏥 **Multi-Disease Prediction**: Predict risk for 4 major diseases
  - Breast Cancer Classification
  - Diabetes Prediction
  - Heart Disease Risk Assessment
  - Parkinson's Disease Detection

- 💻 **User-Friendly Web Interface**: Interactive web application with form-based input
- 🤖 **Pre-trained ML Models**: Fast inference using optimized scikit-learn models
- 📊 **Accurate Predictions**: Models trained on real medical datasets
- 🔒 **Privacy-Focused**: Processes data locally without external API calls

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Framework**: scikit-learn
- **Data Processing**: Pandas, NumPy
- **Model Serialization**: Pickle

## Project Structure

```
Medi-Buddy-Smart-Disease-Predictor/
├── app/
│   └── app.py                    # Flask application server
├── data/
│   ├── breast_cancer.csv         # Training dataset
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
├── models/
│   ├── breast_cancer_model.sav   # Pre-trained model
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── notebooks/
│   ├── MiniProjectBreastCancer.ipynb   # Model development notebooks
│   ├── MiniProjectDiabetes.ipynb
│   ├── MiniProjectHeart.ipynb
│   └── MiniProjectParkinsons.ipynb
├── static/
│   ├── css/
│   │   └── style.css             # Styling for web interface
│   ├── html/
│   │   ├── index.html            # Home page
│   │   ├── breast-cancer.html
│   │   ├── diabetes.html
│   │   ├── heart.html
│   │   └── parkinsons.html
│   └── js/
│       ├── script.js             # Main JavaScript logic
│       ├── breast-cancer.js
│       ├── diabetes.js
│       ├── heart.js
│       └── parkinsons.js
└── README.md
```

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/TheKingKJ/Medi-Buddy-Smart-Disease-Predictor.git
   cd Medi-Buddy-Smart-Disease-Predictor
   ```

2. **Install Dependencies**
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

3. **Start the Flask Server**
   ```bash
   cd app
   python app.py
   ```

4. **Access the Web Interface**
   - Open your browser and navigate to `http://localhost:5000`

## Usage

1. **Select a Disease Prediction**
   - Choose from Breast Cancer, Diabetes, Heart Disease, or Parkinson's
   
2. **Enter Medical Parameters**
   - Fill in the required medical metrics (varies by disease)
   
3. **Get Prediction**
   - Click the predict button to receive risk assessment
   
4. **View Results**
   - Results display the predicted outcome and confidence

## Diseases Covered

### Breast Cancer
- Binary classification (Malignant/Benign)
- Features: Cell characteristics from biopsy data

### Diabetes
- Binary classification (Diabetic/Non-Diabetic)
- Features: Medical measurements and health indicators

### Heart Disease
- Binary classification (Heart Disease/No Disease)
- Features: Cardiovascular health indicators

### Parkinson's Disease
- Binary classification (Parkinson's/Healthy)
- Features: Voice and speech characteristics

## Model Development

Each disease predictor was developed through:
- **Data Analysis**: Exploratory data analysis in Jupyter notebooks
- **Feature Engineering**: Selection and preprocessing of relevant features
- **Model Training**: Using scikit-learn algorithms (Logistic Regression, Random Forest, SVM, etc.)
- **Model Serialization**: Saving trained models as `.sav` files for deployment

View the development process in the `notebooks/` directory.

## Performance

Models are trained on established medical datasets and validated for accuracy. Refer to individual notebooks for detailed performance metrics and evaluation results.

## Disclaimer

⚠️ **Medical Disclaimer**: This application is for educational and informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs and issues
- Suggest improvements
- Submit pull requests

## License

This project is open-source and available under the MIT License.

## Author

Created by TheKingKJ

## Acknowledgments

- Medical datasets from public health data repositories
- scikit-learn library for machine learning
- Flask framework for web development