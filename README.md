# Phishing URL Detection System (MLOps + FastAPI + MLflow/DagsHub)

An end-to-end machine learning system to classify URLs as **phishing or legitimate** using engineered URL-based features.  
Includes modular ML pipelines (ingestion → transformation → training → prediction), experiment tracking with **MLflow + DagsHub**, and deployment via **FastAPI**.

---

## 🚀 Key Features
- Modular pipeline architecture: **Data Ingestion → Data Transformation → Model Training**
- Trains & compares multiple ML models:
  - RandomForest  
  - GradientBoosting  
  - Logistic Regression  
  - AdaBoost
- Experiment tracking with **MLflow + DagsHub**
- REST API deployment using **FastAPI**:
  - `GET /train` → trains the model  
  - `POST /predict` → uploads CSV and returns predictions
- Generates all artifacts: processed data, models, scalers, reports

---

## 🧰 Tech Stack
- **Python**
- Pandas, NumPy  
- Scikit-learn  
- FastAPI, Uvicorn  
- MLflow  
- DagsHub  
- PyYAML  
- MongoDB

---

## 📦 Dataset
Dataset contains extracted URL features and a binary column:

- **Target column:** `Result`  
  - `1` → phishing  
  - `-1` → legitimate  

---

## 📁 Project Structure
```
Phising-URL-Detection-System/
│
├── app.py
├── final_model/
│   └── model.pkl
├── artifacts/
├── networksecurity/
│   ├── components/
│   ├── config/
│   ├── pipeline/
│   ├── utils.py
│   └── ...
├── requirements.txt
└── README.md
```

---

# 🛠️ Installation & Setup

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/ishantyagii/Phising-URL-Detection-System.git
cd Phising-URL-Detection-System
```

---

## 2️⃣ Create & Activate Virtual Environment

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run FastAPI App
```bash
uvicorn app:app --reload
```

Docs: http://127.0.0.1:8000/docs

---

# 📡 API Endpoints

### **GET /train**
Runs the full ML pipeline.

### **POST /predict**
Upload CSV → get phishing predictions.

---

# 📊 MLflow + DagsHub Tracking
Run locally:
```bash
mlflow ui
```

View online via DagsHub repo → *Experiments*.

---

# 📦 Artifacts Generated
- Cleaned dataset  
- Transformed dataset  
- Final model  
- Scalers / encoders  
- MLflow logs  

---

# ⭐ Future Enhancements
- AWS deployment  

---





