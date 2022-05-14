
def factorial(n):
    """
    Calculates the factorial of n.
    """
    return 1 if n == 0 else n * factorial(n-1)
