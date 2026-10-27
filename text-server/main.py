# Libs
from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer(
    title="Text MCP",
    name="Text MCP Server",
    description="Learning how to create a MCP Server using Python SDK",
)


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8003)


# Run Main
if __name__ == "__main__":
    main()
