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


@mcp.tool(
    name="multiply",
    title="Multiply",
    description="Multiply 2 numbers",
)
def multiply(a: int, b: int):
    """Multiply 2 numbers"""

    return a * b


@mcp.tool(
    name="divide",
    title="Divide",
    description="Divide 2 numbers",
)
def divide(a: int, b: int):
    """Divide 2 numbers"""

    return a / b


@mcp.tool(
    name="power",
    title="Power",
    description="Get the value of x raised to power y",
)
def power(x: int, y: int):
    """Get the value of x raised to power y"""

    return math.pow(x, y)


@mcp.tool(
    name="square_root",
    title="Square root",
    description="Get square root of a number",
)
def square_root(x: int):
    """Get square root of a number"""

    return math.sqrt(x)


@mcp.tool(
    name="acos",
    title="arc cosine",
    description="The acos tool returns the arc cosine value of a number",
)
def acos(x: int):
    """The acos method tool the arc cosine value of a number"""

    return math.acos(x)


@mcp.tool(
    name="acosh",
    title="inverse hyperbolic cosine",
    description="The acosh tool returns the inverse hyperbolic cosine of a number",
)
def acosh(x: int):
    """The acosh tool returns the inverse hyperbolic cosine of a number"""

    return math.acosh(x)


@mcp.tool(
    name="asin",
    title="inverse hyperbolic cosine",
    description="The math.asin() method returns the arc sine of a number",
)
def asin(x: int):
    """The acosh tool returns the inverse hyperbolic cosine of a number"""

    return math.asin(x)


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
