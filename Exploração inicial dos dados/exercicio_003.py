"""3. Verifique quantas colunas e linhas existem no DataFrame."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Pirâmide etária - Brasil.csv',sep=';')

"""como o separador de colunas padrão do pandas é ',' então terei que usar o parametro 'sep' do metodo read_csv para indicar que o separador das colunas dessa base de dados é ';'  """

print(arquivo.columns) #verificar as colunas existente no dataframe 
arquivo = arquivo.drop(columns=['Unnamed: 4','Unnamed: 5']) 

"""ao verificar percebeu-se que havia colunas vazias, chamadas de 'Unnamed: 4' e 'Unnamed: 5', então essa linha de codigo com o metodo drop removeu as colunas indesejadas para fazer a contagem correta das colunas"""

num_colunas = len(arquivo.columns)
num_linhas = len(arquivo.index)

print(f'Número de colunas: {num_colunas}')
print(f'Números de linhas: {num_linhas}')