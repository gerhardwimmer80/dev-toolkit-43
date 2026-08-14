import time
import requests

class NetworkOperationError(Exception):
    pass

def perform_network_operation(url, retries=3, delay=1):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2  # Exponential backoff
            else:
                raise NetworkOperationError(f'Failed after {retries} attempts: {e}')  

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        result = perform_network_operation(url)
        print(result)
    except NetworkOperationError as e:
        print(e)
