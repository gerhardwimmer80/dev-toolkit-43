import logging
import os
import datetime

class ErrorThresholdRotatingHandler(logging.FileHandler):
    def __init__(self, filename, threshold=5, mode='a', encoding=None, delay=False):
        super().__init__(filename, mode, encoding, delay)
        self.threshold = threshold
        self.counter = 0

    def emit(self, record):
        if record.levelno >= logging.WARNING:
            self.counter += 1
        super().emit(record)
        if self.counter >= self.threshold:
            self.rotate_log()

    def rotate_log(self):
        self.close()
        if os.path.exists(self.baseFilename):
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            dir_name, file_name = os.path.split(self.baseFilename)
            name, ext = os.path.splitext(file_name)
            new_name = f'{name}_{timestamp}{ext}'
            new_path = os.path.join(dir_name, new_name)
            os