"""1. Carregue os dados da base de dados do IBGE em um DataFrame."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - População por sexo - Brasil.csv')

# Mostrar arquivo para verificar se a base de dados foi carregada no data frame
print(arquivo)