# 1. Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import os

# 2. Load your cleaned dataset
data_path = os.path.join('..', 'data', 'cleaned_network_data.csv')
data = pd.read_csv(data_path)

# Clean column names automatically (recommended way)
data.columns = data.columns.str.strip()


print("✅ Data loaded successfully")
print(data.head())

# 3. Preprocess the data

# Create the target variable
# Threshold: top 10% disconnection counts are 'high risk'
threshold = data['Disconnection Counts'].quantile(0.90)
data['HighRiskDisconnect'] = (data['Disconnection Counts'] > threshold).astype(int)

# Features we want to use
features = [
    'Download Speed (Mbps)',
    'Latency (ms)',
    'Packet Loss (%)',
    'hour',
    'month'
]

X = data[features]
y = data['HighRiskDisconnect']

# 4. Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 6. Evaluate the model
y_pred = model.predict(X_test)

print("✅ Model training complete.\n")

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 7. (Optional) Feature importance
importances = model.feature_importances_
feat_names = X.columns

importance_df = pd.DataFrame({'Feature': feat_names, 'Importance': importances})
importance_df = importance_df.sort_values('Importance', ascending=False)

print("\nFeature Importance:")
print(importance_df)

# 8. Save the model for Streamlit
import joblib

# Create models directory if not exists
os.makedirs('../models', exist_ok=True)

model_save_path = os.path.join('..', 'models', 'disconnect_risk_model.pkl')
joblib.dump(model, model_save_path)

print(f"✅ Model saved to {model_save_path}")
