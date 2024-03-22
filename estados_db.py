import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Create the estados table if it doesn't exist
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS estados (
#     estado_id INTEGER PRIMARY KEY,
#     nome TEXT NOT NULL,
#     sigla TEXT NOT NULL
# )
# ''')

# Insert data for the estados table if it's empty
cursor.execute('''
INSERT INTO estados (estado) 
VALUES ('Alagoas'),
       ('Amapa'),
       ('Amazonas'),
       ('Bahia'),
       ('Ceara'),
       ('Distrito Federal'),
       ('Espirito Santo'),
       ('Goias'),
       ('Maranhao'),
       ('Mato Grosso'),
       ('Mato Grosso do Sul'),
       ('Minas Gerais'),
       ('Para'),
       ('Paraiba'),
       ('Parana'),
       ('Pernambuco'),
       ('Rio de Janeiro'),
       ('Rio Grande do Norte'),
       ('Rio Grande do Sul'),
       ('Rondonia'),
       ('Roraima'),
       ('Santa Catarina'),
       ('Sao Paulo'),
       ('Sergipe'),
       ('Tocantins')
''')


# Commit the changes
conn.commit()

# Close the connection with DB
conn.close()
