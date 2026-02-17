from fastmcp import FastMCP
from fastapi.staticfiles import StaticFiles
from pathlib import Path

# Inicializa tu MCP server
mcp = FastMCP("poc-server-ai")

# Ruta de widgets (input-text.html y assets)
widgets_path = Path(__file__).parent / "widgets"

# Monta la carpeta widgets como archivos estáticos en /widget
mcp.app.mount("/widget", StaticFiles(directory=widgets_path), name="widget")
