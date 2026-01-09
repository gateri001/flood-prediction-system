# app/alerts.py
def risk_level(prob):
    if prob >= 0.85: return "severe"
    if prob >= 0.65: return "high"
    if prob >= 0.40: return "moderate"
    return "low"

def recommendation(level):
    mapping = {
        "severe": "Initiate evacuation, close low bridges, deploy rescue assets.",
        "high": "Issue public alerts, pre-position sandbags, monitor river gauges hourly.",
        "moderate": "Increase monitoring, prepare shelters, inform local leaders.",
        "low": "Routine monitoring; no immediate action."
    }
    return mapping[level]
