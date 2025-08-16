"""
Lógica:
0 - Enter o desafio que vocÊ quer resolver
1 - Percorrer todos os arquivos da pasta base de dados
2 - Importar as bases de dados de vendas
3 - Tratar / compilar as bases de dados
4 - Calcular o produto mais vendido (em quantidade)
5 - Calcular o produto que mais faturou (em faturamento)
6 - Calcular a loja/cidade que mais vendeu (em faturamento) - criar um gráfico/dashboard
"""
import os
import pandas as pd
import plotly.express as px

lista_arquivo = os.listdir("C:/Users/ester_99rty0a/OneDrive/Documentos/estudos/cursos/python/minicurso-python-hashtag/Vendas")
print(lista_arquivo)

tabelas = []

for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        tabela = pd.read_csv(f"C:/Users/ester_99rty0a/OneDrive/Documentos/estudos/cursos/python/minicurso-python-hashtag/Vendas/{arquivo}")
        tabelas.append(tabela)

        tabela_total = pd.concat(tabelas, ignore_index=True)
print(tabela_total)

tabela_produtos = tabela_total.groupby("Produto").sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)

tabela_total['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
tabela_faturamento = tabela_total.groupby('Produto').sum()
print(tabela_faturamento)
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)

tabela_lojas = tabela_total.groupby('Loja').sum()
tabela_lojas = tabela_lojas[['Faturamento']]
print(tabela_lojas)

grafico = px.bar(tabela_lojas, x=tabela_lojas.index, y='Faturamento')
grafico.show()