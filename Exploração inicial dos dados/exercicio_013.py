"""13. Agrupe os dados por uma variável categórica e calcule a média de uma variável numérica para cada grupo."""

import pandas as pd

arquivo_df = pd.read_csv(r'C:\Users\thiag\OneDrive\Documentos\GitHub\Análise_ de_dados\Atividade_001\001_cancer.csv')

print(arquivo_df)

media_por_grupo = arquivo_df.groupby('Grupo')['Idade'].mean()

print(media_por_grupo)