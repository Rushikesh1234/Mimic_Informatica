# Python-based ETL Tool (Mimicking Informatica)

This is a Python-based tool for mimicking data preprocessing operations similar to Informatica. The tool includes basic ETL operations like Extract, Transform, and Load.

## Setup
1. Clone this repository.
2. Install the required Python libraries:
    ```bash
    pip install pandas
    ```
3. Modify `config/settings.py` to update paths to your raw and processed data files.

## Usage

To run the ETL process:

```python
from src.extract import extract_data
from src.transform import clean_data
from src.load import load_data

# Extract data
data = extract_data()

# Transform data
cleaned_data = clean_data(data)

# Load data
load_data(cleaned_data)
