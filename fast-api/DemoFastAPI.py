# pip install fastapi uvicorn
# pip install fastapi

from fastapi import FastAPI

app = FastAPI()
@app.get("/hello")
async def hello():
    return "Hello World!"