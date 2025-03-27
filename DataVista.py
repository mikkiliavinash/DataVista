import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("📂 Upload and Preview CSV/Excel File")

# File uploader widget
uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])

# If a file is uploaded
if uploaded_file is not None:
    # Check if it's a CSV file
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:  # If it's an Excel file
        df = pd.read_excel(uploaded_file)

    # Show file details
    st.write(f"### File Name: {uploaded_file.name}")
    st.write(f"📏 File Size: {uploaded_file.size / 1024:.2f} KB")

    # Show dataset summary
    st.write("### 🏷️ Summary:")
    st.write(df.describe())
    # Creating the new dataset
    summary_data = {
        "Column_Name": df.columns,
        "Distinct_Count": [df[col].nunique() for col in df.columns],
        "Total_Count": [df[col].count() for col in df.columns],
        "Data_Type": [df[col].dtype for col in df.columns],
        "Nulls":[df[col].isnull().sum() for col in df.columns]
    }

     # Show dataset summary
    st.write("### 🏷️ Details:")
    summarydf=pd.DataFrame(summary_data)
    st.write(summarydf)
