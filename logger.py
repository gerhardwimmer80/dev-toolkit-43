import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_size=5*1024*1024, backup_count=3):
    logger = logging.getLogger('RotatingLogger')
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(log_file, maxBytes=max_size, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    if not logger.hasHandlers():
        logger.addHandler(handler)
    
    return logger

# Example usage of the logger
if __name__ == '__main__':
    log = setup_logger()
    log.info('Logger setup complete')
    log.error('This is an error message')
    log.warning('This is a warning message')