import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()


# Chatbot configuration
KEY = os.getenv("EDENAI_KEY")
HEADERS = {"Authorization": f"Bearer {KEY}"}

TOOL_URL = "https://api.edenai.run/v2/text/chat"
PROVIDER = "openai/gpt-4o-mini"

payload = {
    "providers": PROVIDER,
    "text": "",
    "chatbot_global_action": "",
    "previous_history": [],
    "temperature": 0.0,
    "max_tokens": 150,
    "fallback_providers": "",
}


def chatbot():
    while True:
        prompt = input("Q: ")
        payload["text"] = prompt

        if prompt in ["quit", "logout", "leave", "exit", "bye", "stop"]:
            break

        response = requests.post(TOOL_URL, json=payload, headers=HEADERS)
        result = json.loads(response.text)
        rp = result[PROVIDER]

        formatted_response = "\nR: " + rp["generated_text"] + "\n"

        payload["previous_history"].append({"role": "user", "message": prompt})
        payload["previous_history"].append(
            {"role": "assistant", "message": rp["generated_text"]}
        )

        print(formatted_response)
