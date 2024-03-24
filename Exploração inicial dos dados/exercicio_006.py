"""6. Remova linhas que contenham valores ausentes."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Crescimento Populacional - Brasil.csv',sep=';')

print(arquivo)

arquivo = arquivo.drop(columns=['Unnamed: 3', 'Unnamed: 4'])

print(arquivo)