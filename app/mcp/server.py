from fastmcp import MCP
from fastmcp.adapters import LambdaWebAdapter

mcp = MCP()

# En lugar de mount_static
mcp.add_static("/static", "./static")

lambda_adapter = LambdaWebAdapter(mcp)
