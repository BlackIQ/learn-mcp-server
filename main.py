# Libs
from typing import Any  # Types
import logging  # Logging

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("learn")

# Setup Logger
logger = logging.getLogger(__name__)


# Tool
@mcp.tool()
async def say_hi(name: str) -> dict[str, Any] | None:
    """Say hi to someone"""

    return {"message": f"Hello {name}!"}


# The application runner
def main():
    mcp.run(transport="stdio")


# Run Main
if __name__ == "__main__":
    main()
