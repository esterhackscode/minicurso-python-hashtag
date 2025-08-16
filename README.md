# 📊 Dashboard de Vendas

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

---
## Sumário

- [Sobre](#-sobre)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Estrutura do Código](#-estrutura-do-código)
- [Exemplo de Uso](#-exemplo-de-uso)
- [Licença](#-licença)

---
## Sobre
Utilizei o minicurso de Python da Hashtag Programação para treinar mais e tomei a liberdade de treinar também streamlit.

---
## Funcionalidades
Este projeto consiste em um **dashboard interativo de vendas** desenvolvido em Python com Streamlit. O dashboard permite:
- Visualizar produtos mais vendidos.
- Analisar o faturamento por loja.
- Filtrar dados por produto e loja.
- Explorar vendas detalhadas de forma interativa.

Os dados são carregados a partir de arquivos CSV presentes na pasta `Vendas` e agregados automaticamente.

## Tecnologias

- **Python**: Linguagem de programação principal.
- **Pandas**: Manipulação e agregação de dados.
- **Plotly**: Visualização interativa (gráficos).
- **Streamlit**: Criação do dashboard web interativo.

## Estrutura do Código

1. **Carregamento de arquivos CSV**:  
   - Todos os arquivos que contêm `Vendas` no nome são lidos automaticamente.
   - Os dados são concatenados em um único DataFrame.

2. **Cálculo do Faturamento**:  
   - Adiciona-se uma coluna `Faturamento` = `Quantidade Vendida` × `Preço Unitário`.

3. **Agregação de dados**:  
   - `tabela_produtos`: Soma de vendas por produto.
   - `tabela_lojas`: Soma de faturamento por loja.

4. **Filtros interativos com Streamlit**:  
   - Selecione produtos e lojas na barra lateral.
   - O dashboard atualiza gráficos e tabelas conforme os filtros.

5. **Visualizações**:  
   - Tabela de produtos mais vendidos.
   - Gráfico de barras do faturamento por loja.
   - Tabela detalhada de todas as vendas filtradas.

## Exemplo de Uso

Ao acessar o dashboard, use a barra lateral para filtrar produtos e lojas.
Observe a atualização automática dos gráficos e tabelas conforme as seleções.

## Licença

Este projeto está sob a licença MIT.
Sinta-se livre para usar, modificar e compartilhar.
