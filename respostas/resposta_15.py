import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

from utils.transform_number import thousands_formatter
from matplotlib.ticker import FuncFormatter

def plot_maiores_salarios_por_cargo(df:pd.DataFrame):
 
    
    # Cabeçalho de exercício
    st.subheader("15 - Quais são os maiores salários para cada função em relação ao nível de experiÊncia?")
    st.write("Tabela resumo da classificação de salário por nível de experiência em relação a função exercida")
    
    # Cria tabela resmo
    grouped = df.pivot_table(index='Job title', columns='Experience level', values='Salary usd', aggfunc='max', fill_value=0)
    
    # Cria tabela formatada
    df_formated = grouped.applymap(lambda x: thousands_formatter(x, None) if isinstance(x, (float, int)) else x)
    
    # Mostra os dados da tabela formatada na página
    st.dataframe(df_formated, use_container_width=True)
    
    # cria dfs apenas com dados das colunas por tipo de nível de experiência
    experienced_entry_level = grouped[grouped['Entry Level']>0].filter(['Job title', 'Entry Level']).sort_values(by='Entry Level', ascending=False).reset_index()
    experienced_mid_level = grouped[grouped['Mid-level']>0].filter(['Job title', 'Mid-level']).sort_values(by='Mid-level', ascending=False).reset_index()
    experienced_experienced = grouped[grouped['Experienced']>0].filter(['Job title', 'Experienced']).sort_values(by='Experienced', ascending=False).reset_index()
    experienced_senior = grouped[grouped['Senior']>0].filter(['Job title', 'Senior']).sort_values(by='Senior', ascending=False).reset_index()

    
    # --------------------------------------------------------------------------------------------------
    # CHART:
    # --------------------------------------------------------------------------------------------------
    
    # Criando uma figura e eixos para os subplots
    fig, axs = plt.subplots(2, 2, figsize=(14, 12))
    
    # Plotando os gráficos de barras para cada tipo de experiência
    bars = axs[0, 0].bar(experienced_entry_level.iloc[:,0], experienced_entry_level.iloc[:,1])
    axs[0, 0].set_title('Entry Level')
    axs[0, 0].set_xlabel('Profissões', fontsize=10)
    axs[0, 0].set_ylabel('Quantidade', fontsize=10)
    axs[0, 0].tick_params(axis='x', rotation=90)  # Rotacionando os rótulos do eixo x
    axs[0, 0].set_yticklabels([])
    
    
    # Adicionando rótulos de dados apenas no primeiro e último subplot
    for i, bar in enumerate(bars):
        height = bar.get_height()
        if i == 0 or i == len(bars) - 1:  # Apenas no primeiro e último
            axs[0, 0].annotate(thousands_formatter(height, None),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Offset vertical para o rótulo
                            textcoords="offset points",
                            ha='center', va='bottom')
            
    axs[0, 0].yaxis.set_major_formatter(FuncFormatter(thousands_formatter))


    # ----------------------------------------------------------
    # MID-LEVEL
    # ----------------------------------------------------------
    
    # Plotando os gráficos de barras para cada tipo de experiência
    bars = axs[0, 1].bar(experienced_mid_level.iloc[:,0], experienced_mid_level.iloc[:,1])
    axs[0, 1].set_title('Mid-level')
    axs[0, 1].set_xlabel('Profissões', fontsize=10)
    axs[0, 1].set_ylabel('Quantidade', fontsize=10)
    axs[0, 1].tick_params(axis='x', rotation=90)  # Rotacionando os rótulos do eixo x
    axs[0, 1].set_yticklabels([])
    
    
    # Adicionando rótulos de dados apenas no primeiro e último subplot
    for i, bar in enumerate(bars):
        height = bar.get_height()
        if i == 0 or i == len(bars) - 1:  # Apenas no primeiro e último
            axs[0, 1].annotate(thousands_formatter(height, None),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Offset vertical para o rótulo
                            textcoords="offset points",
                            ha='center', va='bottom')
            
    axs[0, 1].yaxis.set_major_formatter(FuncFormatter(thousands_formatter))
    
    # --------------------------------------------------------------------------------------
    # EEXPERIENCED
    # --------------------------------------------------------------------------------------
    
    # Plotando os gráficos de barras para cada tipo de experiência
    bars = axs[1, 0].bar(experienced_experienced.iloc[:,0], experienced_experienced.iloc[:,1])
    axs[1, 0].set_title('Experienced')
    axs[1, 0].set_xlabel('Profissões', fontsize=10)
    axs[1, 0].set_ylabel('Quantidade', fontsize=10)
    axs[1, 0].tick_params(axis='x', rotation=90)  # Rotacionando os rótulos do eixo x
    axs[1, 0].set_yticklabels([])
    
    # Adicionando rótulos de dados apenas no primeiro e último subplot
    for i, bar in enumerate(bars):
        height = bar.get_height()
        if i == 0 or i == len(bars) - 1:  # Apenas no primeiro e último
            axs[1, 0].annotate(thousands_formatter(height, None),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Offset vertical para o rótulo
                            textcoords="offset points",
                            ha='center', va='bottom')
            
    axs[1, 0].yaxis.set_major_formatter(FuncFormatter(thousands_formatter))

    
    # --------------------------------------------------------------------------------------
    # SENIOR
    # --------------------------------------------------------------------------------------
    
    # Plotando os gráficos de barras para cada tipo de experiência
    bars = axs[1, 1].bar(experienced_senior.iloc[:,0], experienced_senior.iloc[:,1])
    axs[1, 1].set_title('Senior')
    axs[1, 1].set_xlabel('Profissões', fontsize=10)
    axs[1, 1].set_ylabel('Quantidade', fontsize=10)
    axs[1, 1].tick_params(axis='x', rotation=90)  # Rotacionando os rótulos do eixo x
    axs[1, 1].set_yticklabels([])
    
    # Adicionando rótulos de dados apenas no primeiro e último subplot
    for i, bar in enumerate(bars):
        height = bar.get_height()
        if i == 0 or i == len(bars) - 1:  # Apenas no primeiro e último
            axs[1, 1].annotate(thousands_formatter(height, None),
                            xy=(bar.get_x() + bar.get_width() / 2, height),
                            xytext=(0, 3),  # Offset vertical para o rótulo
                            textcoords="offset points",
                            ha='center', va='bottom')
            
    axs[1, 1].yaxis.set_major_formatter(FuncFormatter(thousands_formatter))


    plt.tight_layout(pad=3.0, w_pad=3.0)
    st.pyplot(fig)
    #st.dataframe(experienced_entry_level)