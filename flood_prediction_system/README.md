🌊 Flood Prediction System
📌 Overview
Floods are among the most destructive natural disasters, threatening lives, infrastructure, and national security. This project leverages AI-powered predictive analytics to anticipate flood risks in real-time, enabling governments, communities, and emergency responders to act before disaster strikes.

Our system simulates hydrological and meteorological data (rainfall, river level, soil moisture, runoff rate, catchment slope, upstream release) and trains a neural network classifier to predict flood likelihood. It integrates with APIs, localized alerts, and batch scoring tools to deliver actionable insights.

🎯 Problem Statement
Floods cause:

Loss of life and displacement of communities

Damage to infrastructure and agriculture

Strain on emergency services and governance systems

Traditional flood monitoring relies on manual observation and delayed reporting. This project provides real-time, AI-driven flood prediction to strengthen disaster preparedness and national resilience.

✅ Solution
Synthetic & Real Data Support: Works with simulated hydrological data and can integrate Kaggle datasets.

AI Classifier: Neural network trained to predict binary flood risk (safe vs flood likely).

Evaluation Tools: Confusion matrix, ROC curve, and accuracy metrics.

FastAPI Service: REST API for real-time predictions.

Localized Alerts: Messages in English, Swahili, and Kikuyu for citizen engagement.

Batch Scoring CLI: Score entire datasets and export risk levels.

Dockerized Deployment: Ready to run in containerized environments.

🛡️ Alignment with Hackathon Themes
This project directly supports AI for National Prosperity:

Threat Detection & Prevention Floods are national security threats. Our system detects risks in real-time and enables rapid response.

Predictive Analytics Core domain: AI model predicts flood likelihood before disaster occurs.

Governance & Public Policy Transparent decision-making, efficient resource allocation, and public alerts strengthen governance.

Generative & Agentic AI Localized alerts in Swahili/Kikuyu enhance citizen engagement and accessibility.

⚙️ Tech Stack
Python 3.12

TensorFlow / Keras – Neural network classifier

Scikit-learn – Preprocessing, evaluation

FastAPI + Uvicorn – REST API service

Pandas / NumPy – Data simulation and handling

Docker – Deployment-ready containerization

🚀 Quick Start
1. Generate Synthetic Data
bash
python data_simulation.py
2. Train Model
bash
python train.py
3. Evaluate Model
bash
python evaluation.py
4. Run API
bash
python -m uvicorn api:app --host 0.0.0.0 --port 8000
5. Test Prediction
powershell
Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method POST -ContentType "application/json" -Body '{"rainfall":160,"river_level":4.2,"soil_moisture":0.85,"runoff_rate":72,"catchment_slope":9,"upstream_release":1.6,"lang":"sw"}'
6. Batch Scoring
bash
python score_csv.py data/samples.csv --lang sw
📊 Example Output
json
{
  "probability": 0.7256,
  "risk_level": "high",
  "message": "Hatari ya mafuriko ni kubwa. Jiandae.",
  "recommendation": "Issue public alerts, pre-position sandbags, monitor river gauges hourly."
}
🌍 Impact
Disaster Preparedness: Early warnings save lives and reduce economic loss.

National Security: Protects critical infrastructure and supply chains.

Governance: Transparent, data-driven decision-making.

Citizen Engagement: Localized alerts empower communities to act.

📦 Deployment
Build and run with Docker:

bash
docker build -t flood-api .
docker run -p 8000:8000 flood-api
🏆 Hackathon Positioning
This project is a ready-to-go AI solution that demonstrates:

Real-time threat detection

Predictive analytics for sustainable development

Strengthened governance & public policy

Localized citizen engagement

## 📸 Sample Predictions

### Severe Flood Risk (English)
![Severe Flood Risk](screenshots/severe_risk.png)

### High Flood Risk (Swahili)
![High Flood Risk](screenshots/high_risk_swahili.png)

### Low Flood Risk (Kikuyu)
![Low Flood Risk](screenshots/low_risk_kikuyu.png)

Each prediction includes:
- Flood probability (0–1)
- Risk level (low, moderate, high, severe)
- Localized safety message
- Actionable recommendation
