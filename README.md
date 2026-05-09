# Employee Attrition Prediction System

An end-to-end Machine Learning project that predicts whether an employee is likely to leave the company based on HR analytics data. This project covers the complete ML workflow including data preprocessing, model training, prediction pipelines, and deployment using Flask.

---

## 🚀 Project Overview

Employee attrition is one of the biggest challenges faced by organizations. This project uses Machine Learning techniques to analyze employee-related factors and predict attrition probability.

The project includes:

- Data Collection
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training
- Prediction Pipeline
- Flask API Deployment
- Docker Support

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- CatBoost
- Docker
- Git & GitHub

---

## 📂 Project Structure

```bash
End-To-End-Employee-Attrition-Prediction/
│
├── data/
│   └── raw/
│
├── logs/
├── models/
├── notebooks/
├── src/
│   ├── api/
│   ├── config/
│   ├── models/
│   ├── pipelines/
│   ├── utils/
│   ├── predict.py
│   └── __init__.py
│
├── Dockerfile
├── README.md
├── requirements.txt
└── setup.py
```

---

## 📊 Features Used

The model uses multiple employee-related features such as:

- Age
- Department
- Job Role
- Monthly Income
- Work-Life Balance
- Years at Company
- Overtime
- Job Satisfaction
- Environment Satisfaction
- Performance Rating
- Training Times Last Year

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aroraneel/End-To-End-Employee-Attrition-Prediction.git
```

Move to the project directory:

```bash
cd End-To-End-Employee-Attrition-Prediction
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run The Project

Run the Flask application:

```bash
python src/api/app.py
```

Application will run on:

```bash
http://127.0.0.1:5000
```

---

## 🐳 Docker Setup

Build Docker image:

```bash
docker build -t employee-attrition .
```

Run Docker container:

```bash
docker run -p 5000:5000 employee-attrition
```

---

## 📈 Machine Learning Workflow

1. Data Collection  
2. Data Cleaning  
3. Exploratory Data Analysis  
4. Feature Engineering  
5. Model Training  
6. Model Evaluation  
7. Prediction Pipeline  
8. Flask Deployment  

---

## 🎯 Project Goal

The objective of this project is to:

- Reduce employee attrition
- Help HR teams make better decisions
- Identify employees at high risk of leaving
- Improve workforce management using Machine Learning

---

## 📸 Project Preview

You can add screenshots of:

- Flask Web Interface
- Prediction Results
- EDA Visualizations

Example path:

```bash
notebooks/images/project_preview.png
```

---

## 📦 Requirements

Main libraries used:

```txt
pandas
numpy
scikit-learn
flask
catboost
matplotlib
seaborn
```

---

## 🤝 Contributing

Contributions are welcome.

Steps to contribute:

1. Fork the repository  
2. Create a new branch  
3. Commit your changes  
4. Push to GitHub  
5. Open a Pull Request  

---

## 👨‍💻 Author

### Neel Arora

AI/ML Enthusiast passionate about building intelligent predictive systems using Machine Learning, Data Analytics, and modern technologies.

Focused on developing real-world AI solutions with scalable and production-ready workflows.

⭐ If you found this project useful, feel free to star the repository.