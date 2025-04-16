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
    
def normalize_column(df, column):
    """Normalize column min-max scaling"""
    try:
        if column in df.columns:
            min_val = df[column].min()
            max_val = df[column].max()

            df[column + '_normalized'] = (df[column] - min_val) / (max_val - min_val)
            log_info(f"Data normalize with min-max scaling for columns")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None

def remove_outliers(df, column, threshold=3):
    """Remove rows where column has outliers based on z-score"""
    try:
        if column in df.columns:
            mean = df[column].mean()
            std = df[column].std()

            df = df[(df[column] - mean).abs() / std < threshold]
            log_info(f"Remove outliers for Data columns")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None

def standardize_column(df, column):
    """Standardize column using z-score"""
    try:
        if column in df.columns:
            df[column + '_zscore'] = (df[column] - df[column].mean()) / df[column].std()
            log_info(f"Data standardize for column")
        return df
    except Exception as e:
        log_error(f"Error cleaning data: {e}")
        return None
