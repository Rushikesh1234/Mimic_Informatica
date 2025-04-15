import pandas as pd

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
