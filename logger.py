import logging
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    logging.warning(f'Attempt {attempts}: {e}')
                    if attempts == max_attempts:
                        logging.error('Max attempts reached. Raising exception.')
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

# Example network operation with retry logic
@retry(max_attempts=5, delay=2)
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json() 
