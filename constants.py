import time
import random

RETRY_MAX_ATTEMPTS = 5
RETRY_DELAY_BASE = 1  # seconds

EXCEPTIONS_TO_HANDLE = (ConnectionError, TimeoutError)


def retry_operation(operation, max_retries=RETRY_MAX_ATTEMPTS, base_delay=RETRY_DELAY_BASE):
    attempts = 0
    while attempts < max_retries:
        try:
            return operation()
        except EXCEPTIONS_TO_HANDLE as e:
            attempts += 1
            delay = base_delay * (2 ** (attempts - 1)) + random.uniform(0, 1)  # Jitter
            print(f'Attempt {attempts} failed: {e}. Retrying in {delay:.2f} seconds.')
            time.sleep(delay)
    raise Exception(f'Operation failed after {max_retries} attempts')

