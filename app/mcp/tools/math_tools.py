from app.mcp.mcp_app import mcp
from app.services.math_service import MathService
from fastmcp.server.apps import AppConfig

@mcp.tool()
def suma(a: float, b: float) -> float:
    return MathService.suma(a, b)


@mcp.tool()
def resta(a: float, b: float) -> float:
    return MathService.resta(a, b)

VIEW_URI = "ui://calculator/input-text.html"

@mcp.tool(
    description="Abre una calculadora visual para sumar números.",
    app=AppConfig(resource_uri=VIEW_URI)
)
def sumar_ui() -> str:
    return "Calculadora lista."

