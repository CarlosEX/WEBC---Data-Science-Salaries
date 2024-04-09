import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

def plot_remote_distribution(df:pd.DataFrame):
    
    ratio_counts = df['Remote ratio'].value_counts()
    mapping = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
    ratio_counts.index = ratio_counts.index.map(mapping)
    colors = ['#8198B8', '#C0C7D4', '#F9F6F5']
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(ratio_counts, labels=ratio_counts.index, autopct='%1.1f%%', colors=colors, startangle=90, textprops={'fontsize': 14})
    ax.set_title('Distribuição dos Funcionários por Perfil de Trabalho',  fontsize=14)
    
    st.subheader("10 - Qual é a proporção de funcionários remotos em relação ao total de funcionários?")
    st.pyplot(fig)

# Exemplo de uso:
# df = ... # Seu DataFrame
# fig = plot_remote_distribution(df)
# st.pyplot(fig)
