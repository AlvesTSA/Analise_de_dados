"""10.Faça um histograma para visualizar a distribuição de uma variável numérica."""

import pandas as pd
import matplotlib.pyplot as plt

arquivo_df = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - Pirâmide etária - Brasil.csv',sep=';')

arquivo_df = arquivo_df[['Grupo de idade','População feminina(pessoas)']]

x = arquivo_df['Grupo de idade']
y = arquivo_df['População feminina(pessoas)']

plt.figure(figsize=(10, 6))  # Define o tamanho da figura
plt.bar(x, y, color='skyblue')
plt.xlabel('Faixa de Idade')
plt.ylabel('População Feminina (pessoas)')
plt.title('População Feminina por Faixa de Idade')
plt.xticks(rotation=90)  # Rotaciona os rótulos do eixo x para facilitar a leitura
plt.tight_layout()  # Ajusta o layout para evitar sobreposições
plt.show()