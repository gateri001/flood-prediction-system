# cli/score_csv.py
import argparse
import pandas as pd
from joblib import load
import tensorflow as tf
import numpy as np

FEATURES = ["rainfall","river_level","soil_moisture","runoff_rate","catchment_slope","upstream_release"]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--lang", default="en")
    args = parser.parse_args()

    scaler = load("models/artifacts/scaler.pkl")
    model = tf.keras.models.load_model("models/artifacts/model.keras")

    df = pd.read_csv(args.csv)
    X = df[FEATURES].values
    Xs = scaler.transform(X)
    probs = model.predict(Xs, verbose=0).flatten()

    out = df.copy()
    out["probability"] = probs
    out["risk_level"] = pd.cut(
        probs, bins=[-1,0.4,0.65,0.85,2],
        labels=["low","moderate","high","severe"]
    )
    out.to_csv("scored.csv", index=False)
    print("Saved scored.csv")

if __name__ == "__main__":
    main()
