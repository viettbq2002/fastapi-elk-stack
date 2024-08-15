from typing import Union

from fastapi import FastAPI

from app.logging_setup import LoggerSetup
from app.logging_middlware import LoggingMiddleware

logger_setup = LoggerSetup()
app = FastAPI(
    title="FastAPI ELK Stack",
    description="Learning ELK Stack Logging Centralize with fastapi",
    version="1.0.0",
)

app.add_middleware(LoggingMiddleware)


@app.get("/")
def read_root():
    return {"Status": "Your API Work"}


@app.post("/hello")
def post_test(data: dict):
    return data


@app.get("test")
def test():
    return {"This is": "Test Repsonse hoho"}
