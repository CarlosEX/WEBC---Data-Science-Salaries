import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_distribuicao_nivel_experiencia_funcionarios(df:pd.DataFrame):

    # ============================================================================================
    # 6 - Qual é a distribuição dos níveis de experiência dos funcionários?
    # ============================================================================================
       
    experience_distribuicao = df['Experience level']
    df_experience_counts = experience_distribuicao.value_counts().reset_index()
    df_experience_counts = df_experience_counts.rename(columns={'index': 'Nível de Experiência', 'count': 'Contagem'})
    
    # gráfico
    plt.figure(figsize=(12, 8))
    
    chart2 = sns.barplot(
            x=list(df_experience_counts['Experience level']), 
            y=list(df_experience_counts['Contagem']), 
            palette='vlag')
    
    plt.title(' Distribuição dos Níveis de Experiência dos Funcionários',fontsize=16)
    plt.xlabel('Nível de Experiência', fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylabel('Número de Funcionários', fontsize=14)
    plt.yticks(fontsize=12)
    plt.xticks(rotation=90)
    
    # Adicionando rótulos de dados ( valores) no gráfico
    for index, value in enumerate(df_experience_counts['Contagem']):
        chart2.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
        
    st.subheader("6 - Qual é a distribuição dos níveis de experiência dos funcionários?")
    st.pyplot(chart2.figure)