from src.utils.log import setup_logger, log_error, log_info
from src.extract import extract_data
from src.transform import clean_data
from src.load import load_data

import config.settings as config

setup_logger(config.LOG_PATH)

try:
    log_info(f"Data Extraction Process is executing...")

    # Step 1: Extract Data
    data = extract_data()

    # Step 2: Transform Data
    cleaned_data = clean_data(data)

    # Step 3: Load Data
    load_data(cleaned_data)

    log_info(f"Data Extraction Process has been executed successfully")

except Exception as e:
    log_error(f"Error in Data Extraction Process: {e}")