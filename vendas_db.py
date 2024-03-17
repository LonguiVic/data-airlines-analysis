import sqlite3

conn = sqlite3.connect('vendas.db')

cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE vendas (
#     id INTEGER PRIMARY KEY,
#     cliente_nome TEXT,
#     cliente_sobrenome TEXT,
#     data_compra TEXT,
#     produto TEXT,
#     preco REAL,
#     quantidade INTEGER
# )
# ''')

cursor.execute('''
INSERT INTO vendas (cliente_nome, cliente_sobrenome, data_compra, produto, preco, quantidade)
VALUES
    ('Amanda', 'Rodrigues', '2024-03-01', 'Produto A', 10.99, 5),
    ('Elvis', 'da Silva', '2024-03-02', 'Produto B', 15.99, 3),
    ('Marcos', 'Pereira', '2024-03-03', 'Produto C', 20.49, 8),
    ('Ana', 'Santos', '2024-03-03', 'Produto D', 20.49, 8),
    ('Rafael', 'Duarte', '2024-03-04', 'Produto E', 30.99, 6),
    ('Diego', 'Coelho', '2024-03-05', 'Produto F', 25.49, 10),
    ('Juliana', 'Silva', '2024-09-18', 'Produto B', 30.49, 7),
    ('Lucas', 'Martins', '2024-04-27', 'Produto D', 22.99, 9),
    ('Fernanda', 'Almeida', '2024-08-03', 'Produto A', 18.75, 5),
    ('Rafael', 'Santos', '2024-06-14', 'Produto C', 35.00, 3),
    ('Carolina', 'Ferreira', '2024-03-01', 'Produto F', 27.49, 6),
    ('Pedro', 'Oliveira', '2024-10-22', 'Produto E', 25.99, 8),
    ('Vanessa', 'Pereira', '2024-01-05', 'Produto A', 19.99, 4),
    ('Gabriel', 'Silva', '2024-07-30', 'Produto B', 32.25, 10),
    ('Mariana', 'Gomes', '2024-11-19', 'Produto D', 28.50, 7),
    ('Diego', 'Rodrigues', '2024-05-12', 'Produto C', 24.00, 2),
    ('Patricia', 'Santana', '2024-02-28', 'Produto F', 36.49, 5),
    ('Gustavo', 'Lima', '2024-12-15', 'Produto E', 21.75, 6),
    ('Ana', 'Martinez', '2024-09-10', 'Produto B', 33.99, 8),
    ('Luciana', 'Fernandes', '2024-07-08', 'Produto D', 29.00, 4),
    ('Thiago', 'Gonçalves', '2024-04-03', 'Produto C', 15.49, 3),
    ('Camila', 'Alves', '2024-03-25', 'Produto F', 38.25, 9),
    ('André', 'Correia', '2024-11-01', 'Produto E', 23.99, 7),
    ('Renata', 'Nunes', '2024-08-17', 'Produto A', 27.50, 5),
    ('José', 'Carvalho', '2024-06-02', 'Produto B', 20.99, 6),
    ('Marcela', 'Oliveira', '2024-12-09', 'Produto D', 32.00, 8),
    ('Bruno', 'Sousa', '2024-10-15', 'Produto C', 18.75, 4),
    ('Tatiane', 'Ribeiro', '2024-01-20', 'Produto F', 25.49, 3),
    ('Fernando', 'Silveira', '2024-05-30', 'Produto E', 22.25, 2),
    ('Aline', 'Gomes', '2024-07-20', 'Produto B', 28.99, 7),
    ('Roberto', 'Pinto', '2024-02-15', 'Produto A', 31.50, 9),
    ('Carla', 'Mendes', '2024-09-02', 'Produto D', 17.99, 5),
    ('Vitor', 'Rocha', '2024-03-10', 'Produto C', 29.00, 6),
    ('Sandra', 'Martins', '2024-06-18', 'Produto F', 23.49, 4),
    ('Felipe', 'Santos', '2024-11-24', 'Produto E', 40.75, 8),
    ('Laura', 'Ferreira', '2024-10-06', 'Produto A', 26.99, 7),
    ('Paulo', 'Oliveira', '2024-04-14', 'Produto B', 19.50, 3),
    ('Mariana', 'Costa', '2024-08-29', 'Produto D', 34.00, 6),
    ('Renan', 'Gonçalves', '2024-01-08', 'Produto C', 24.75, 5),
    ('Natália', 'Almeida', '2024-07-05', 'Produto F', 36.99, 8),
    ('Gustavo', 'Fernandes', '2024-12-20', 'Produto E', 28.25, 7),
    ('Fernanda', 'Lima', '2024-05-08', 'Produto A', 22.49, 4),
    ('Rodrigo', 'Ribeiro', '2024-03-17', 'Produto B', 30.00, 9),
    ('Ana', 'Santos', '2024-09-24', 'Produto D', 16.75, 3),
    ('Diego', 'Machado', '2024-11-13', 'Produto C', 29.25, 7),
    ('Carolina', 'Silva', '2024-06-28', 'Produto F', 33.50, 5),
    ('Rafael', 'Nogueira', '2024-01-02', 'Produto E', 27.99, 6),
    ('Patricia', 'Martinez', '2024-08-12', 'Produto A', 21.50, 2),
    ('Lucas', 'Correia', '2024-12-29', 'Produto B', 38.25, 7),
    ('Marcela', 'Ferreira', '2024-07-16', 'Produto D', 25.99, 4)
    ''')

conn.commit()

conn.close()