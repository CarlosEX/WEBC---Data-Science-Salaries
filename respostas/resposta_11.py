import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_distribuicao_nivel_experiencia_funcionarios(df:pd.DataFrame):

    # Agrupe os dados por 'JobTitle' e 'Remote ratio', e calcule a contagem de ocorrências
    analise = df.groupby(['Job title', 'Remote ratio']).size().reset_index(name='Contagem')

    # Para cada 'JobTitle', encontre o rátio remoto com a maior contagem de ocorrências
    resultado = analise.loc[analise.groupby('Remote ratio')['Contagem'].idxmax()]
    
    mapping = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
    resultado['Remote ratio'] = resultado['Remote ratio'].map(mapping)
            
    # Crie um gráfico de barras com Seaborn
    plt.figure(figsize=(12, 8))
    chart = sns.barplot(x='Remote ratio', y='Contagem', hue='Job title', data=resultado)
    plt.title('Contagem de Ocorrências por Tipo de Rátio Remoto e Título de Trabalho', fontsize=14)
    plt.xlabel('Tipo de Rátio Remoto', fontsize=14)
    plt.ylabel('Contagem de Ocorrências', fontsize=14)
    plt.xticks(rotation=90, fontsize=14)
    #   plt.tight_layout()

    # Adicionando rótulos de dados ( valores) no gráfico
    for index, value in enumerate(resultado['Contagem']):
        chart.text(index, value, str(value), ha='center', va='bottom', fontsize=12)
        
    st.subheader("11 - Quais são as funções com mais incidência de trabalho por Remote ratio?","SIM")
    # Exiba o gráfico na interface do Streamlit
    st.pyplot(chart.figure)