import logging
from logging.handlers import RotatingFileHandler
import sys

def setup_logger(name: str = "dev_toolkit", log_file: str = "app.log") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if logger.handlers:
        return logger

    log_format = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s"
    formatter = logging.Formatter(log_format)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    try:
        file_handler = RotatingFileHandler(
            log_file, 
            maxBytes=1048576, 
            backupCount=3, 
            encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    except IOError as e:
        logger.warning(f"Failed to initialize file logger: {e}")

    return logger

if __name__ == "__main__":
    log = setup_logger()
    log.info("Logger initialized successfully with rotation.")
