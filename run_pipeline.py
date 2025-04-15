from src.extract import extract_data
from src.transform import clean_data
from src.load import load_data

# Step 1: Extract Data
data = extract_data()

# Step 2: Transform Data
cleaned_data = clean_data(data)

# Step 3: Load Data
load_data(cleaned_data)