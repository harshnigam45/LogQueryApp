import logging
import json
from logging.handlers import RotatingFileHandler
import datetime

def setup_logger(name, level, logfile):
    """Configure and return a logger with specified name, level, and logfile."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    handler = RotatingFileHandler(logfile, maxBytes=10000, backupCount=5)
    formatter = logging.Formatter('{"level": "%(levelname)s", "log_string": "%(message)s", "timestamp": "%(asctime)s", "metadata": {"source": "%(filename)s"}}', datefmt='%Y-%m-%dT%H:%M:%SZ')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
api_logger1 = setup_logger('api1', logging.INFO, 'log1.log')
api_logger2 = setup_logger('api2', logging.ERROR, 'log2.log')
api_logger3 = setup_logger('api3', logging.WARNING, 'log3.log')

# Simulating log entries
api_logger1.info('Starting the application')
api_logger2.error('Failed to retrieve data')
api_logger3.warning('Execution is slower than expected')
