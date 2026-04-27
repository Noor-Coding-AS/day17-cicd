from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="CI/CD Demo", version="1.0.0")

@app.get("/")
async def root():
    return {
        "message": "Hello from CI/CD pipeline!",
        "built_by": "Asfer Saeed",
        "day": "17 of 90",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

def add_numbers(a: int, b: int) -> int:
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    return a * b