from fastmcp import FastMCP
from pathlib import Path

# Inicializa tu MCP server
mcp = FastMCP("poc-server-ai")

# Ruta de widgets (input-text.html y assets)
widgets_path = Path(__file__).parent / "widgets"

# Monta la carpeta widgets como archivos estáticos
mcp.mount_static("/widget", widgets_path)
