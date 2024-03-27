"""11. Calcule a correlação entre duas variáveis numéricas no DataFrame."""

import pandas as pd

#arquivos_df = pd.DataFrame()

arquivo1 = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\analfabetismo.csv')

arquivo2 = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\escolarização.csv')

arquivos_df = pd.merge(arquivo1, arquivo2, on='periodo')

print(arquivos_df)

correlacao = arquivos_df['valor_x'].corr(arquivos_df['valor_y'])

print(f'A correlação entre analfabetismo e escolarização é: {correlacao:.2f}')
