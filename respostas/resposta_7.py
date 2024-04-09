import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_distribuicao_tipos_emprego(df:pd.DataFrame):
    # ============================================================================================
    # 7 - Qual é a distribuição dos tipos de emprego (employment_type)?
    # ============================================================================================
   
    df_distribuicao_tipos_empregos = df['Job title']
    df_distribuicao_tipos_empregos_counts = df_distribuicao_tipos_empregos.value_counts().reset_index()
    df_distribuicao_tipos_empregos_counts = df_distribuicao_tipos_empregos_counts.rename(columns={'index': 'Tipos de Funções', 'count': 'Contagem'})
    
     # gráfico
    plt.figure(figsize=(10, 6))
    
    chart_distribuicao_tipos_empregos = sns.barplot(
            x=list(df_distribuicao_tipos_empregos_counts['Job title']), 
            y=list(df_distribuicao_tipos_empregos_counts['Contagem']), 
            palette='vlag')
    
    plt.title('Distribuição dos Tipos de Cargo (Job Title)',fontsize=16)
    plt.xlabel('Tipo de Emprego', fontsize=12)
    plt.xticks(fontsize=12)
    plt.ylabel('Quantidade', fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(rotation=90)
    
    for index, value in enumerate(df_distribuicao_tipos_empregos_counts['Contagem']):
        chart_distribuicao_tipos_empregos.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
    
    st.subheader("7 - Qual é a distribuição dos tipos de emprego (employment_type)?")
    st.pyplot(chart_distribuicao_tipos_empregos.figure)