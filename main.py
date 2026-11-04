from fastapi import FastAPI
from router import health

app = FastAPI()

app.include_router(health.router)
