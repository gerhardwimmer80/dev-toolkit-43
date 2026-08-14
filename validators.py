import time
import requests
from requests.exceptions import RequestException

def retry_request(url, retries=3, backoff=1):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            if attempt < retries - 1:
                wait_time = backoff * (2 ** attempt)
                print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print(f"All {retries} attempts failed.")
                raise

# Example use case
if __name__ == '__main__':
    try:
        data = retry_request('https://api.example.com/data')
        print(data)
    except Exception as e:
        print(f"Failed to fetch data: {e}")