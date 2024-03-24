"""7. Identifique e remova possíveis duplicatas no DataFrame."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Crescimento Populacional - Brasil.csv',sep=';')

print(arquivo) #mostra arquivo

duplicado = arquivo.duplicated() #identificação de linhas duplicadas

print(arquivo[duplicado]) #mostra linhas duplicadas

arquivo = arquivo.drop_duplicates() #remoção de linhas duplicadas

print(arquivo) #mostra arquivo atualizado com linhas duplicadas removidas