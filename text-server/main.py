# Libs
from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("learn")


# The application runner
def main():
    mcp.run(transport="streamable-http")


# Run Main
if __name__ == "__main__":
    main()
