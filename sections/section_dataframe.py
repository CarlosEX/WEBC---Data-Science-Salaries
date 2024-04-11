import pandas as pd
import streamlit as st
import os

@st.cache_data
def get_dataframe():
    
    path = os.path.join("data","ds_salaries.xlsx")
    df = pd.read_excel(path)
    return df
    