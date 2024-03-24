"""5. Verifique se existem valores ausentes no DataFrame e, em caso afirmativo, conte quantos são em cada coluna."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Crescimento Populacional - Brasil.csv',sep=';')

print(arquivo)

valores_ausente = arquivo.isnull().sum() 

print(valores_ausente)