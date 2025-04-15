from src.utils.log import log_info, log_error
import pandas as pd

def clean_data(df):
    """Perform Data Cleaning"""

    try:
        df.columns = df.columns.str.strip()
        log_info(f"Data cleaned: whitespaces removed from column names")

        df.columns = df.columns.str.lower()
        log_info(f"Data cleaned: Convert column values to lower case")

        df.fillna(0, inplace=True)
        log_info(f"Data cleaned: Fill empty columns values with 0")

        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None