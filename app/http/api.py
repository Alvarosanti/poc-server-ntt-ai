from fastapi import FastAPI
from app.http.routes import math_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(math_routes.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # luego restringes a Netlify
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)