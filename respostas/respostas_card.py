import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import utils.transform_number as transform
from streamlit_extras.metric_cards import style_metric_cards

def plot_respostas_card(df:pd.DataFrame, year_selected):
    # ===============================================================================
    # RESPOSTA (3,4,5 e 6)
    # ===============================================================================

    st.subheader("1-4. Estatística descritiva Salário Geral")
    st.write(f"Estatística descritiva do Salário Geral (USD) para o ano selecionado: {year_selected}.")
    
    media_salarial = transform.formatar_numero(df['Salary usd'].mean())
    mediana_salarial = transform.formatar_numero(df['Salary usd'].median())
    maior_salario = transform.formatar_numero(df['Salary usd'].max())
    menor_salario = transform.formatar_numero(df['Salary usd'].min())
    desvio_padrao = transform.formatar_numero(df['Salary usd'].std())
    quantile_0_25 = transform.formatar_numero(df['Salary usd'].quantile(0.25))
    quantile_0_75 = transform.formatar_numero(df['Salary usd'].quantile(0.75))
    amplitude = transform.formatar_numero(df['Salary usd'].max() - df['Salary usd'].min())
    
    IQR = transform.formatar_numero(df['Salary usd'].quantile(0.75) - df['Salary usd'].quantile(0.25))
    

    col1, col2, col3 = st.columns(3)

    col1.metric(label="(Média) Salarial", value=media_salarial)
    col1.metric(label="(Mediana) Salarial", value=mediana_salarial)
    col1.metric(label="(Q) 3º Quartil", value=quantile_0_75)
    
    col2.metric(label="(Max) Maior Salário", value=maior_salario)
    col2.metric(label="(Min) Menor Salário", value=menor_salario)
    col2.metric(label="(IQR) Intervalo Interquartil (IQR)", value=IQR)
    
    col3.metric(label="(STD) Desvio Padrão", value=desvio_padrao)
    col3.metric(label="(Q) 1º Quartil", value=quantile_0_25)
    col3.metric(label="(A) Amplitude", value=amplitude)
        
    #col3.metric(label="(A) Amplitude", value=amplitude, delta=0)

    style_metric_cards()
        