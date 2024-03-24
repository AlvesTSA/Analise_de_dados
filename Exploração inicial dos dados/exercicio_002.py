"""2. Mostre as primeiras 5 linhas do DataFrame para entender a estrutura dos dados."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - População por cor ou raça - Brasil.csv')

# Mostrar arquivo para verificar se a base de dados foi carregada no data frame
print(arquivo)

print(arquivo.head(5))

