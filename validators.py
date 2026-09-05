import time
import functools
from typing import Callable, Any

def retry_operation(max_attempts: int = 3, delay: float = 1.0):
    """Decorator implementing exponential backoff for network instability."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = delay
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except (ConnectionError, TimeoutError) as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
            raise last_exception
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=0.5)
def fetch_remote_resource(url: str) -> str:
    # simulate potential unstable network call
    import random
    if random.random() < 0.7:
        raise ConnectionError("transient network glitch")
    return f"content from {url}"