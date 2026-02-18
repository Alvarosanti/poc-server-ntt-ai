from fastmcp import FastMCP
from fastmcp.apps import App

mcp = FastMCP("poc-server-ai")

my_app = App(
    name="my-app",
    resources_dir="app/mcp/apps/my-app"
)

mcp.register_app(my_app)