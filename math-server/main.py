# Libs
from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("learn")


# The application runner
def main():
    mcp.run(transport="stdio")


# Run Main
if __name__ == "__main__":
    main()
