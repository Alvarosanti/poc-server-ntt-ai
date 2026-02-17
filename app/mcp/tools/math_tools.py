from app.mcp.mcp_app import mcp
from app.services.math_service import MathService

@mcp.tool()
def suma(a: float, b: float) -> float:
    return MathService.suma(a, b)

@mcp.tool()
def resta(a: float, b: float) -> float:
    return MathService.resta(a, b)

@mcp.tool(
    meta={
        "openai/outputTemplate": "ui://widget/input-text.html",
        "openai/toolInvocation/invoking": "Abriendo calculadora...",
        "openai/toolInvocation/invoked": "Calculadora lista"
    }
)

def sumar_ui() -> str:
    """
    Tool que abre el widget InputText para sumar números.
    """
    return "Formulario para sumar números"
