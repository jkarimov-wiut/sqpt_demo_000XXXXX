from fastapi import FastAPI, Query
from app.calculator import add, subtract, multiply, divide

app = FastAPI(title="Calculator API")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/calc/{operation}")
def calc(operation: str, a: float = Query(...), b: float = Query(...)):
    ops = {"add": add, "subtract": subtract,
           "multiply": multiply, "divide": divide}
    if operation not in ops:
        return {"error": "unknown operation"}
    return {"result": ops[operation](a, b)}
