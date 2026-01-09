# models/evaluate.py
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
from sklearn.preprocessing import StandardScaler
from joblib import load
import matplotlib.pyplot as plt
import tensorflow as tf

FEATURES = ["rainfall","river_level","soil_moisture","runoff_rate","catchment_slope","upstream_release"]

df = pd.read_csv("data/samples.csv")
X = df[FEATURES].values
y = df["flood"].values

scaler = load("models/artifacts/scaler.pkl")
X_scaled = scaler.transform(X)

model = tf.keras.models.load_model("models/artifacts/model.keras")
probs = model.predict(X_scaled, verbose=0).flatten()
preds = (probs > 0.5).astype(int)

print(classification_report(y, preds, digits=4))
print("Confusion matrix:\n", confusion_matrix(y, preds))
print("ROC AUC:", roc_auc_score(y, probs))

RocCurveDisplay.from_predictions(y, probs)
plt.title("ROC Curve")
plt.tight_layout()
plt.savefig("models/artifacts/roc.png")
print("Saved ROC to models/artifacts/roc.png")
