import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns

def plot_correlacao_nivel_experiencia_por_trabalho_remoto(df:pd.DataFrame):
    st.subheader("12 - Como é a distribuição de Nível de Experiência em relação ao Trabalho Remoto?")

    c_row5_1, c_row5_2 = st.columns([0.4,0.6])
    
    analise = df.groupby(['Remote ratio', 'Experience level']).size().reset_index(name='Contagem')
    analise['Proporção'] = analise.groupby('Remote ratio')['Contagem'].transform(lambda x: x / x.sum())

    mapping = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
    analise['Remote ratio'] = analise['Remote ratio'].map(mapping)

    pivot_table = analise.pivot(index='Experience level', columns='Remote ratio', values='Proporção')

    plt.figure(figsize=(10, 6))
    chart = sns.heatmap(pivot_table, annot=True, cmap='Blues', fmt=".2%", linewidths=.5)
    plt.title('Relação entre Remote ratio e Experience level')
    plt.xlabel('Remote ratio')
    plt.ylabel('Experience level')

    # Adicionando uma seta vertical
    ax = plt.gca()
    ax.annotate('', xy=(3, 1), xytext=(3, 4),
                arrowprops=dict(facecolor='blue', shrink=0.02))
    
    with c_row5_1:
        st.write("Nesta análise, explorei a interseção entre o tipo de rátio remoto e o nível de experiência dos colaboradores. Por meio da avaliação dos dados de contagem de ocorrências para cada combinação de rátio remoto e nível de experiência, pudemos identificar as proporções de cada nível de experiência em relação a cada tipo de rátio remoto.")
        
        pivot = analise.pivot_table(values='Proporção', index='Experience level', columns='Remote ratio',fill_value=0)
        pivot = pivot.applymap(lambda x: "{:.2%}".format(x) if isinstance(x, (float, int)) else x)
        st.dataframe(pivot, use_container_width=True)

    with c_row5_2:
        st.pyplot(chart.figure)


