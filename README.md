# Python-based ETL Tool (Mimicking Informatica)

This is a Python-based tool for mimicking data preprocessing operations similar to Informatica. The tool includes basic ETL operations like Extract, Transform, and Load. It mimics Informatica's functionality for cleaning and transforming data using Python libraries like Pandas, with options for both CLI and GUI-based interaction.

## Features
- Extracts data from CSV files
- Cleans and transforms data
- Handles missing values, normalization, outliers
- Saves processed data to file
- Logging for traceability
- Streamlit GUI and Command-line interface

## Setup
1. Clone this repository.
2. Install the required Python libraries:
    ```bash
    pip install pandas
    pip install streamlit
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
```

## How to Run

### Option 1: Run from Command Line (CLI)

Execute the full ETL pipeline directly from the terminal:

```bash
python run_pipeline.py
```
### Option 2: Run with Streamlit (GUI)

Launch the interactive UI:

```bash
streamlit run run_gui_pipeline.py
```
![streamlit gui](https://github.com/user-attachments/assets/0cb8a977-7979-4f46-a9b5-9d276a2d1c21)


