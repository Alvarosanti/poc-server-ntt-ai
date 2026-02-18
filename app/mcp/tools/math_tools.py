from app.mcp.mcp_app import mcp
from app.services.math_service import MathService


@mcp.tool()
def suma(a: float, b: float) -> float:
    return MathService.suma(a, b)


@mcp.tool()
def resta(a: float, b: float) -> float:
    return MathService.resta(a, b)


@mcp.tool(
    description=(
        "Abre una interfaz visual para que el usuario ingrese dos números "
        "cuando quiera realizar una suma."
    ),
    app={
        "resourceUri": "ui://my-app/view.html"
    }
)
def sumar_ui() -> str:
    return "Abriendo calculadora..."
