import json
from datetime import datetime

class RequestHandler:
    def __init__(self, request):
        self.request = request
        self.response = {}

    def process(self):
        self.log_request()
        self.validate_request()
        self.create_response()
        return self.response

    def log_request(self):
        print(f"[{datetime.now()}] Incoming request: {json.dumps(self.request)}")

    def validate_request(self):
        if 'data' not in self.request:
            raise ValueError('Invalid request: Missing data')

    def create_response(self):
        self.response = {'status': 'success', 'data': self.request['data']}