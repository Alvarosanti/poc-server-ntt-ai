from fastmcp import FastMCP

mcp = FastMCP("poc-server-ntt-ai")

# importa tools para que se registren
from app.mcp.tools import math_tools  # noqa: F401