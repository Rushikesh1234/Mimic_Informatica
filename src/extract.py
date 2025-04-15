from src.utils.file_operations import read_data
from src.utils.log import log_info, log_error
import config.settings as config

def extract_data():
    """Extract data from CSV File"""
    try:
        df = read_data(config.INPUT_PATH)
        if df is None:
            log_error(f"Error: Data could not be loaded")
            return None
        log_info(f"Data Extraction Successful from {config.INPUT_PATH}")
        return df
    except Exception as e:
        log_error(f"Error extracting data: {e}")
        return None
