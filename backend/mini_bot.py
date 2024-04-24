import json
import requests

from config import HEADERS, TOOL_URL, PROVIDER, payload


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