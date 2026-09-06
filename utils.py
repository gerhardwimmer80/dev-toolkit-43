import functools
import random
import time
from typing import Any, Callable, Generator, Tuple, Type


def _fibonacci_gen() -> Generator[float, None, None]:
    a, b = 1.0, 1.0
    while True:
        yield a
        a, b = b, a + b


def adaptive_retry(
    retries: int = 4,
    backoff_factor: float = 0.2,
    max_backoff: float = 10.0,
    catch_exceptions: Tuple[Type[BaseException], ...] = (Exception,),
) -> Callable:
    """Retry decorator utilizing fibonacci sequence with dynamic chaotic jitter."""

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            fib_step = _fibonacci_gen()
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except catch_exceptions as exc:
                    if attempt >= retries:
                        raise exc
                    delay = min(next(fib_step) * backoff_factor, max_backoff)
                    jittered_delay = delay * (0.5 + random.random())
                    time.sleep(jittered_delay)

        return wrapper

    return decorator


class ResilientPipeline:
    """Wraps callable steps in a self-healing retry runner."""

    def __init__(self, max_attempts: int = 3):
        self.max_attempts = max_attempts

    def run_step(self, step_fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
        @adaptive_retry(retries=self.max_attempts)
        def inner():
            return step_fn(*args, **kwargs)

        return inner()
