"""9. Crie um gráfico de barras mostrando a distribuição de uma variável categórica."""
import pandas as pd
import matplotlib.pyplot as plt

arquivo_df = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Analise_de_dados\Base de dados IBGE\Indicadores sociais\Censo 2022 - População por cor ou raça - Brasil.csv',sep=';')

print(arquivo_df)

arquivo_df = arquivo_df[['Cor ou raça','População (pessoas)']]

print(arquivo_df)

# Agrupar os valores da coluna 'População (pessoas)' por categoria da variável 'Cor ou raça' e somar
populacao_por_cor_raca = arquivo_df[['Cor ou raça','População (pessoas)']
]
# Criar o gráfico de barras
populacao_por_cor_raca.plot.bar(y='População (pessoas)',x='Cor ou raça',color='skyblue', figsize=(10, 6))
plt.title('População por Cor ou Raça')
plt.xlabel('Cor ou Raça')
plt.ylabel('População (pessoas)')
plt.xticks(rotation=45)  # Rotação dos rótulos do eixo x para facilitar a leitura
plt.grid(axis='y')  # Adicionar linhas de grade no eixo y
plt.tight_layout()  # Ajustar layout para evitar cortes nos rótulos
plt.show()