from fastmcp import FastMCP
from app.mcp.mcp_app import mcp
from app.mcp.tools import math_tools  # noqa: F401

# Inicializa la aplicación MCP correctamente
mcp = FastMCP(
    modules=[math_tools],  # importa tus herramientas
    # Ya no necesitas mount_static
)