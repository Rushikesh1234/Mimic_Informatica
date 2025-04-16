from src.utils.file_operations import save_data
from src.utils.log import log_error, log_info
import config.settings as config

def load_data(df, file_type):
    """Load Transformed Data into CSV File"""
    try:
        output_file, file_name = save_data(df, file_type)
        log_info(f"{file_type} Data loaded successfully")
        return output_file, file_name
    except Exception as e:
        log_error(f"Error loading data: {e}")