# models/train.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from joblib import dump
import tensorflow as tf
from tensorflow.keras import layers, models

FEATURES = ["rainfall","river_level","soil_moisture","runoff_rate","catchment_slope","upstream_release"]

def load_data(path="data/samples.csv"):
    return pd.read_csv(path)

def build_model(input_dim):
    model = models.Sequential([
        layers.Input(shape=(input_dim,)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dropout(0.2),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

if __name__ == "__main__":
    df = load_data()
    X = df[FEATURES].values
    y = df["flood"].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_val, y_train, y_val = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    model = build_model(X_train.shape[1])
    model.fit(X_train, y_train, epochs=20, batch_size=64, validation_data=(X_val, y_val), verbose=0)

    model.save("models/artifacts/model.keras")
    dump(scaler, "models/artifacts/scaler.pkl")
    loss, acc = model.evaluate(X_val, y_val, verbose=0)
    print(f"Model saved. Val accuracy: {acc:.4f}")
