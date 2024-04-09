import pandas as pd
import streamlit as st
import duckdb

def execute_sql(df:pd.DataFrame):
    
    
    
    with st.expander("Dataset"):
        st.dataframe(df)
    
    with st.form("my_form"):
        st.info("Realize operações SQL no conjunto de dados")
        text_sql = st.text_area("Query SQL")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            df_result = duckdb.query(text_sql)
            df_result = df_result.fetchdf()
            st.dataframe(df_result)


        
        
