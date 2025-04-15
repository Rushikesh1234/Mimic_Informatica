"""Learn and Understand from - https://docs.python.org/3/library/logging.html and some other docuements including videos"""
import logging
import os

def setup_logger(log_file):
    """Sets up a logger that writes a log in logs/app.log file"""
    if not os.path.exists(os.path.dirname(log_file)):
        os.makedirs(os.path.dirname(log_file))
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)