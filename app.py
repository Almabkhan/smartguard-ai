import streamlit as st
import dashboard
from gemini_api import FraudDetector

st.set_page_config(page_title="SmartGuard AI", layout="wide")

# Title
st.title("🛡️ SmartGuard AI - Live Demo")
st.markdown("**Autonomous Fraud Detection for Agentic Commerce**")

# Tabs
tab1, tab2 = st.tabs(["📊 Dashboard", "🤖 AI Analysis"])

with tab1:
    dashboard.show_dashboard()

with tab2:
    st.subheader("Gemini AI Fraud Detection")
    amount = st.number_input("Transaction Amount (USDC)", min_value=0.0, value=1500.0)
    sender = st.text_input("Sender ID", value="Agent_Alpha")
    receiver = st.text_input("Receiver ID", value="Wallet_XYZ")
    
    if st.button("🔍 Analyze Risk"):
        # Mock analysis for demo (no API key needed)
        mock_scores = {
            "Agent_Alpha": 85,
            "HighRisk_Agent": 92, 
            "Wallet_XYZ": 65,
            "Trusted_Vendor": 45,
            "New_User": 78
        }
        
        score = mock_scores.get(sender, 75)  # Default 75 if sender not in list
        
        # Mock reasons
        if score >= 80:
            reason = "🚨 High Risk: Unusual transaction pattern detected."
            st.error("🚨 High Risk - Recommend Block")
        elif score >= 60:
            reason = "⚠️ Medium Risk: Slightly above average amount."
            st.warning("⚠️ Medium Risk - Review Required")
        else:
            reason = "✅ Low Risk: Normal transaction pattern."
            st.success("✅ Low Risk - Auto Approve")
        
        st.metric("Risk Score", f"{score}/100")
        st.info(f"**Reason:** {reason}")

st.caption("SmartGuard AI | Built for Agentic Commerce Hackathon 2026")
