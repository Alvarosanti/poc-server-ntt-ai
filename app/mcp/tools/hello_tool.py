from app.mcp.server import mcp

@mcp.tool()
def hello(name: str) -> str:
    """Simple hello tool"""
    return f"Hello {name}!"