from fastmcp import FastMCP

mcp = FastMCP("poc-server-ai")

from app.mcp.tools import math_tools

if __name__ == "__main__":
    mcp.run()