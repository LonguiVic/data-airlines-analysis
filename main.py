import pandas as pd
import sqlite3
import calendar
from sazonalidade_vendas import plot_sazonalidade_vendas
from top_10_clientes import criar_grafico_top_10_clientes

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('vendas.db')

# Carregar dados do banco de dados
df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)

# Calcular o valor total da venda e atribuí-lo à coluna 'valor_total'
df_sqlite['valor_total'] = df_sqlite['preco'] * df_sqlite['quantidade']

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

# Combinar os DataFrames usando a função concat, concatenando-os verticalmente
df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)

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
print(clientes_lucrativos)

# Calcular o valor total das vendas por mês para analisar a sazonalidade das vendas
vendas_por_mes = df_combined.groupby('mes_compra')['valor_total'].sum().reset_index()

# Renomear a coluna 'mes_compra' para 'Mês'
vendas_por_mes.rename(columns={'mes_compra': 'Mês'}, inplace=True)

# Plotar a sazonalidade das vendas por mês
plot_sazonalidade_vendas(vendas_por_mes)

# Plotar gráfico dos top 10 clientes mais lucrativos
criar_grafico_top_10_clientes(clientes_lucrativos)
