import logging
from logging.handlers import RotatingFileHandler
import os

class CustomLogger:
    def __init__(self, name='dev-toolkit-43', log_file='app.log'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        
        # Creative twist: Rotating by size but keeping 5 backups
        handler = RotatingFileHandler(
            log_file, maxBytes=1024 * 1024 * 5, backupCount=5
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
        # Adding a console stream for visibility
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        self.logger.addHandler(console)

    def get_logger(self):
        return self.logger

# Singleton-ish instance for easy import
setup_logger = CustomLogger().get_logger()

def log_debug(msg: str):
    setup_logger.debug(f"[DEBUG] {msg}")

def log_info(msg: str):
    setup_logger.info(f"[INFO] {msg}")

def log_error(msg: str):
    setup_logger.error(f"[ERROR] {msg}")