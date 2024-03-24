"""4. Exiba os nomes das colunas presentes no DataFrame."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Crescimento Populacional - Brasil.csv',sep=';')

for colunas in arquivo.columns:
    
    print(colunas)