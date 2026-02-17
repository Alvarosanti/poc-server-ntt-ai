from fastapi import FastAPI
from app.http.routes import math_routes

app = FastAPI()

app.include_router(math_routes.router)
