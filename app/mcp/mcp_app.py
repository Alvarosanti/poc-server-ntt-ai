from fastmcp import FastMCP
from pathlib import Path

# Inicializa tu MCP server
mcp = FastMCP("poc-server-ai")

widgets_path = Path(__file__).parent / "widgets"

mcp.mount_static("/widget", widgets_path)