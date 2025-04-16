import json
import pandas as pd
from src.utils.log import log_error, log_info
from io import StringIO, BytesIO

def read_data(file_path, file_format):
    
    try:
        '''Read Data from different file_format'''
        if file_format == 'CSV':
            df = pd.read_csv(file_path)  
            log_info(f"{file_format} Data loaded from {file_path}")
            return df
        elif file_format == 'Excel':
            df = pd.read_excel(file_path)  
            log_info(f"{file_format} Data loaded from {file_path}")
            return df
        elif file_format == "JSON":
            df = pd.read_json(file_path)  
            log_info(f"{file_format} Data loaded from {file_path}")
            return df
        else:
            log_error(f"Invalid File Format: {file_format} for {file_path}")
            return None 
    except Exception as e:
        log_error(f"Error loading data: {e}")
        return None
    
def save_data(df, file_format):
    try:
        """Save Data to different File Format"""
        if file_format == 'CSV':
            output_file, file_name =  df.to_csv(index=False).encode('utf-8'), 'processed_data.csv'
            log_info(f"{file_format} Data saved successfully.")
            return output_file, file_name
        elif file_format == 'Excel':
            output = BytesIO()
            df.to_excel(output, index=False, engine='openpyxl')
            output_file, file_name = output.getvalue(), 'processed_data.xlsx'
            log_info(f"{file_format} Data saved successfully")
            return output_file, file_name
        elif file_format == 'JSON':
            output_file, file_name = df.to_json(orient='records'), 'processed_data.json'
            log_info(f"{file_format} Data saved successfully")
            return output_file, file_name
        else:
            log_error(f"Invalid File Format: {file_format}")
    except Exception as e:
        log_error(f"Error loading data: {e}")


'''
def read_data(file_path):
    """Read Data from CSV File"""
    try:
        df = pd.read_csv(file_path)  
        print(f"Data loaded from {file_path}")
        return df
    except Exception as e:
        print(f"Error reading data: {e}")
        return None
    
def save_data(df, file_path):
    """Save Data to CSV File"""
    try:
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data: {e}")
'''