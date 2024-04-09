import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sections.section_sidebar as section_sidebar
import sections.section_dataframe as section_dataframe
import sections.section_header as section_header
import sections.section_peguntas as perguntas
import sections.section_sql as section_sql

import utils.transform_number as formater_number
import data.etl_dataframe as etl

from streamlit_extras.metric_cards import style_metric_cards
from sections.social_icons import linkedin_icon, yutube_icon
from streamlit_extras.colored_header import colored_header

from respostas import respostas_card
from respostas import resposta_6
from respostas import resposta_7
from respostas import resposta_8
from respostas import resposta_9
from respostas import resposta_10
from respostas import resposta_11
from respostas import resposta_12
from respostas import resposta_13_14
from respostas import resposta_15
from respostas import resposta_16



# Configurações da página
st.set_page_config(
    page_title="WEBC Analytics",
    initial_sidebar_state='auto',
    layout='wide'
)


# carrega o dataframe
df = section_dataframe.get_dataframe()

# aplica os tratamentos de dados no df
df = etl.transform_dataframe(df)

# SIDER BAR
# Cria o sidebar e retorna o valor do ano selecionado para a variável ano_filtered
ano_filtered = section_sidebar.content(df)


# Aplica formatação css da página
hide_st_style = """
                        <style>
                        header {visibility: hidden}
                        .block-container {padding:25px}
                        #MainMenu {visibility:hidden;}
                        footer {visibility:hidden;}
                        </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# cria as duas principais guias da página principal
tab_dash, tab_info, tab_sql = st.tabs(["📈 Dashboard", "🗃 Detalhes do Conjundo de dados", "Análise SQL"])

with tab_dash:
    
    
    #Header 
    
    st.info("Analisando dados com Python + Pandas e Streamlit")
    
    df_current_year = df[df['Work year'].isin([ano_filtered])] 
    
    
    
    # -------------------------
    # PLOT: ROW 1
    
    respostas_card.plot_respostas_card(df_current_year, ano_filtered)


    st.divider()
    

    # --------------------------------------------------------------------------------------------------
    # PLOT: ROW 2
    c_row2_1, c_row2_2 = st.columns(2)
    
    with c_row2_1:
        resposta_6.plot_distribuicao_nivel_experiencia_funcionarios(df_current_year)
    with c_row2_2:
        resposta_7.plot_distribuicao_tipos_emprego(df_current_year)

    
    st.divider()  
    
    # --------------------------------------------------------------------------------------------------
    # PLOT: ROW 3
    c_row3_1, c_row3_2 = st.columns(2)
    
    with c_row3_1:
        resposta_8.plot_residencia_mais_comuns_dos_funcionarios(df_current_year)
    with c_row3_2:
        resposta_9.plot_residencia_mais_comum_dos_funcionarios(df_current_year)

    st.divider()
    
    # --------------------------------------------------------------------------------------------------
    # PLOT: ROW 4
    c_row4_1, c_row4_2 = st.columns([0.4,0.6])
    
    with c_row4_1:
        resposta_10.plot_remote_distribution(df_current_year)

    with c_row4_2:
        resposta_11.plot_distribuicao_nivel_experiencia_funcionarios(df_current_year)
    
    st.divider()
    
    # --------------------------------------------------------------------------------------------------
    # PLOT: ROW 5
    resposta_12.plot_correlacao_nivel_experiencia_por_trabalho_remoto(df_current_year)
    
    st.divider()
    
    
    # --------------------------------------------------------------------------------------------------
    # PLOT: ROW 6
    # 13 - Como o tamanho da empresa é distribuído no conjutno de dados? Company size
    resposta_13_14.plot_distribuicao_tamanho_empresa(df_current_year)
        
    
    st.divider()
    

    # ------------------------------------------------------------------------------------------------
    # PLOT: ROW 7
    # "15 - Quais são os maiores salários para cada função em relação ao nível de experiÊncia?"
    resposta_15.plot_maiores_salarios_por_cargo(df_current_year)

    
    st.divider()
    
    
    # -------------------------------------------------------------------------------------------------
    # PLOT: ROW 8
    # Existe alguma diferença salarial significativa entre funcionários remotos e não-remotos para o mesmo título de trabalho?
    
    resposta_16.plot_correlacao_nivel_experiencia_por_trabalho_remoto(df_current_year)
    
    st.divider()
    
    st.subheader("17 - Como o tamanho da empresa varia de acordo com o tipo de emprego?")
    
    tamanho_empresa_por_emprego = df_current_year.pivot_table(
        values='Remote ratio', 
        index='Job title',
        columns='Company size',
        aggfunc='count',
        fill_value=0)
    
    st.data_editor(tamanho_empresa_por_emprego)



    st.divider()



    plt.figure(figsize=(12,8),dpi=200)
    c = sns.barplot(y='Salary usd',x='Job title',data=df_current_year, palette="icefire")
    plt.xticks(rotation=90)

    st.pyplot(c.figure)



    st.divider()
    

    # Salary Analysis by Job Title
    plt.figure(figsize=(12, 8))
    sns.boxplot(data=df_current_year, x="Job title", y="Salary usd",palette="mako")
    plt.title("Salary Distribution by Job Title")
    plt.xticks(rotation=90, ha="right")
    plt.tight_layout()
    st.pyplot(plt, use_container_width=True)






  
with tab_info:

    # sobre o arquivo
    st.header("Sobre o Arquivo")
    perguntas.content()
    st.write("O Data Science Salaries Dataset fornece insights sobre as tendências de remuneração no campo da ciência de dados em vários setores, locais, níveis de experiência e funções. Esse conjunto de dados normalmente inclui informações como:")
    
    with st.expander("Dataframe"):
        
        st.data_editor(
            data=df_current_year,
            hide_index=True,
            use_container_width=True)
        
        st.divider()
        st.write("Tamanho do Dataframe")
        
with tab_sql:
    section_sql.execute_sql(df_current_year)