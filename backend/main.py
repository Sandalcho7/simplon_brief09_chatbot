from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from chatbot import get_answer_from_chatbot



app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You can restrict this to specific HTTP methods if needed
    allow_headers=["*"],  # You can restrict this to specific headers if needed
)


@app.get("/test", description="Test !")
def test():
    return "Yo"


@app.post("/{prompt}")
async def chatbot(prompt):
    return get_answer_from_chatbot(prompt)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)