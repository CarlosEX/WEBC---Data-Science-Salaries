import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_distribuicao_tamanho_empresa(df:pd.DataFrame):
    c_row6_1, c_row6_2 = st.columns([0.4,0.6])
    
    df_company_size = df['Company size'].value_counts()
    
    colors = ['#8198B8', '#C0C7D4', '#F9F6F5']
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(df_company_size, labels=df_company_size.index, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'fontsize': 14})
    ax.set_title('Distribuição do tamanho das empresas no conjunto de dados',  fontsize=14)
    
    
    with c_row6_1:
        st.subheader("13 - Como o tamanho da empresa é distribuído no conjutno de dados?")
        st.pyplot(fig)
        
    with c_row6_2:
        st.subheader("14 - Estatística descritiva de salário para cada título de trabalho.")
        estatisticas_salario = df.groupby('Job title')['Salary usd'].describe()
        estatisticas_salario['IQR'] = estatisticas_salario['75%'] - estatisticas_salario['25%']
        
        estatisticas_salario = estatisticas_salario.rename(columns={
                                                            '50%': 'Mediana', 
                                                            '25%': 'Quartil 1', 
                                                            '75%': 'Quartil 3',
                                                            'count': 'Count',
                                                            'min': 'Min',
                                                            'max': 'Max'})
        
        estatisticas_salario = estatisticas_salario[['Count', 'Mediana', 'Quartil 1', 'Quartil 3', 'IQR', 'Min','Max']]


        st.data_editor(estatisticas_salario)