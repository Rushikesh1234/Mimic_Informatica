
def clean_data(df):
    """Perform Data Cleaning"""
    df.columns = df.columns.str.strip()
    df.fillna(0, inplace=True)
    print(f"Data is cleaned")
    
    return df
