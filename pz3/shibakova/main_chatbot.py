import uvicorn
from fastapi import FastAPI
from transformers import pipeline, Conversation

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.state.chatbot = pipeline(model="facebook/blenderbot-400M-distill")
    app.state.history = []

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/chatbot/")
async def chatbot_api(user_input: str):
    if user_input.lower() == "bye":
        return {'response': 'Goodbye!'}
    else:
        conversation = Conversation()
        conversation.add_user_input(user_input)
        conversation = app.state.chatbot(conversation)
        chatbot_response = conversation.generated_responses[-1]
        app.state.history.append({"user_input": user_input, "chatbot_response": chatbot_response})
        return {"response": chatbot_response}
