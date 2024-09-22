import streamlit as st
import pandas as pd
from sections.social_icons import linkedin_icon, yutube_icon

linkedin_url = "https://www.linkedin.com/in/carlos-antonio-analista/"

def content(df:pd.DataFrame):
    with st.sidebar:
    
        st.title("WEBC - Data Science Salaries")
        st.info("O Data Science Salaries Dataset fornece insights sobre as tendências de remuneração no campo da ciência de dados em vários setores, locais, níveis de experiência e funções.")
        
        # filtro    
        ano_filtered = st.sidebar.selectbox(
            label="Selecione um ano:",
            options=df["Work year"].unique(),
            index=2
        )
            
        # st.warning("https://www.kaggle.com/datasets/zain280/data-science-salaries")
        
        st.divider()
        col1, col2, col3 = st.columns([3,1,1])
        
        with col1:
            st.write(":)")
        with col2:
            pass
            # linkedin_icon(linkedin_url)

        return ano_filtered




