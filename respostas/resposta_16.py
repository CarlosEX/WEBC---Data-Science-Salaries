import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_correlacao_nivel_experiencia_por_trabalho_remoto(df:pd.DataFrame):

    st.subheader("16 - Existe alguma diferença salarial significativa entre funcionários remotos e não-remotos para o mesmo título de trabalho?")
    # st.write("Para essa análise, estamos levando em consideração o valor da mádia")
    # st.selectbox("Selecione um médida de cálculo:", options=['Média', 'Moda', 'Mediana', 'Máx', 'Min', 'Q1', 'Q2', 'Q3', 'IQR', 'Desvio Padrão'])
    df_filtered = df.loc[(df['Remote ratio'].isin([0,100])), ['Job title', 'Salary usd', 'Experience level', 'Remote ratio']]

    pivot = df_filtered.pivot_table(
        values='Salary usd',
        index=['Job title', 'Remote ratio' ],
        columns=['Experience level'],
        aggfunc='mean',
        fill_value=0
    )
    
    
    def formatar_numero(valor):
        if valor >= 1000000:
            return '{:.0f}M'.format(valor / 1000000)
        elif valor >= 1000:
            return '{:.0f}K'.format(valor / 1000)
        else:
            return '{:,.0f}'.format(valor)
    
    pivot = pivot.map(formatar_numero)
    
    st.dataframe(pivot, use_container_width=True)
