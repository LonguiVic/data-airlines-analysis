import pandas as pd
import sqlite3
import datetime
import matplotlib.pyplot as plt

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('vendas.db')

# Carregar dados do banco de dados
df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)

# Calcular o valor total da venda e atribuí-lo à coluna 'valor_total'
df_sqlite['valor_total'] = df_sqlite['preco'] * df_sqlite['quantidade']

# Imprimir nome da tabela antes de imprimir o DataFrame do SQLite
print("Tabela SQLite: vendas_db_sqlite")
print("---------------------------------------------------------------------------------------------------------------------------")
print(df_sqlite.head())
print("\n" * 2)  # Adicionando espaçamento entre os DataFrames

# Fechar conexão com o banco de dados
conn.close()

# Carregar dados do arquivo CSV
df_csv = pd.read_csv('vendas_db.csv')

# Criar um campo de ID para o DataFrame CSV
df_csv['id'] = df_csv.index + 1

# Reorganizar as colunas, colocando 'id' como a primeira coluna
cols = ['id'] + [col for col in df_csv.columns if col != 'id']
df_csv = df_csv[cols]

# Calcular o valor total das vendas para o DataFrame CSV
df_csv['valor_total'] = df_csv['preco'] * df_csv['quantidade']

# Imprimir nome da tabela antes de imprimir o DataFrame CSV
print("Tabela CSV: vendas_df_csv")
print("---------------------------------------------------------------------------------------------------------------------------")
print(df_csv.head())
print("\n" * 2)  # Adicionando espaçamento entre os DataFrames

# Combinar os DataFrames usando a função concat, concatenando-os verticalmente
df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)

# Imprimir o DataFrame combinado
print("Tabela combinada:")
print("---------------------------------------------------------------------------------------------------------------------------")
print(df_combined)
print("\n" * 2)  # Adicionando espaçamento entre os DataFrames

# Converter a coluna 'data_compra' para o tipo datetime
df_combined['data_compra'] = pd.to_datetime(df_combined['data_compra'])

# Extrair o mês da data de compra
df_combined['mes_compra'] = df_combined['data_compra'].dt.month

# Calcular o valor total das vendas por cliente
clientes_lucrativos = df_combined.groupby('cliente_nome')['valor_total'].sum().reset_index()

# Ordenar os clientes com base no valor total das vendas (do maior para o menor)
clientes_lucrativos = clientes_lucrativos.sort_values(by='valor_total', ascending=False)

# Redefinir o índice para obter IDs numéricos para os clientes
clientes_lucrativos.reset_index(inplace=True)

# Renomear a coluna de índice para 'ID'
clientes_lucrativos.rename(columns={'index': 'ID'}, inplace=True)

# Imprimir os clientes mais lucrativos com ID
print("Clientes mais lucrativos:")
print("--------------------------------------")
print(clientes_lucrativos[['ID', 'cliente_nome', 'valor_total']].head())
print("\n" * 2)  # Adicionando espaçamento entre os DataFrames

# Calcular o valor total das vendas por mês para analisar a sazonalidade das vendas
vendas_por_mes = df_combined.groupby('mes_compra')['valor_total'].sum().reset_index()

# Renomear a coluna 'mes_compra' para 'Mês'
vendas_por_mes.rename(columns={'mes_compra': 'Mês'}, inplace=True)

# Imprimir a sazonalidade das vendas por mês
print("Sazonalidade de vendas por mês:")
print("----------------------------------")
print(vendas_por_mes.to_string(index=False, header=["Mês", "Total de Vendas"]))

# Plotar gráfico de barras dos top 10 clientes mais lucrativos
plt.figure(figsize=(10, 6))
plt.bar(clientes_lucrativos['cliente_nome'][:10], clientes_lucrativos['valor_total'][:10], color='skyblue')
plt.title('Top 10 Clientes Mais Lucrativos')
plt.xlabel('Clientes')
plt.ylabel('Valor Total das Compras')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Plotar a sazonalidade das vendas por mês
plt.figure(figsize=(10, 6))
plt.plot(vendas_por_mes['Mês'], vendas_por_mes['valor_total'], marker='o', color='green', linestyle='-')
plt.title('Sazonalidade de Vendas por Mês')
plt.xlabel('Mês')
plt.ylabel('Total de Vendas')
plt.grid(True)
plt.tight_layout()
plt.show()