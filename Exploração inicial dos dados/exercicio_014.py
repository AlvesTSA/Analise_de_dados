"""14. Crie um gráfico de pizza mostrando a distribuição percentual de uma variável categórica."""

import pandas as pd
import matplotlib.pyplot as plt

arquivo_df = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Análise_ de_dados\Atividade_001\001_cancer.csv')

contagem = arquivo_df['Grupo'].value_counts()



print(contagem)

data = {'Grupo': ['1', '2', '3', '4'],
'Valores': [56, 146, 95, 65]}

df = pd.DataFrame(data)

total = df['Valores'].sum()

print(total)

df['percentual'] = (df['Valores'] / total) * 100

plt.figure(figsize=(8, 6))
plt.pie(df['percentual'], labels=df['Grupo'], autopct='%1.1f%%', startangle=140)
plt.title('Distribuição Percentual por Grupo')
plt.axis('equal')  # Deixa o gráfico de pizza circular
plt.show()