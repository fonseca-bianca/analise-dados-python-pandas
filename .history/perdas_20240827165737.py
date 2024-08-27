import pandas as pd

# carregar os dados a partir de um arquivo CSV ou Excel
# supondo que os dados do ERP tenham sido exportados para um arquivo CSV ou Excel
df = pd.read_csv("dados_floricultura.csv")  # ou arquivo em Excel --> pd.read_excel('dados_floricultura.xlsx')

print(df.head())

# filtrar registros das perdas
perdas_df = df[df["observacoes"].str.contains("perda", case=False)]

# exibir as perdas dos produtos
print(perdas_df.head())

# o total de produtos perdidos
quantidade_total_perdida = perdas_df["quantidade"].sum()
print(f"Quantidade total de produtos perdidos: {quantidade_total_perdida}")

# agrupar as perdas por tipo de produto
perdas_por_produto = perdas_df.groupby('produto')['quantidade'].sum().reset_index()

print(perdas_por_produto)

# transformar a coluna de datas para datetime (se for necessário)
perdas_df["data"] = pd.to_datetime(perdas_df["data"])

# agrupar as perdas por mês ou dia, conforme a necessidade da floricultura
perdas_por_mes = perdas_df.groupby(perdas_df["data"].dt.to_period("M"))["quantidade"].sum().reset_index()

print(perdas_por_mes)

####################################################################
# visualizar os dados para identificar padrões de perda e tomar as decisões cabíveis
import matplotlib.pyplot as plt

# uso de gráfico de barras para perdas por produto
plt.figure(figsize=(10, 6))
plt.bar(perdas_por_produto["produto"], perdas_por_produto["quantidade"], color="pink")
plt.xlabel("Produto")
plt.ylabel("Quantidade Perdida")
plt.title("Perdas por Tipo de Produto")
plt.xticks(rotation=45)
plt.show()

# uso de gráfico de linha para perdas de produtos por mês
plt.figure(figsize=(10, 6))
plt.plot(perdas_por_mes["data"].astype(str), perdas_por_mes["quantidade"], marker="o", linestyle="-", color="red")
plt.xlabel("Mês")
plt.ylabel("Quantidade prodito perdida")
plt.title("Perdas mensais")
plt.xticks(rotation=45)
plt.show()
