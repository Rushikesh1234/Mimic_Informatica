from src.utils.file_operations import save_data
from src.utils.log import log_error, log_info
import config.settings as config

def load_data(df):
    """Load Transformed Data into CSV File"""
    try:
        save_data(df, config.OUTPUT_PATH)
        log_info(f"Data loaded successfully to {config.OUTPUT_PATH}")
    except Exception as e:
        log_error(f"Error loading data: {e}")