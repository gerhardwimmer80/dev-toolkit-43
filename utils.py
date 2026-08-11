def safe_divide(numerator, denominator):
    """Safely divide two numbers, avoiding zero division errors."""
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return float('inf')  # Return infinity if division by zero
    return result


def factorial(n):
    """Return the factorial of a number using recursion."""
    if n < 0:
        raise ValueError('Negative values not allowed.')
    return 1 if n == 0 else n * factorial(n - 1)


def flatten_list(nested_list):
    """Flatten a nested list into a single list."""
    flat_list = []
    for elem in nested_list:
        if isinstance(elem, list):
            flat_list.extend(flatten_list(elem))  # Recursion for nested lists
        else:
            flat_list.append(elem)
    return flat_list


def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_fibonacci(n):
    """Generate Fibonacci series up to the nth term."""
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]
