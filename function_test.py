def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return the quotient of three numbers.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(number: int) -> int:
    """Return the factorial of a non-negative integer."""
    if number < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if number == 0 else number * factorial(number - 1)
