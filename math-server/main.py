# Libs
import math  # Math

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("Math MCP")


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
