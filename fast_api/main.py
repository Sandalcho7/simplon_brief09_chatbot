import os
import json
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scraper import scrape_data

KEY = os.getenv("EDEN_AI_KEY")
HEADERS = {"Authorization": KEY}

URL = "https://api.edenai.run/v2/text/chat"
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


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/test/{prompt}", description="Test !")
def test(prompt):
    return "Yo"


@app.post("/{prompt}")
async def chatbot(prompt):
    try:
        data = scrape_data(SCRAPED_URL)
    except:
        data = ""

    payload["text"] = prompt
    payload["chatbot_global_action"] = (
        f"Act as an assistant, answer questions using the following data if needed: {data}. Your answer need to be shorter than 100 words."
    )

    print("-----------------------KEY = ", KEY)

    response = requests.post(URL, json=payload, headers=HEADERS)
    result = json.loads(response.text)
    rp = result[PROVIDER]
    formatted_response = rp["generated_text"].strip('"')
    return formatted_response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
