from fastapi import FastAPI
from routers import emotions

app = FastAPI()
app.include_router(emotions.router)