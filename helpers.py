import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff=1):
    attempt = 0
    while attempt < retries:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            attempt += 1
            if attempt == retries:
                raise NetworkError(f'Failed to fetch {url} after {retries} attempts') from e
            time.sleep(backoff * (2 ** (attempt - 1)))  # Exponential backoff
            continue
    return None

# Example usage
if __name__ == '__main__':
    try:
        result = retry_request('https://api.example.com/data')
        print(result)
    except NetworkError as e:
        print(e)