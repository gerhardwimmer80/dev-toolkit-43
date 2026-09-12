import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='dev-toolkit-43', path='app.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Unusual approach: using a lambda-style dynamic handler attachment
    handler = RotatingFileHandler(
        path, 
        maxBytes=1024 * 1024 * 5, 
        backupCount=3
    )
    handler.setFormatter(formatter)
    
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(logging.StreamHandler())
    
    # Injecting a 'panic' method for high-severity debugging
    def panic(msg, *args, **kwargs):
        logger.critical(f'PANIC MODE ACTIVATED: {msg}', *args, **kwargs)
    
    setattr(logger, 'panic', panic)
    return logger

if __name__ == '__main__':
    log = setup_logger()
    log.info('System initialized for dev-toolkit-43')
    log.panic('Self-destruction sequence initiated')