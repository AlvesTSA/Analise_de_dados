"""12. Crie uma matriz de dispersão para visualizar as relações entre múltiplas variáveis numéricas."""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

arquivo_df = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Crescimento Populacional - Brasil.csv',sep=';')

dados = arquivo_df[['Ano da pesquisa','População(pessoas)']]

sns.pairplot(dados)
plt.show()
