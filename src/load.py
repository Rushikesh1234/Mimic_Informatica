from src.utils import save_data
import config.settings as config

def load_data(df):
    """Load Transformed Data into CSV File"""
    save_data(df, config.OUTPUT_PATH)
