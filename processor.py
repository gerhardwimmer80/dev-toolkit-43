import time
import random
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=5, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Failed to fetch data from {url} after {retries} attempts')
            wait_time = backoff_factor * (2 ** (retries - 1)) + random.uniform(0, 1)
            time.sleep(wait_time)
            print(f'Retry {retries}/{max_retries} for {url} after {wait_time:.2f} seconds')
    raise NetworkError('Max retries exceeded')

# Example Usage
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except NetworkError as e:
        print(e)
