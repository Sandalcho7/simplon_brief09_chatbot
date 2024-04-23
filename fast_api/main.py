import os
import json
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config import HEADERS, TOOL_URL, PROVIDER, SCRAPED_URL, payload
from scraper import scrape_data


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

    response = requests.post(TOOL_URL, json=payload, headers=HEADERS)
    result = json.loads(response.text)
    rp = result[PROVIDER]
    formatted_response = rp["generated_text"].strip('"')

    return formatted_response


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
