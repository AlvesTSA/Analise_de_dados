"""8. Calcule a média, mediana, mínimo e máximo de uma coluna numérica específica."""

import pandas as pd

arquivo = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\mortalidade-infantil-óbitos-a-cada-mil-nascidos-vivos.csv')

print(arquivo)

media = arquivo['valor'].mean()
mediana = arquivo['valor'].median()
minimo = arquivo['valor'].min()
maximo = arquivo['valor'].max()

print("Media: {:.2f}\nMediana: {:.2f}\nMínimo: {}\nMáximo: {}".format(media,mediana,minimo,maximo))

