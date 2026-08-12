import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            retries += 1
            if retries == max_retries:
                raise NetworkError(f"Failed to fetch data from {url}: {e}")
            time.sleep(backoff_factor * (2 ** (retries - 1)))

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as ne:
        print(ne)