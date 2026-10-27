# Libs
import math  # Math

from mcp.server import MCPServer  # MCP Server

# Create MCP Server
mcp = MCPServer("Math MCP")


@mcp.tool("arc cosine value of x")
def acos(x: int):
    """
    The acos tool returns the arc cosine value of a number

    Note: The parameter passed in acos must lie between -1 to 1.
    Tip: acos will return the value of PI.

    Args:
        - x: Required. A number in the range -1 to 1
    """

    return math.acos(x)


@mcp.tool("inverse hyperbolic cosine of x")
def acosh(x: int):
    """
    The acosh tool returns the inverse hyperbolic cosine of a number

    Note: The parameter passed in acosh must be greater than or equal to 1.

    Args:
        - x: Required. A positive number >= 1
    """

    return math.acosh(x)


@mcp.tool("arc sine of a x")
def asin(x: int):
    """
    The asin tool returns the arc sine of a number

    Note: The parameter passed in asin must lie between -1 to 1.
    Tip: asin will return the value of PI/2, and asin of -1 will return the value of -PI/2.

    Args:
        - x: Required. A number in the range -1 to 1
    """

    return math.asin(x)


@mcp.tool("inverse hyperbolic sine of x")
def asinh(x: int):
    """
    The asinh tool returns the inverse hyperbolic sine of a number

    Args:
        - x: Required. A positive or negative number
    """

    return math.asinh(x)


@mcp.tool("arc tangent of x")
def atan(x: int):
    """
    The atan tool returns the arc tangent of a number (x) as a numeric value between -PI/2 and PI/2 radians

    Arc tangent is also defined as an inverse tangent function of x, where x is the value of the arc tangent is to be calculated.

    Args:
        - x: Required. A positive or negative number
    """

    return math.atan(x)


@mcp.tool("arc tangent of x and y")
def atan2(x: int, y: int):
    """
    The atan2 tool returns the arc tangent of y/x, in radians. Where x and y are the coordinates of a point (x,y)

    The returned value is between PI and -PI.

    Args:
        - x: Required. Specifies a positive or negative number
        - y: Required. Specifies a positive or negative number
    """

    return math.atan2(x, y)


@mcp.tool("inverse hyperbolic tangent of x")
def atanh(x: int):
    """
    The atanh tool returns the inverse hyperbolic tangent of a number

    Note: The parameter passed in atanh must lie between -0.99 to 0.99.

    Args:
        - x: Required. A positive or negative number between -0.99 and 0.99
    """

    return math.atanh(x)


@mcp.tool("rounds up x")
def ceil(x: int):
    """
    The ceil tool rounds a number UP to the nearest integer, if necessary, and returns the result

    Tip: To round a number DOWN to the nearest integer, look at the floor tool.

    Args:
        - x: Required. Specifies the number to round up
    """

    return math.ceil(x)


@mcp.tool("rounds down x")
def floor(x: int):
    """
    The floor tool rounds a number DOWN to the nearest integer, if necessary, and returns the result

    Tip: To round a number UP to the nearest integer, look at the ceil tool.

    Args:
        - x: Required. Specifies the number to round down
    """

    return math.floor(x)


@mcp.tool("cosine of x")
def cos(x: int):
    """
    The cos tool returns the cosine of a number

    Args:
        - x: Required. A number to find the cosine of
    """

    return math.cos(x)


@mcp.tool("hyperbolic cosine of x")
def cosh(x: int):
    """
    The cosh tool returns the hyperbolic cosine of a number (equivalent to (exp(number) + exp(-number)) / 2)

    Args:
        - x: Required. A number to find the hyperbolic cosine of
    """

    return math.cosh(x)


# The application runner
def main():
    mcp.run(transport="streamable-http", port=8002)


# Run Main
if __name__ == "__main__":
    main()
