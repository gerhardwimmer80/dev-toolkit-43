import time
import random

MAX_RETRIES = 5
DELAY_MULTIPLIER = 2
BASE_DELAY = 1

class RetryException(Exception):
    pass


def retry_decorator(func):
    def wrapper(*args, **kwargs):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == MAX_RETRIES:
                    raise RetryException(f'Operation failed after {MAX_RETRIES} attempts') from e
                delay = BASE_DELAY * (DELAY_MULTIPLIER ** (attempt - 1)) + random.uniform(0, 1)
                time.sleep(delay)
                print(f'Retry #{attempt} for {func.__name__} in {delay:.2f} seconds')
    return wrapper

@retry_decorator
def network_operation():
    if random.choice([True, False]):
        raise Exception('Network error occurred')
    return 'Success!'

if __name__ == '__main__':
    try:
        result = network_operation()
        print(result)
    except RetryException as e:
        print(e)