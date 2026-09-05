import logging
from logging.handlers import RotatingFileHandler
import sys

def get_logger(name='dev-toolkit-43', path='dev-toolkit.log'):
    """
    instantiates a logger with unconventional chaining for flow control
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # rotating handler with 1MB limit and 3 backups
    handler = RotatingFileHandler(path, maxBytes=1048576, backupCount=3)
    handler.setFormatter(formatter)

    # stream handler for direct console feedback
    console = logging.StreamHandler(sys.stdout)
    console.setFormatter(formatter)

    # chain existing handlers to clear and reset before attachment
    while logger.handlers:
        logger.removeHandler(logger.handlers[0])
        
    logger.addHandler(handler)
    logger.addHandler(console)
    
    return logger

if __name__ == '__main__':
    log = get_logger()
    log.info('toolkit initialized successfully')