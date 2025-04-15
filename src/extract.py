from src.utils import read_data
import config.settings as config

def extract_data():
    """Extract data from CSV File"""
    df = read_data(config.INPUT_PATH)
    if df is None:
        print("Error: Data could not be loaded")
        return None
    return df
