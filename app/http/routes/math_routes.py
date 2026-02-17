from fastapi import APIRouter
from app.services.math_service import MathService
from app.services.helloWorld_service import HelloService

router = APIRouter(prefix="/math", tags=["math"])

@router.get("/suma")
def suma(a: float, b: float):
    return {"result": MathService.suma(a, b)}

@router.get("/resta")
def resta(a: float, b: float):
    return {"result": MathService.resta(a, b)}

@router.get("/hello-world")
def hello_world():
    return {"message": HelloService.say_hello()}