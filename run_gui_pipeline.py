import streamlit as st
import pandas as pd

from src.extract import extract_data
from src.transform import clean_data
from src.load import load_data

st.title("Mimic_Informatica")

if st.button("Run ETL"):
    df = extract_data()
    df = clean_data(df)
    load_data(df)
    st.success("ETL Completed")

