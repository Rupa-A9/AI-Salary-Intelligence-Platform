import streamlit as st

from utils.data_loader import load_csv
from utils.validator import validate_dataframe

st.title("Salary Prediction")

uploaded_file = st.file_uploader(
    "Upload Employee Dataset",
    type=["csv"]
)

if uploaded_file:

    df = load_csv(uploaded_file)

    st.success("Dataset uploaded successfully.")

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    report = validate_dataframe(df)

    st.subheader("Dataset Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", report["Rows"])
        st.metric("Columns", report["Columns"])

    with col2:
        st.metric("Missing Values", report["Missing Values"])
        st.metric("Duplicate Rows", report["Duplicate Rows"])