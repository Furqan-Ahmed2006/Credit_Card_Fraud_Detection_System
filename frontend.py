import streamlit as st
import requests
st.set_page_config(page_title="FRAUD-GUARD PRO", page_icon="🚫", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    div.stButton > button {
        background-color: #ff4b4b; color: white; border-radius: 10px;
        height: 3em; font-weight: bold; border: none; transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #ff1a1a; transform: scale(1.02); }
    .status-box { padding: 20px; border-radius: 15px; text-align: center; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)
st.title("🛡️ FRAUD-GUARD AI")
st.subheader("Real-Time Transaction Analysis Dashboard")
st.write("---")
col1, col2 = st.columns([1, 1.5], gap="large")

with col1:
    st.markdown("### 📝 Transaction Details")
    time_input = st.number_input("Time Offset (Seconds)", min_value=0, max_value=172800, value=400, step=1)
    st.caption("Seconds since 1st transaction (Max: 172,800)")
    
    amount_input = st.number_input("Transaction Amount ($)", min_value=0.0, value=150.0, step=10.0)
    st.caption("Enter the transaction value in USD")
    
    st.markdown("<br>", unsafe_allow_html=True) # Thori si space ke liye
    analyze_btn = st.button("RUN AI DIAGNOSTICS")

with col2:
    st.markdown("### 📊 Live Risk Assessment")
    
    if analyze_btn:
        try:
            url = "https://furqan2006-credit-card-fraud-detection.hf.space/predict"
            payload = {"time": float(time_input), "amount": float(amount_input)}
            response = requests.post(url, json=payload)
            
            result = response.json()
            
            prob_str = result['fraud_probability'].replace('%', '')
            probability = float(prob_str)
            status = result['result']
            if status == "Fraud":
                st.error(f"### 🚨 Prediction: {status}")
                st.metric(label="Risk Score", value=result['fraud_probability'], delta="CRITICAL")
                st.warning("Immediate action recommended: Flagged by AI behavior analysis.")
            else:
                st.success(f"### ✅ Prediction: {status}")
                st.metric(label="Risk Score", value=result['fraud_probability'], delta="SAFE", delta_color="normal")
                st.info("Transaction patterns appear normal.")

            st.progress(probability / 100)

        except Exception as e:
            st.error(f"❌ API Offline: Make sure your FastAPI is running!")
    else:
        st.info("Waiting for input... Fill the details and click 'Run AI Diagnostics'.")
