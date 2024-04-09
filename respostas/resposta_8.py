import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_residencia_mais_comuns_dos_funcionarios(df:pd.DataFrame):
    # ============================================================================================
    # 8 - Quais são os 5 títulos de trabalho mais comuns na empresa?
    # ============================================================================================
    
    
    df_distribuicao_tipos_empregos = df['Job title']

    df_distribuicao_tipos_empregos_counts = df_distribuicao_tipos_empregos.value_counts().reset_index()
    df_distribuicao_tipos_empregos_counts = df_distribuicao_tipos_empregos_counts.rename(columns={'index': 'Título Cargos', 'count': 'Contagem'})
    
    job_title_counts = df_distribuicao_tipos_empregos_counts.head(5)
    
    # Criando o heatmap com Seaborn
    plt.figure(figsize=(10, 6))
    chart_top_five_profissions = sns.barplot(
                x=list(job_title_counts['Job title']), 
                y=list(job_title_counts['Contagem']), 
                palette='vlag')
    
        
    #sns.barplot(job_title_counts, annot=True, cmap='viridis', fmt='d')  # 'annot=True' para mostrar os valores no heatmap
    plt.title('Top 5 títulos de trabalho mais comuns na empresa?')
    plt.xlabel('Profissões', fontsize=12)
    plt.xticks(fontsize=12)
    plt.ylabel('Quantidade', fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(rotation=90)

    for index, value in enumerate(job_title_counts['Contagem']):
        chart_top_five_profissions.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
    
    st.subheader("8 - Quais são os 5 títulos de trabalho mais comuns na empresa?")
    st.pyplot(chart_top_five_profissions.figure)