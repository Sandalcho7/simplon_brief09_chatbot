import os


# EDEN AI settings
KEY = os.getenv("EDEN_AI_KEY")  # ex: "eyJhbG..."
HEADERS = {"Authorization": f"Bearer {KEY}"}

TOOL_URL = "https://api.edenai.run/v2/text/chat"
PROVIDER = "mistral"
SCRAPED_URL = "http://abb09.westeurope.azurecontainer.io:8001/"


payload = {
    "providers": PROVIDER,
    "text": "",
    "chatbot_global_action": "",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "",
}
