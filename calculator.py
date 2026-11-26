"""Smart CLI Calculator for UCS 745 Cloud & DevOps Lab Assignment (Q1)."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers, raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def power(a: float, b: float) -> float:
    """Return a raised to the power b."""
    return a ** b


def modulus(a: float, b: float) -> float:
    """Return the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot compute modulus with zero divisor.")
    return a % b


def get_supported_operations() -> list[str]:
    """Return the list of supported calculator operations."""
    return ["add", "subtract", "multiply", "divide", "power", "modulus"]


def format_result(operation: str, a: float, b: float, result: float, precision: int = 2) -> str:
    """Format a calculation result with scientific label and configurable decimal precision."""
    rounded_val = round(result, precision)
    return f"[LOG] {operation.upper()}({a}, {b}) -> {rounded_val:.{precision}f}"


def main() -> None:
    print("=== Smart CLI Calculator v1.2 (Scientific + Precision Edition) ===")
    print("Supported operations:", ", ".join(get_supported_operations()))
    print(format_result("power", 2, 5, power(2, 5), precision=0))
    print(format_result("divide", 22, 7, divide(22, 7), precision=3))


if __name__ == "__main__":
    main()
