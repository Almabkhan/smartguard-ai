def show_dashboard():

import streamlit as st
import pandas as pd

st.set_page_config(page_title="SmartGuard AI", layout="wide")
st.title("🛡️ SmartGuard AI Dashboard")
st.markdown("### Real-time Fraud Detection for Agentic Commerce")

# Sample transaction data
transactions = pd.DataFrame({
    "Transaction ID": ["TX001", "TX002", "TX003", "TX004"],
    "Risk Score": [85, 92, 45, 78],
    "Status": ["✅ Approved", "❌ Blocked", "✅ Approved", "⚠️ Review"],
    "Amount (USDC)": ["$1,500", "$3,200", "$800", "$2,100"],
    "Time": ["10:30 AM", "10:32 AM", "10:35 AM", "10:40 AM"]
})

# Display table
st.dataframe(transactions, use_container_width=True, hide_index=True)

# Dashboard metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Transactions", "1,247", "+12%")
with col2:
    st.metric("Fraud Blocked", "38", "-5%")
with col3:
    st.metric("Avg Risk Score", "67/100", "+3")

# Risk distribution chart
st.subheader("Risk Score Distribution")
chart_data = pd.DataFrame({"Risk": [20, 35, 25, 15, 5]}, index=["0-20", "21-40", "41-60", "61-80", "81-100"])
st.bar_chart(chart_data)

st.caption("SmartGuard AI - Autonomous fraud detection system | Last updated: Real-time")
