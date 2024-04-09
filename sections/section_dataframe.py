import pandas as pd
import streamlit as st

@st.cache_data
def get_dataframe():
    df = pd.read_excel("data\ds_salaries.xlsx")
    return df
    