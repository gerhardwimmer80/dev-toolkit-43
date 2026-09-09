import functools
import collections
import time

class MemoizeCache:
    def __init__(self, ttl=300):
        self.cache = {}
        self.ttl = ttl

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (func.__name__, args, frozenset(kwargs.items()))
            now = time.time()
            if key in self.cache:
                result, timestamp = self.cache[key]
                if now - timestamp < self.ttl:
                    return result
            result = func(*args, **kwargs)
            self.cache[key] = (result, now)
            return result
        return wrapper

def batch_process(data, chunk_size=100):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def fast_lookup(iterable, key_func):
    lookup = collections.defaultdict(list)
    for item in iterable:
        lookup[key_func(item)].append(item)
    return lookup

class AsyncBuffer:
    def __init__(self, limit=1000):
        self.storage = collections.deque(maxlen=limit)
    
    def push(self, item):
        self.storage.append(item)
    
    def flush(self):
        items = list(self.storage)
        self.storage.clear()
        return items