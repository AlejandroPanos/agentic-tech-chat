import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import health

app = FastAPI()

# Configure CORS (Cross-Origin Resource Sharing) settings for the frontend origins
allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "FRONTEND_ORIGINS",
        "http://localhost:3000,http://localhost:5173",
    ).split(",")
    if origin.strip()
]

# Add CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers for different endpoints
app.include_router(health.router)
