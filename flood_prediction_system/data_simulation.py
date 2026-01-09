# data/simulate.py
import numpy as np
import pandas as pd

def simulate(n=5000, seed=42):
    rng = np.random.default_rng(seed)
    rainfall = rng.normal(120, 40, n)             # mm
    river_level = rng.normal(3.5, 1.0, n)         # m
    soil_moisture = rng.uniform(0, 1, n)          # 0-1
    runoff_rate = rng.normal(50, 15, n)           # mm/hr
    catchment_slope = rng.normal(10, 5, n)        # degrees
    upstream_release = rng.normal(0, 1, n)        # proxy: dam release anomaly

    flood = (
        ((rainfall > 150) & (river_level > 4) & (soil_moisture > 0.8)) |
        (runoff_rate > 70) |
        ((river_level > 4.3) & (upstream_release > 1.5))
    ).astype(int)

    df = pd.DataFrame({
        "rainfall": rainfall,
        "river_level": river_level,
        "soil_moisture": soil_moisture,
        "runoff_rate": runoff_rate,
        "catchment_slope": catchment_slope,
        "upstream_release": upstream_release,
        "flood": flood
    })
    return df

if __name__ == "__main__":
    df = simulate()
    df.to_csv("data/samples.csv", index=False)
    print("Saved data/samples.csv")
