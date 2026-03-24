from fastapi import FastAPI
from app.api.routes import router

app = FastAPI()


@app.get('/')
def home():
    return {"mag":"run!!!"}

app.include_router(router)