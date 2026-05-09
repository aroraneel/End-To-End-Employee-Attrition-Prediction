# Employee Attrition Prediction System

An end-to-end Machine Learning project that predicts whether an employee is likely to leave the company based on HR analytics data. This project covers the complete ML workflow including data preprocessing, model training, evaluation, prediction pipelines, and deployment using Streamlit.

---

## 🚀 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. This project uses Machine Learning techniques to analyze employee-related factors and predict attrition probability.

The project includes:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training & Evaluation (Accuracy, F1, ROC-AUC)
- Prediction Pipeline
- Streamlit Web App Deployment
- Docker Support

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Docker
- Git & GitHub

---

## 📂 Project Structure

```bash
End-To-End-Employee-Attrition-Prediction/
│
├── data/
│   └── raw/                  # Raw CSV dataset
│
├── logs/                     # Training and inference logs
├── models/                   # Saved model artifacts
├── notebooks/                # EDA notebook
├── src/
│   ├── api/
│   │   └── app.py            # Streamlit web application
│   ├── config/
│   │   └── config.py         # Central path configuration
│   ├── models/
│   │   ├── train.py          # Model training + evaluation
│   │   └── predict.py        # Model loading + prediction
│   ├── pipelines/
│   │   ├── training_pipeline.py    # Training entry point
│   │   └── inference_pipeline.py   # Inference entry point
│   ├── utils/
│   │   └── logger.py         # File-based logging setup
│   └── __init__.py
│
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── setup.py
```

---

## 📊 Features Used

The model uses the following employee-related features:

- Satisfaction Level
- Last Evaluation Score
- Number of Projects
- Average Monthly Hours
- Years at Company
- Work Accident (Yes/No)
- Promotion in Last 5 Years (Yes/No)
- Department
- Salary Level (Low / Medium / High)

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aroraneel/End-To-End-Employee-Attrition-Prediction.git
cd End-To-End-Employee-Attrition-Prediction
```

Create and activate a virtual environment:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -e .
```

---

## ▶️ Run The Project

### 1. Train the model

```bash
python src/pipelines/training_pipeline.py
```

This will print evaluation metrics (Accuracy, F1, ROC-AUC) and save the model to `models/model.pkl`.

### 2. Launch the Streamlit app

```bash
streamlit run src/api/app.py
```

Application will open at:

```
http://localhost:8501
```

---

## 🐳 Docker Setup

Build the Docker image:

```bash
docker build -t employee-attrition .
```

Run the container:

```bash
docker run -p 8501:8501 employee-attrition
```

Open in browser:

```
http://localhost:8501
```

---

## 📈 Machine Learning Workflow

1. Data Loading & Cleaning
2. Exploratory Data Analysis (see `notebooks/EDA.ipynb`)
3. Feature Engineering (`pd.get_dummies` encoding)
4. Train / Test Split (80/20, stratified)
5. Model Training (`RandomForestClassifier`)
6. Model Evaluation (Accuracy, F1, ROC-AUC, Confusion Matrix)
7. Model Serialization (`joblib`)
8. Streamlit Deployment

---

## 🎯 Project Goal

- Reduce employee attrition by enabling early identification of at-risk employees
- Help HR teams make data-driven decisions
- Demonstrate a production-style end-to-end ML project structure

---

## 📦 Requirements

```
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
matplotlib>=3.6.0
seaborn>=0.12.0
streamlit>=1.28.0
joblib>=1.2.0
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to GitHub (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

### Neel Arora

AI/ML Enthusiast passionate about building intelligent predictive systems using Machine Learning, Data Analytics, and modern technologies.

⭐ If you found this project useful, feel free to star the repository.
