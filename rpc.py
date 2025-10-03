from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    x: int
    y: int

@app.post("/add")
async def add(data: Numbers):
    return {"result": data.x + data.y}

@app.post("/multiply")
async def multiply(data: Numbers):
    return {"result": data.x * data.y}

