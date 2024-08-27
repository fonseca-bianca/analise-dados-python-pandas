import pandas as pd

# Carregar os dados a partir de um arquivo CSV ou Excel
# Supondo que os dados do ERP tenham sido exportados para um arquivo CSV ou Excel
df = pd.read_csv('dados_floricultura.csv')  # ou pd.read_excel('dados_floricultura.xlsx')

# Exibir as primeiras linhas para entender a estrutura
print(df.head())

# Filtrar registros de perdas
perdas_df = df[df['observacoes'].str.contains('perda', case=False)]

# Exibir as perdas
print(perdas_df.head())

# Total de produtos perdidos
quantidade_total_perdida = perdas_df['quantidade'].sum()
print(f"Quantidade total de produtos perdidos: {quantidade_total_perdida}")

# Agrupar perdas por tipo de produto
perdas_por_produto = perdas_df.groupby('produto')['quantidade'].sum().reset_index()

print(perdas_por_produto)

# Transformar a coluna de datas para datetime se necessário
perdas_df['data'] = pd.to_datetime(perdas_df['data'])

# Agrupar por mês ou dia, conforme sua necessidade
perdas_por_mes = perdas_df.groupby(perdas_df['data'].dt.to_period('M'))['quantidade'].sum().reset_index()

print(perdas_por_mes)

import matplotlib.pyplot as plt

# Exemplo de gráfico de barras para perdas por produto
plt.figure(figsize=(10, 6))
plt.bar(perdas_por_produto['produto'], perdas_por_produto['quantidade'], color='salmon')
plt.xlabel('Produto')
plt.ylabel('Quantidade Perdida')
plt.title('Perdas por Tipo de Produto')
plt.xticks(rotation=45)
plt.show()

# Exemplo de gráfico de linha para perdas por mês
plt.figure(figsize=(10, 6))
plt.plot(perdas_por_mes['data'].astype(str), perdas_por_mes['quantidade'], marker='o', linestyle='-', color='teal')
plt.xlabel('Mês')
plt.ylabel('Quantidade Perdida')
plt.title('Perdas Mensais')
plt.xticks(rotation=45)
plt.show()
