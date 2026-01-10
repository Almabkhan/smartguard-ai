import streamlit as st
# FROM:
from dashboard import show_dashboard

# TO:
import dashboard
from gemini_api import FraudDetector

st.set_page_config(page_title="SmartGuard AI", layout="wide")

# Title
st.title("🛡️ SmartGuard AI - Live Demo")
st.markdown("**Autonomous Fraud Detection for Agentic Commerce**")

# Tabs
tab1, tab2 = st.tabs(["📊 Dashboard", "🤖 AI Analysis"])

with tab1:
    show_dashboard()

with tab2:
    st.subheader("Gemini AI Fraud Detection")
    amount = st.number_input("Transaction Amount (USDC)", min_value=0.0, value=1500.0)
    sender = st.text_input("Sender ID", value="Agent_Alpha")
    receiver = st.text_input("Receiver ID", value="Wallet_XYZ")
    
    if st.button("🔍 Analyze Risk"):
        detector = FraudDetector(api_key="YOUR_API_KEY")  # Replace with actual key
        tx_data = {
            "amount": f"${amount}",
            "sender": sender,
            "receiver": receiver,
            "location": "Simulated Location",
            "pattern": "normal"
        }
        score, reason = detector.analyze_transaction(tx_data)
        
        st.metric("Risk Score", f"{score}/100")
        st.info(f"**Reason:** {reason}")
        
        if score > 80:
            st.error("🚨 High Risk - Recommend Block")
        elif score > 60:
            st.warning("⚠️ Medium Risk - Review Required")
        else:
            st.success("✅ Low Risk - Auto Approve")

st.caption("SmartGuard AI | Built for Agentic Commerce Hackathon 2026")
