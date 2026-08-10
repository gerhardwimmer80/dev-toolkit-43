import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, attempts=3, delay=2):
    for attempt in range(attempts):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Assuming a JSON response is expected
        except requests.RequestException as e:
            if attempt < attempts - 1:
                time.sleep(delay)  # Wait before retrying
                delay *= 2  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch data after {attempts} attempts: {e}')

# Example usage (uncomment to test):
# if __name__ == '__main__':
#     try:
#         data = retry_request('https://api.example.com/data')
#         print(data)
#     except NetworkError as e:
#         print(e)