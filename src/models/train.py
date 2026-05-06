import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Create artifacts folder
os.makedirs("artifacts", exist_ok=True)

# Load dataset
df = pd.read_csv(r"C:\Users\Neel Arora\OneDrive\Desktop\End to End Employee Attrition Prediction\data\raw\Dataset01-Employee_Attrition.csv")

# Convert categorical columns
df = pd.get_dummies(df, drop_first=True)

# Check columns
print(df.columns)

# Features and target
X = df.drop("left", axis=1)
y = df["left"]

# Train model
model = RandomForestClassifier()

model.fit(X, y)

# Save model
joblib.dump(model, "artifacts/model.pkl")

print("✅ Model trained and saved!")
