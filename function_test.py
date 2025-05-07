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
    """Return the quotient of two numbers.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n == 0 else n * factorial(n - 1)