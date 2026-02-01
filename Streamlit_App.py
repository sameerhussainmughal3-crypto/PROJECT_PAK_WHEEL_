import pandas as pd
import streamlit as st

st.title("Car Data Viewer")

uploaded_file = st.file_uploader("Upload CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Cleaning
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'].astype(str).str.replace('[\$,]', '', regex=True), errors='coerce')
    if 'mileage' in df.columns:
        df['mileage'] = pd.to_numeric(df['mileage'].astype(str).str.replace(' km', '', regex=True), errors='coerce')

    st.write("Preview of your data:")
    st.dataframe(df)

    csv = df.to_csv(index=False)
    st.download_button("Download cleaned CSV", csv, "cleaned_data.csv", "text/csv")
