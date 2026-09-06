import functools
import time
import uuid
from typing import Callable, Any

def memoize_with_expiry(ttl: int = 300):
    def decorator(func: Callable):
        cache = {}
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            if key in cache and now - cache[key][1] < ttl:
                return cache[key][0]
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def generate_slug(length: int = 8) -> str:
    return str(uuid.uuid4())[:length]

def dict_deep_merge(base: dict, update: dict) -> dict:
    for key, value in update.items():
        if isinstance(value, dict) and key in base and isinstance(base[key], dict):
            dict_deep_merge(base[key], value)
        else:
            base[key] = value
    return base

def chain(*funcs: Callable) -> Callable:
    def combined(*args, **kwargs):
        res = funcs[0](*args, **kwargs)
        for f in funcs[1:]:
            res = f(res)
        return res
    return combined

class Registry:
    def __init__(self):
        self._map = {}
    def register(self, name: str):
        def wrapper(func: Callable):
            self._map[name] = func
            return func
        return wrapper
    def __call__(self, name: str, *args, **kwargs) -> Any:
        return self._map[name](*args, **kwargs)