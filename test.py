import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('vendas.db')
df_sqlite = pd.read_sql_query("SELECT * FROM vendas", conn)

df_csv = pd.read_csv('vendas_csv.csv')

print("Primeiras linhas dos dados do banco de dados SQLite:")
print(df_sqlite.head())

print("\nPrimeiras linhas dos dados do arquivo CSV:")
print(df_csv.head())

print("\nEstatísticas descritivas dos dados do banco de dados SQLite:")
print(df_sqlite.describe())

print("\nEstatísticas descritivas dos dados do arquivo CSV:")
print(df_csv.describe())

plt.figure(figsize=(10, 6))
plt.hist(df_sqlite['preco'], bins=20, color='skyblue')
plt.title('Histograma de Preços dos Produtos (SQLite)')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(df_csv['preco'], df_csv['quantidade'], color='orange')
plt.title('Preço vs. Quantidade (CSV)')
plt.xlabel('Preço')
plt.ylabel('Quantidade')
plt.grid(True)
plt.show()
