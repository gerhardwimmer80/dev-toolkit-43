import time
import requests

class NetworkError(Exception):
    pass

def retry_operation(func, max_retries=3, delay=2, *args, **kwargs):
    retries = 0
    while retries < max_retries:
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f'Request failed after {max_retries} attempts') from e
            time.sleep(delay)

def fetch_data(url):
    response = retry_operation(requests.get, url=url)
    response.raise_for_status()
    return response.json()

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = fetch_data(url)
        print(data)
    except NetworkError as e:
        print(f'Error fetching data: {e}')