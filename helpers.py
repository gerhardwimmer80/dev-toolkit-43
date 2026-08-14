def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def is_even(n):
    return n % 2 == 0

def find_max(numbers):
    if not numbers:
        raise ValueError('The list is empty')
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def find_min(numbers):
    if not numbers:
        raise ValueError('The list is empty')
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

def average(numbers):
    if not numbers:
        raise ValueError('The list is empty')
    return sum(numbers) / len(numbers)