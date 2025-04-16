import streamlit as st
import pandas as pd
import inspect
from src.extract import extract_data
from src.transform import Transformations
from src.load import load_data


st.title("Mimic_Informatica")

file_type = st.selectbox("Select file type to upload", ["CSV", "Excel", "JSON"])
uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])

steps = []

if uploaded_file:
    try:
        for name in Transformations:
            if st.sidebar.button(f"Add: {name}"):
                steps.append({"name":name, "params":{}})

            for i, step in enumerate(steps):
                st.sidebar.markdown(f"**Step {i+1}: {step['name']}**")
                fn = Transformations[step["name"]]
                sig = inspect.signature(fn)
                for p in sig.parameters.values():
                    if p.name == "df" : continue
                    default = p.default if p.default is not inspect._empty else ""
                    val = st.sidebar.text_input(f"{step['name']} -> {p.name}", value= str(default), key=f"{i}-{p.name}")
                    step["params"][p.name] = eval(val)
            
            if st.button("Run Pipeline"):
                df = extract_data(uploaded_file, file_type)
                st.success("Data uploaded successfully.")
                st.subheader("Original uploaded data")
                st.dataframe(df, use_container_width=True)

                st.subheader("Data Transformation in progress..")
                for step in steps:
                    fn = Transformations[step["name"]]
                    df = fn(df, **step["params"])
                st.success(f"Data Transformed/Processed successfully.")
                st.dataframe(df, use_container_width=True)

                st.subheader("Export Transformed Data")
                export_format = st.selectbox("Choose export format", ["CSV", "Excel", "JSON"])
                export_btn = st.button("Download processed data")
                
                if export_btn:
                    output_file, file_name = load_data(df, export_format)
                    st.download_button("Click to download", data=output_file, file_name=file_name)
                    st.success("ETL Completed")

    except Exception as e:
        st.error(f"Failed to read file")
        st.stop()    


# Normal Process - Basic ETL Steps

# st.title("Mimic_Informatica")

# file_type = st.selectbox("Select file type to upload", ["CSV", "Excel", "JSON"])
# uploaded_file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])

# if uploaded_file:
#     try:
#         df = extract_data(uploaded_file, file_type)
#         st.success("Data uploaded successfully.")
#         st.subheader("Original uploaded data")
#         st.dataframe(df, use_container_width=True)

#         st.subheader("Transformed Data")
#         df = clean_data(df)
#         st.success(f"Data Transformed/Processed successfully.")

#         st.subheader("Export Transformed Data")
#         export_format = st.selectbox("Choose export format", ["CSV", "Excel", "JSON"])
#         export_btn = st.button("Download processed data")
        
#         if export_btn:
#             output_file, file_name = load_data(df, export_format)
#             st.download_button("Click to download", data=output_file, file_name=file_name)
#             st.success("ETL Completed")
#     except Exception as e:
#         st.error(f"Failed to read file")
#         st.stop()