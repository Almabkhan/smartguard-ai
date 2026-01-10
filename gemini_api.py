import google.generativeai as genai

class FraudDetector:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
    
    def analyze_transaction(self, transaction_data):
        """Analyze transaction for fraud risk using Gemini AI"""
        prompt = f"""
        Analyze this transaction for fraud risk:
        Amount: {transaction_data.get('amount')}
        Sender: {transaction_data.get('sender')}
        Receiver: {transaction_data.get('receiver')}
        Location: {transaction_data.get('location')}
        Previous pattern: {transaction_data.get('pattern', 'normal')}
        
        Return only: RISK_SCORE|REASON
        Example: 85|Unusual location pattern
        """
        
        try:
            response = self.model.generate_content(prompt)
            result = response.text.strip()
            if "|" in result:
                score, reason = result.split("|", 1)
                return int(score), reason
            return 50, "Analysis inconclusive"
        except Exception as e:
            return 50, f"AI error: {str(e)}"

# Example usage
if __name__ == "__main__":
    detector = FraudDetector(api_key="YOUR_API_KEY_HERE")
    sample_tx = {
        "amount": "$1,500",
        "sender": "Agent_Alpha",
        "receiver": "Wallet_XYZ",
        "location": "New York, USA",
        "pattern": "normal"
    }
    score, reason = detector.analyze_transaction(sample_tx)
    print(f"Risk Score: {score}/100")
    print(f"Reason: {reason}")
