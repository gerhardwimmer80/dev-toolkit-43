import time
import functools
import logging

logger = logging.getLogger('dev-toolkit-43')

def retry_operation(max_attempts=3, delay=1.0, backoff=2.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts, current_delay = 0, delay
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts == max_attempts:
                        logger.error(f'Final attempt failed for {func.__name__}: {e}')
                        raise
                    logger.warning(f'Attempt {attempts} failed for {func.__name__}, retrying in {current_delay}s')
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

@retry_operation(max_attempts=3, delay=0.5)
def fetch_remote_resource(url):
    # Simulate network instability
    import random
    if random.random() < 0.7:
        raise ConnectionError('network handshake failed')
    return {'status': 200, 'data': 'success'}