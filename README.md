
# Credit Card Fraud Detection System

## 📝 Project Overview
This project is an **end-to-end machine learning system** designed to detect credit card fraud using historical transaction data.  

It includes:  
- **Machine learning models** (RandomForest, XGBoost)  
- Handling **imbalanced data** with SMOTE  
- **API deployment using FastAPI**  
- **Frontend demo using Streamlit**  

The system predicts whether a transaction is **Fraudulent** or **Normal** and provides a **fraud probability score**.

---

## 🎯 Objective
- Detect fraudulent transactions in a dataset of credit card transactions.  
- Focus on **high recall** to capture fraud cases effectively.  
- Demonstrate **full ML workflow**: preprocessing, modeling, evaluation, and deployment.

---

## 📂 Dataset
- Dataset: [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
- Rows: 284,807  
- Features: 30 numerical features (`V1` to `V28`, `Time`, `Amount`)  
- Target: `Class` (0 = Normal, 1 = Fraud)  
- Note: `V1`–`V28` are **PCA-transformed** to anonymize original features.

---

## ⚙️ Data Preprocessing
1. **Train-test split** (80-20)  
2. **StandardScaler** applied on all features  
3. **SMOTE** used to balance the minority class  
4. Train models on resampled data to improve **recall** of fraudulent transactions  

---

## ⚠️ PCA Challenge & Solution
**Problem:**  
- Original features were transformed using **PCA**, so real-time calculation of `V1`–`V28` for new transactions is **not possible**.  
- This made **real-time predictions** for unseen transactions tricky.  

**Solution:**  
- For API and Streamlit demo, we **sample patterns from the dataset** that match fraud and normal transactions.  
- Combine user input (`Time` and `Amount`) with sampled PCA patterns to make predictions.  
- This approach allows **testing and demonstration** while keeping ML logic valid.  

> Note: This is **practical for portfolio/demo purposes**, although not live PCA transformation.

---

## 🧰 Models Used
1. **RandomForestClassifier**  
   - n_estimators: 200  
   - max_depth: 12  
   - Random state: 42  

2. **XGBoostClassifier**  
   - max_depth: 4  
   - learning_rate: 0.1  
   - n_estimators: 300  
   - Subsample: 0.8  

**Ensemble**: Weighted average of predictions  
- 60% RandomForest + 40% XGBoost  

---

## 📊 Model Evaluation
- **Metrics Used**:  
  - Confusion Matrix  
  - Recall (focus on detecting fraud)  
  - Precision  
  - ROC-AUC  
  - Cross-validation (StratifiedKFold)  

- Focus on **recall** since catching fraud is more important than overall accuracy.

---
For testing visit:
  
🔗https://creditcardfrauddetectionsystem-acr4bbgqpvvf5nefnpqbta.streamlit.app/


## ⚡ API & Frontend Deployment
- **FastAPI** endpoint `/predict` accepts:
```json
{
"time": 407.9,
  "amount": 96.99
}
## Returns fraud prediction and probability:
{
  "result": "Fraud",
  "fraud_probability": "85.12%",
  "mode": "Fraud Pattern Path"
}

🔧 Requirements
Python >= 3.9
pandas, numpy
scikit-learn, xgboost
imbalanced-learn
matplotlib, seaborn
fastapi, uvicorn
streamlit
joblib

Install via:
pip install -r requirements.txt

📌 Limitations
Real-time PCA calculation not possible; API/demo samples patterns from dataset.
Threshold for fraud probability can be adjusted depending on the business context.
Model performance depends on historical fraud patterns.

🚀 How to Run
Clone the repo
Install requirements
Run API:
uvicorn app:app --reload
Open Swagger docs: http://127.0.0.1:8000/docs
Run Streamlit frontend:streamlit run frontend.py
🔍 Key Learnings
Handling highly imbalanced datasets using SMOTE
Building ensemble models for robust prediction
Evaluating models using recall-focused metrics
Deploying ML API with FastAPI
Creating interactive frontend with Streamlit

