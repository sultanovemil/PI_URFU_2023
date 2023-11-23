from pydantic import BaseModel, Field

class Emotion(BaseModel):
    label: str = Field(example="joy")
    score: float = Field(example=0.8993354439735413)

class EmotionsInput(BaseModel):
    text: str = Field(example="I am so happy about developing FastAPI apps!")

class EmotionsOutput(EmotionsInput):
    emotions: list[Emotion]