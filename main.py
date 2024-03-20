import pandas as pd
import sqlite3
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
print("Tabela CSV: vendas_db")
print("--------------------------------------------------------------------------------")
print(df_csv.head())
print("\n" * 2)  # Adding spacing between DataFrames

# Combining the DataFrames using the concat function, concatenating them vertically
df_combined = pd.concat([df_sqlite, df_csv], ignore_index=True)

# Printing the combined DataFrame
print("Tabela combinada:")
print("--------------------------------------------------------------------------------")
print(df_combined)