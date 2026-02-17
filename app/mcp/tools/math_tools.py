from app.mcp.server import mcp
from app.services.math_service import MathService

@mcp.tool()
def suma(a: float, b: float) -> float:
    return MathService.suma(a, b)

@mcp.tool()
def resta(a: float, b: float) -> float:
    return MathService.resta(a, b)
