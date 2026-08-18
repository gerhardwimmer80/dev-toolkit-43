def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def unique_elements(iterable):
    seen = set()
    return [x for x in iterable if not (x in seen or seen.add(x))]


def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result


def batch_process(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def safe_divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return float('inf')


def timed_execution(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Function \'{func.__name__}\' executed in {{end_time - start_time:.4f}} seconds')
        return result
    return wrapper

@timed_execution

def example_function(x):
    return [i ** 2 for i in range(x)]

