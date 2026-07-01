from fastapi import FastAPI
from pydantic import BaseModel

from app.recommender import recommend

app = FastAPI()


class ChatRequest(BaseModel):
    messages: list


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    if len(request.messages) == 0:
        return {
            "reply": "Hello! I can help you choose SHL assessments.",
            "recommendations": [],
            "end_of_conversation": False
        }

    last_message = request.messages[-1]["content"]
    
    return recommend(last_message)