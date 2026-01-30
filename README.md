# Phishing URL Detection System (MLOps + FastAPI + MLflow/DagsHub)

An end-to-end machine learning system to classify URLs as **phishing or legitimate** using engineered URL-based features.  
Includes modular ML pipelines (ingestion → transformation → training → prediction), experiment tracking with **MLflow + DagsHub**, and deployment via **FastAPI**.

---

## Key Features
- Modular pipeline architecture: **Data Ingestion, Data Transformation, Model Training**
- Trains & compares multiple models (RandomForest, GradientBoosting, Logistic Regression, AdaBoost)
- Tracks experiments & metrics (**F1 / Precision / Recall**) using **MLflow + DagsHub**
- Exposes REST APIs using **FastAPI**
  - `GET /train` → trains model
  - `POST /predict` → predicts on uploaded CSV dataset

---

## Tech Stack
**Python**, Pandas, NumPy, Scikit-learn, FastAPI, Uvicorn, MLflow, DagsHub, PyYAML, MongoDB

---

## Dataset
The project uses a phishing dataset where each row contains URL-derived features and a target label:
- Target column: `Result`
  - Typically: `1 = phishing`, `-1 = legitimate` (depends on dataset version)

---

## Project Structure 
- `networksecurity/` → core ML pipeline code (ingestion, transformation, training)
- `app.py` → FastAPI entrypoint exposing `/train` and `/predict`
- `artifacts/` → generated artifacts (processed data, models, etc.)
- `final_model/` → final model pickle

---
## 🚀 Installation & Setup

Follow the steps below to set up and run the **Phishing URL Detection System** locally.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ishantyagii/Phising-URL-Detection-System.git
cd Phising-URL-Detection-System
---

### 2️⃣ Create & Activate Virtual Environment

#### **Windows**
```bash
python -m venv venv
venv\Scripts\activate



