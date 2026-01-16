import google.generativeai as genai

class FraudDetector:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
def analyze_transaction(self, transaction_data):
    """Analyze transaction for fraud risk (MOCK VERSION for demo)"""
    # Mock scores for different sender types
    mock_scores = {
        "Agent_Alpha": 85,
        "HighRisk_Agent": 92,
        "Trusted_Vendor": 45,
        "New_User": 78,
        "Wallet_XYZ": 65,
        "Crypto_Bot": 88
    }
    
    # Get sender or use default
    sender = transaction_data.get('sender', 'Unknown')
    score = mock_scores.get(sender, 65)  # Default 65 if sender not in list
    
    # Mock reasons based on score
    if score >= 80:
        reasons = [
            "High risk: Unusual transaction amount detected.",
            "High risk: Sender location mismatch with history.",
            "High risk: New device fingerprint detected."
        ]
    elif score >= 60:
        reasons = [
            "Medium risk: Slightly above average amount.",
            "Medium risk: Unusual time for this agent.",
            "Medium risk: Multiple rapid transactions."
        ]
    else:
        reasons = [
            "Low risk: Normal transaction pattern.",
            "Low risk: Trusted agent with clean history.",
            "Low risk: Amount within safe limits."
        ]
    
    import random
    reason = random.choice(reasons)
    
    return score, reason
