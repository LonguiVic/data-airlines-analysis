import pandas as pd
import sqlite3
import calendar
from sazonalidade_vendas import plot_sazonalidade_vendas
from top_10_clientes import criar_grafico_top_10_clientes

conn = sqlite3.connect('vendas.db')

df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)

df_sqlite['valor_total'] = df_sqlite['preco'] * df_sqlite['quantidade']

conn.close()

df_csv = pd.read_csv('vendas_db.csv')

df_csv['id'] = df_csv.index + 1

cols = ['id'] + [col for col in df_csv.columns if col != 'id']
df_csv = df_csv[cols]

df_csv['valor_total'] = df_csv['preco'] * df_csv['quantidade']

df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)

df_combined['data_compra'] = pd.to_datetime(df_combined['data_compra'])

df_combined['mes_compra'] = df_combined['data_compra'].dt.month

clientes_lucrativos = df_combined.groupby('cliente_nome')['valor_total'].sum().reset_index()

clientes_lucrativos = clientes_lucrativos.sort_values(by='valor_total', ascending=False)

clientes_lucrativos.reset_index(inplace=True)

clientes_lucrativos.rename(columns={'index': 'ID'}, inplace=True)


vendas_por_mes = df_combined.groupby('mes_compra')['valor_total'].sum().reset_index()

vendas_por_mes.rename(columns={'mes_compra': 'Mês'}, inplace=True)


plot_sazonalidade_vendas(vendas_por_mes)


criar_grafico_top_10_clientes(clientes_lucrativos)
