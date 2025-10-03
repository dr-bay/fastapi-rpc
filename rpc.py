from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define input data model
class Numbers(BaseModel):
    x: int
    y: int

@app.post("/add")
def add(numbers: Numbers):
    return {"result": numbers.x + numbers.y}

@app.post("/multiply")
def multiply(numbers: Numbers):
    return {"result": numbers.x * numbers.y}
