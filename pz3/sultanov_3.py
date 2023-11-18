from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-mul-en")

class Item(BaseModel):
    text: str
    
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/translate/")
def translate(item: Item):
    """Перевод текста с мультиязычного (mul) на английский язык (en)"""
    return pipe(item.text)[0]



