import os
import pandas as pd
import plotly.express as px
import streamlit as st


caminho_da_pasta = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Vendas')

tabelas = []

for arquivo in os.listdir(caminho_da_pasta):
    if 'Vendas' in arquivo:
        tabela = os.path.join(caminho_da_pasta, arquivo)
        tabela = pd.read_csv(tabela)
        tabelas.append(tabela)
        
tabela_total = pd.concat(tabelas, ignore_index=True)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]

#streamlit

st.set_page_config(
    page_title="Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
)

st.sidebar.header("🔍 Filtros")
produtos = tabela_total['Produto'].unique()
lojas = tabela_total['Loja'].unique()

produtos_selecionados = st.sidebar.multiselect('Produtos', produtos, default=produtos)
lojas_selecionadas = st.sidebar.multiselect('Loja', lojas, default=lojas)

tabela_filtrada = tabela_total[
    (tabela_total['Produto'].isin(produtos_selecionados)) &
    (tabela_total['Loja'].isin(lojas_selecionadas))
]

tabela_produtos_filtrada = tabela_filtrada.groupby("Produto").sum()
tabela_lojas_filtrada = tabela_filtrada.groupby("Loja").sum()[['Faturamento']]

st.subheader("Produto mais vendido")
st.dataframe(tabela_produtos_filtrada[['Quantidade Vendida']])

st.subheader("Faturamento por Loja")
st.bar_chart(tabela_lojas_filtrada)

st.subheader("Vendas Detalhadas")
st.dataframe(tabela_filtrada)