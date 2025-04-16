from src.utils.file_operations import read_data
from src.utils.log import log_info, log_error
import config.settings as config

def extract_data(uploaded_file, file_type):
    """Extract data from CSV File"""
    try:
        df = read_data(uploaded_file, file_type)
        if df is None:
            log_error(f"Error: Data could not be loaded")
            return None
        log_info(f"{file_type} Data Extraction Successful from {uploaded_file}")
        return df
    except Exception as e:
        log_error(f"Error extracting data: {e}")
        return None
