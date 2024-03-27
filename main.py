import calendar
import sqlite3

import pandas as pd

from graphs.sazonalidade_vendas import plot_sazonalidade_vendas
from graphs.top_10_clientes import criar_grafico_top_10_clientes
from graphs.total_vendas_estado import plot_vendas_por_estado
from graphs.total_vendas_produto import gerar_grafico_vendas_por_produto

conn = sqlite3.connect('vendas.db')

# Lendo dados do SQLite
df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)
df_sqlite['valor_total'] = df_sqlite['preco'] * df_sqlite['quantidade']

# Lendo dados do CSV
df_csv = pd.read_csv('vendas_db.csv')

# Verificando se a coluna 'id' está presente no DataFrame df_csv
if 'id' in df_csv.columns:
    # Verificando o último ID existente no SQLite
    ultimo_id_sqlite = df_sqlite['id'].max()

    # Ajustando os IDs do dataframe CSV para continuar a partir do último ID existente
    df_csv['id'] = df_csv.index + 1 + ultimo_id_sqlite
    df_csv['valor_total'] = df_csv['preco'] * df_csv['quantidade']

else:
    # Se a coluna 'id' não estiver presente, cria com valores contínuos a partir do último ID existente no SQLite
    ultimo_id_sqlite = df_sqlite['id'].max()
    df_csv['id'] = pd.RangeIndex(start=ultimo_id_sqlite + 1, stop=ultimo_id_sqlite + 1 + len(df_csv))
    df_csv['valor_total'] = df_csv['preco'] * df_csv['quantidade']

# Concatenando os dataframes
df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)
df_combined['data_compra'] = pd.to_datetime(df_combined['data_compra'])
df_combined['mes_compra'] = df_combined['data_compra'].dt.month

# Exportando para o SQLite
df_combined.to_sql('df_combined', conn, if_exists='replace', index=False)


conn.close()


# Analise de clientes
clientes_lucrativos = df_combined.groupby('cliente_nome')['valor_total'].sum().reset_index()
clientes_lucrativos = clientes_lucrativos.sort_values(by='valor_total', ascending=False)
clientes_lucrativos.reset_index(inplace=True)
clientes_lucrativos.rename(columns={'index': 'ID'}, inplace=True)

# -------------------------------- Analise de vendas ----------------------------------------

# Sazonalidade de vendas por mês
vendas_por_mes = df_combined.groupby('mes_compra')['valor_total'].sum().reset_index()
vendas_por_mes.rename(columns={'mes_compra': 'Mês'}, inplace=True)

# Total de vendas por estado
vendas_por_estado = df_combined.groupby('estado')['valor_total'].sum().reset_index()
vendas_por_estado = vendas_por_estado.rename(columns={'valor_total': 'Total de vendas'})

# Total de vendas por produto
vendas_por_produto = df_combined.groupby('produto')['valor_total'].sum().reset_index()



plot_sazonalidade_vendas(vendas_por_mes)

criar_grafico_top_10_clientes(clientes_lucrativos)

plot_vendas_por_estado(vendas_por_estado)

gerar_grafico_vendas_por_produto (df_combined)
