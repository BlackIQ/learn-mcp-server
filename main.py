# Libs
import math  # Math

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("Math MCP")


@mcp.tool(
    name="acos",
    title="arc cosine",
    description="The acos tool returns the arc cosine value of a number",
)
def acos(x: int):
    """
    The acos method tool the arc cosine value of a number

    Note: The parameter passed in acos must lie between -1 to 1.
    Tip: acos will return the value of PI.

    Args:
        - x: Required. A number in the range -1 to 1
    """

    return math.acos(x)


@mcp.tool(
    name="acosh",
    title="inverse hyperbolic cosine",
    description="The acosh tool returns the inverse hyperbolic cosine of a number",
)
def acosh(x: int):
    """
    The acosh tool returns the inverse hyperbolic cosine of a number

    Note: The parameter passed in acosh must be greater than or equal to 1.

    Args:
        - x: Required. A positive number >= 1
    """

    return math.acosh(x)


@mcp.tool(
    name="asin",
    title="arc sine",
    description="The asin tool returns the arc sine of a number",
)
def asin(x: int):
    """
    The asin tool returns the arc sine of a number

    Note: The parameter passed in asin must lie between -1 to 1.
    Tip: asin will return the value of PI/2, and asin of -1 will return the value of -PI/2.

    Args:
        - x: Required. A number in the range -1 to 1
    """

    return math.asin(x)


@mcp.tool(
    name="asinh",
    title="inverse hyperbolic sine",
    description="The asinh tool returns the inverse hyperbolic sine of a number",
)
def asinh(x: int):
    """
    The asinh tool returns the inverse hyperbolic sine of a number

    Args:
        - x: Required. A positive or negative number
    """

    return math.asinh(x)


@mcp.tool(
    name="atan",
    title="arc tangent",
    description="The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians",
)
def atan(x: int):
    """
    The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians

    Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated.

    Args:
        - x: Required. A positive or negative number
    """

    return math.atan(x)


@mcp.tool(
    name="atan2",
    title="arc tangent of y/x",
    description="The atan2 method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)",
)
def atan2(x: int, y: int):
    """
    The atan2 method returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)

    The returned value is between PI and -PI.

    Args:
        - x: Required. Specifies a positive or negative number
        - y: Required. Specifies a positive or negative number
    """

    return math.atan2(x, y)


@mcp.tool(
    name="atanh",
    title="inverse hyperbolic tangent",
    description="The atanh tool returns the inverse hyperbolic tangent of a number",
)
def atanh(x: int):
    """
    The atanh tool returns the inverse hyperbolic tangent of a number

    Note: The parameter passed in math.atanh() must lie between -0.99 to 0.99.

    Args:
        - x: Required. A positive or negative number between -0.99 and 0.99
    """

    return math.atanh(x)


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
