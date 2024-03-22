import pandas as pd
import sqlite3
import datetime
# import matplotlib.pyplot as plt
# import seaborn as sns

# Connect to SQLite DB
conn = sqlite3.connect('vendas.db')

# Loading data from the database
df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)

# Calculating the total sale value and assigning it to the 'valor_total' column
df_sqlite['valor_total'] = df_sqlite['preco'] * df_sqlite['quantidade']

print("\n" * 1)  # Adding spacing between DataFrames
# Printing table name before printing SQLite DataFrame
print("Tabela SQLite: vendas")
print("--------------------------------------------------------------------------------")
print(df_sqlite.head())
print("\n" * 2)  # Adding spacing between DataFrames

# Closing connection with DB
conn.close()

# Loading data from CSV file
df_csv = pd.read_csv('vendas_db.csv')

# Creating an ID field for the CSV DataFrame
df_csv['id'] = df_csv.index + 1

cols = list(df_csv.columns)
cols = ['id'] + [col for col in cols if col != 'id']
df_csv = df_csv[cols]

# Calculating total sales value for CSV DataFrame
df_csv['valor_total'] = df_csv['preco'] * df_csv['quantidade']

# Printing table name before printing CSV DataFrame
print("Tabela CSV: vendas_df")
print("--------------------------------------------------------------------------------")
print(df_csv.head())
print("\n" * 2)  # Adding spacing between DataFrames

# Combining the DataFrames using the concat function, concatenating them vertically
df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)

# Printing the combined DataFrame
print("Tabela combinada:")
print("--------------------------------------------------------------------------------")
print(df_combined)
print("\n" * 2)  # Adding spacing between DataFrames

# Converting the 'data_compra' column to the datetime type
df_combined['data_compra'] = pd.to_datetime(df_combined['data_compra'])

# Extracting the month from the purchase date
df_combined['mes_compra'] = df_combined['data_compra'].dt.month

# Calculating the total sales value per customer
clientes_lucrativos = df_combined.groupby('cliente_nome')['valor_total'].sum().reset_index()

# Sort customers based on total sales value (highest to lowest)
clientes_lucrativos = clientes_lucrativos.sort_values(by='valor_total', ascending=False)

# Printing the most profitable customers
print("Clientes mais lucrativos:")
print("------------------------------")
print(clientes_lucrativos.head())
print("\n" * 2)  # Adding spacing between DataFrames

# Calculating total sales per month to analyze sales seasonality
vendas_por_mes = df_combined.groupby('mes_compra')['valor_total'].sum().reset_index()

# Printing sales seasonality by month
print("Sazonalidade de vendas por mês:")
print("----------------------------------")
print(vendas_por_mes)