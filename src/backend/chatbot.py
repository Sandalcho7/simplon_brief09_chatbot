import requests
import json
import os

from scraper import scrape_data
from dotenv import load_dotenv

load_dotenv()


# Chatbot configuration
KEY = os.getenv("EDENAI_KEY")
HEADERS = {"Authorization": f"Bearer {KEY}"}

TOOL_URL = "https://api.edenai.run/v2/text/chat"
PROVIDER = "openai/gpt-4o-mini"

SCRAPED_URL = "http://frontend:8001/"

payload = {
    "providers": PROVIDER,
    "text": "",
    "chatbot_global_action": "",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "",
}


# Chatbot function
def get_answer_from_chatbot(prompt):
    try:
        data = scrape_data(SCRAPED_URL)
    except:
        data = ""

    payload["text"] = prompt
    payload["chatbot_global_action"] = (
        f"Act as an assistant, answer questions using the following data if needed: {data}. Your answer need to be shorter than 100 words."
    )

    response = requests.post(TOOL_URL, json=payload, headers=HEADERS)
    result = json.loads(response.text)
    rp = result[PROVIDER]
    formatted_response = rp["generated_text"].strip('"')

    return formatted_response
