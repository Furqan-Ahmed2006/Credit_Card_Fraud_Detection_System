from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import joblib
import pandas as pd
df=pd.read_csv("Credit_card_fraud_clean_Data.csv")
app=FastAPI(title="Simple Fraud Detection API",description="Fraud Detection by Just Entering Amount and Time")
try:
    model_rf=joblib.load("model_rf.pkl")
    model_xgb=joblib.load("model_xgb.pkl")
    scaler=joblib.load("scaler.pkl")
except Exception as e:
    print(f"Error!: Model File Missing {e}")

class TransactionInput(BaseModel):
    time :float=Field(...,ge=0,example=407.9,description="Transaction Time in seconds")
    amount:float=Field(...,ge=0,example=96.99,description="Transaction Amount in decimal")
@app.get("/")
async def home():
    return {"message":"Welcome to Fraud Detection API! Go to /docs for testing."}
@app.post("/predict")
async def predict_fraud(data: TransactionInput):
    try:
        sample = df.sample(1).drop("Class", axis=1).copy()
        sample["Time"] = data.time
        sample["Amount"] = data.amount

        scaled_data = scaler.transform(sample)
        rf_prob = model_rf.predict_proba(scaled_data)[0][1]
        xgb_prob = model_xgb.predict_proba(scaled_data)[0][1]

        final_score = (0.6 * rf_prob) + (0.4 * xgb_prob)
        prediction = "Fraud" if final_score > 0.3 else "Normal"

        return {
            "result": prediction,
            "fraud_probability": f"{round(final_score*100,2)}%",
            "mode": "Fraud Pattern Path" if final_score > 0.3 else "Normal Pattern Path"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))