import requests
import json

from .scraper import scrape_data
from .config import HEADERS, PROVIDER, TOOL_URL, SCRAPED_URL, payload



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