from fastmcp import FastMCP
from pathlib import Path

mcp = FastMCP("poc-server-ai")

BASE_DIR = Path(__file__).parent / "apps"
VIEW_URI = "ui://calculator/input-text.html"

@mcp.resource(VIEW_URI)
def calculator_view() -> str:
    html_path = BASE_DIR / "input-text.html"
    return html_path.read_text()