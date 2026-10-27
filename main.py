# Libs
import math  # Math

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("Math MCP")


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
    title="arc sine",
    description="The asin tool returns the arc sine of a number",
)
def asin(x: int):
    """The asin tool returns the arc sine of a number"""

    return math.asin(x)


@mcp.tool(
    name="asinh",
    title="inverse hyperbolic sine",
    description="The asinh tool returns the inverse hyperbolic sine of a number",
)
def asinh(x: int):
    """The asinh tool returns the inverse hyperbolic sine of a number"""

    return math.asinh(x)


@mcp.tool(
    name="atan",
    title="arc tangent",
    description="The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians",
)
def atan(x: int):
    """The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians"""

    return math.atan(x)


@mcp.tool(
    name="atan2",
    title="arc tangent of y/x",
    description="The atan2 method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)",
)
def atan2(x: int, y: int):
    """The atan2 method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)"""

    return math.atan2(x, y)


@mcp.tool(
    name="atan2",
    title="inverse hyperbolic tangent",
    description="The atanh tool returns the inverse hyperbolic tangent of a number",
)
def atan2(x: int):
    """The atanh tool returns the inverse hyperbolic tangent of a number"""

    return math.atanh(x)


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
