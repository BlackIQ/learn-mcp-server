# Libs
import math  # Math

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("Math MCP")


@mcp.tool(
    name="add",
    title="Add",
    description="Add 2 numbers",
)
def add(a: int, b: int):
    """Add 2 numbers"""

    return a + b


@mcp.tool(
    name="subtract",
    title="Subtract",
    description="Subtract 2 numbers",
)
def subtract(a: int, b: int):
    """Subtract 2 numbers"""

    return a - b


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
