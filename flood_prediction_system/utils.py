# app/utils.py
import numpy as np
from joblib import load
import tensorflow as tf

FEATURES = ["rainfall","river_level","soil_moisture","runoff_rate","catchment_slope","upstream_release"]

class FloodModel:
    def __init__(self, model_path="models/artifacts/model.keras", scaler_path="models/artifacts/scaler.pkl"):
        self.scaler = load(scaler_path)
        self.model = tf.keras.models.load_model(model_path)

    def predict_proba(self, payload):
        x = np.array([[payload[f] for f in FEATURES]], dtype=float)
        x_scaled = self.scaler.transform(x)
        p = float(self.model.predict(x_scaled, verbose=0).flatten()[0])
        return p
