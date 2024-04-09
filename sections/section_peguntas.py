import streamlit as st
import pandas as pd

data = [
        ("1 - Qual a média geral dos salários do ano selecionado?", "SIM"), 
        ('2 - Qual a mediana geral dos salários do ano selecionado?', "SIM"), 
        ('3 - Qual o valor do desvio padrão geral dos salários do ano selecionado?', "SIM"),
        ("4 - Qual o maior salário do ano selecionado?","SIM"),
        ("5 - Qual o menor salário do ano selecionado?","SIM"),
        ("6 - Qual é a distribuição dos níveis de experiência dos funcionários?","SIM"),
        ("7 - Qual é a distribuição dos tipos de emprego (employment_type)?","SIM"),
        ("8 - Quais são os 5 títulos de trabalho mais comuns na empresa?","SIM"),
        ("9 - Qual é a residência mais comum dos funcionários?","SIM"),
        ("10 - Qual é a proporção de funcionários remotos em relação ao total de funcionários?","SIM"),
        ("11 - Quais são as funções com mais incidência de trabalho por Remote ratio?","SIM"),
        ("12 - Como é a distribuição de Nível de Experiência em relação ao Trabalho Remoto?","SIM"),
        ("13 - Como o tamanho da empresa é distribuído no conjutno de dados?","SIM"),
        ("14 - Estatística descritiva de salário para cada título de trabalho?","SIM"),
        ("15 - Quais são os maiores salários para cada função em relação ao nível de experiÊncia?","SIM"),
        ("16 - Existe alguma diferença salarial significativa entre funcionários remotos e não-remotos para o mesmo título de trabalho?","SIM"),
        ("17 - Como o tamanho da empresa varia de acordo com o tipo de emprego?","NÃO"),
        ("Como o tamanho da empresa varia de acordo com o trabalho remoto?","NÃO"),
        ("Existe alguma diferença salarial significativa entre diferentes países de residência dos funcionários?","NÃO"),
        ("Existe alguma correlação entre o salário e a proporção de funcionários remotos?","NÃO"),
        ("Qual é a proporção de funcionários em tempo integral versus meio período?","NÃO"),
        ("Como a distribuição salarial varia entre os diferentes níveis de experiência?","NÃO"),
        ("Como o salário dos funcionários se compara entre diferentes tipos de emprego e níveis de experiência?","NÃO"),
        ("Existe alguma relação entre o tipo de emprego e a localização geográfica da empresa?","NÃO"),
        ("Existe alguma correlação entre o tipo de emprego e o tamanho da empresa?","NÃO"),
        ("Existe alguma correlação no salário entre o tipo de função e o tamanho da empresa","NÃO"),
        ("Como a distribuição dos tipos de emprego varia entre diferentes países de residência dos funcionários?","NÃO"),
        ("Existe alguma diferença salarial significativa entre funcionários que trabalham em empresas de diferentes tamanhos?","NÃO"),
        ("Existe uma relação entre o tamanho da empresa e a proporção de funcionários em diferentes níveis de experiência?","NÃO")
    ]

# Função para aplicar estilo
def highlight_sim(value):
    if value == 'SIM':
        return 'color: white; background-color: green'
    else:
        return 'color: white; background-color: orange'
    
def content():
    df = pd.DataFrame(data=data, columns=['Perguntas de Negócio', 'Status'])
    styled_df = df.style.applymap(highlight_sim, subset=['Status'])
    st.dataframe(styled_df)