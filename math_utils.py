def factorial(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer')
    if n < 0:
        raise ValueError('Input must be non-negative')
    if n == 0:
        return 1
    return n * factorial(n - 1)