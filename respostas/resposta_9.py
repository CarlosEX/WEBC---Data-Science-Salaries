import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

# ============================================================================================
# PERGUNTA 9
# Qual é a residência mais comum dos funcionários?
# ============================================================================================
    
def plot_residencia_mais_comum_dos_funcionarios(df:pd.DataFrame):
    
    df_locations = df['Company location']
    df_locations_counts = df_locations.value_counts().reset_index()
    df_locations_counts = df_locations_counts.rename(columns={'index': 'Locations', 'count': 'Contagem'})
    
     # gráfico
    plt.figure(figsize=(10, 6))
    
    chart_locations_count = sns.barplot(
            x=list(df_locations_counts['Company location']), 
            y=list(df_locations_counts['Contagem']), 
            palette='vlag')
    
    
    plt.title('Concentração de região mais comuns entre os empregados',fontsize=16)
    plt.xlabel('Tipo de Emprego', fontsize=12)
    plt.xticks(fontsize=12)
    plt.ylabel('Quantidade', fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(rotation=90)
    
    for index, value in enumerate(df_locations_counts['Contagem']):
        chart_locations_count.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
        
    st.subheader("9 - Qual é a residência mais comum dos funcionários?")
    st.pyplot(chart_locations_count.figure)