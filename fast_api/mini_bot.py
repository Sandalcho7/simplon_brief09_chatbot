import json
import requests

from keys.key import key

HEADERS = {"Authorization": f"Bearer {key}"}
URL = "https://api.edenai.run/v2/text/chat"
PROVIDER = 'mistral'

payload = {
        "providers": PROVIDER,
        "text": "",
        "chatbot_global_action": "Act as Queen Elisabeth and answer in less than 100 words",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 150,
        "fallback_providers": ""
    }

def chatbot():
    while True:
        prompt = input('Q: ')
        payload["text"] = prompt
    
        if prompt in ['quit', 'logout', 'leave', 'exit', 'bye', 'stop']:
            break
        
        response = requests.post(URL, json=payload, headers=HEADERS)
        result = json.loads(response.text)
        rp = result[PROVIDER]
    
        formatted_response = "\nR: " + rp["generated_text"] + "\n"
    
        payload["previous_history"].append({"role": "user", "message": prompt})
        payload["previous_history"].append({"role": "assistant", "message": rp["generated_text"]})
        
        print(formatted_response)