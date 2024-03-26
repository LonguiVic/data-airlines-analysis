import sqlite3
import random

# Conectar ao banco de dados
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Criar a tabela vendas, se ainda não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_nome TEXT,
    cliente_sobrenome TEXT,
    cliente_email TEXT,
    data_compra TEXT,
    produto TEXT,
    preco REAL,
    quantidade INTEGER
)
''')

# Dados dos clientes
clientes = [
    ('Amanda', 'Rodrigues', 'amanda.rodrigues@example.com', '2024-03-01', 'Produto A', 10.99, 5),
    ('Elvis', 'da Silva', 'elvis.dasilva@example.com', '2024-03-02', 'Produto B', 15.99, 3),
    ('Marcos', 'Pereira', 'marcos.pereira@example.com', '2024-03-03', 'Produto C', 20.49, 8),
    ('Elvis', 'da Silva', 'elvis.dasilva@example.com', '2024-03-02', 'Produto B', 15.99, 3),
    ('Marcos', 'Pereira', 'marcos.pereira@example.com', '2024-03-03', 'Produto C', 20.49, 8),
    ('Ana', 'Santos', 'ana.santos@example.com', '2024-03-03', 'Produto D', 20.49, 8),
    ('Rafael', 'Duarte', 'rafael.duarte@example.com', '2024-03-04', 'Produto E', 30.99, 6),
    ('Diego', 'Coelho', 'diego.coelho@example.com', '2024-03-05', 'Produto F', 25.49, 10),
    ('Juliana', 'Silva', 'juliana.silva@example.com', '2024-09-18', 'Produto B', 30.49, 7),
    ('Lucas', 'Martins', 'lucas.martins@example.com', '2024-04-27', 'Produto D', 22.99, 9),
    ('Fernanda', 'Almeida', 'fernanda.almeida@example.com', '2024-08-03', 'Produto A', 18.75, 5),
    ('Rafael', 'Santos', 'rafael.santos@example.com', '2024-06-14', 'Produto C', 35.00, 3),
    ('Carolina', 'Ferreira', 'carolina.ferreira@example.com', '2024-03-01', 'Produto F', 27.49, 6),
    ('Pedro', 'Oliveira', 'pedro.oliveira@example.com', '2024-10-22', 'Produto E', 25.99, 8),
    ('Vanessa', 'Pereira', 'vanessa.pereira@example.com', '2024-01-05', 'Produto A', 19.99, 4),
    ('Gabriel', 'Silva', 'gabriel.silva@example.com', '2024-07-30', 'Produto B', 32.25, 10),
    ('Mariana', 'Gomes', 'mariana.gomes@example.com', '2024-11-19', 'Produto D', 28.50, 7),
    ('Diego', 'Rodrigues', 'diego.rodrigues@example.com', '2024-05-12', 'Produto C', 24.00, 2),
    ('Patricia', 'Santana', 'patricia.santana@example.com', '2024-02-28', 'Produto F', 36.49, 5),
    ('Gustavo', 'Lima', 'gustavo.lima@example.com', '2024-12-15', 'Produto E', 21.75, 6),
    ('Ana', 'Martinez', 'ana.martinez@example.com', '2024-09-10', 'Produto B', 33.99, 8),
    ('Luciana', 'Fernandes', 'luciana.fernandes@example.com', '2024-07-08', 'Produto D', 29.00, 4),
    ('Thiago', 'Gonçalves', 'thiago.goncalves@example.com', '2024-04-03', 'Produto C', 15.49, 3),
    ('Camila', 'Alves', 'camila.alves@example.com', '2024-03-25', 'Produto F', 38.25, 9),
    ('André', 'Correia', 'andre.correia@example.com', '2024-11-01', 'Produto E', 23.99, 7),
    ('Renata', 'Nunes', 'renata.nunes@example.com', '2024-08-17', 'Produto A', 27.50, 5),
    ('José', 'Carvalho', 'jose.carvalho@example.com', '2024-06-02', 'Produto B', 20.99, 6),
    ('Marcela', 'Oliveira', 'marcela.oliveira@example.com', '2024-12-09', 'Produto D', 32.00, 8),
    ('Bruno', 'Sousa', 'bruno.sousa@example.com', '2024-10-15', 'Produto C', 18.75, 4),
    ('Tatiane', 'Ribeiro', 'tatiane.ribeiro@example.com', '2024-01-20', 'Produto F', 25.49, 3),
    ('Fernando', 'Silveira', 'fernando.silveira@example.com', '2024-05-30', 'Produto E', 22.25, 2),
    ('Aline', 'Gomes', 'aline.gomes@example.com', '2024-07-20', 'Produto B', 28.99, 7),
    ('Roberto', 'Pinto', 'roberto.pinto@example.com', '2024-02-15', 'Produto A', 31.50, 9),
    ('Carla', 'Mendes', 'carla.mendes@example.com', '2024-09-02', 'Produto D', 17.99, 5),
    ('Vitor', 'Rocha', 'vitor.rocha@example.com', '2024-03-10', 'Produto C', 29.00, 6)
]

# Inserir dados na tabela
for cliente in clientes:
    cursor.execute('''
    INSERT INTO vendas (cliente_nome, cliente_sobrenome, cliente_email, data_compra, produto, preco, quantidade)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', cliente)

# Confirmar as alterações
conn.commit()
conn.close()

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# 1. Adicionar o campo "estado" à tabela existente
cursor.execute('''ALTER TABLE vendas ADD COLUMN estado TEXT''')

# 2. Gerar estados aleatórios para cada cliente
estados = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG',
    'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
] # Lista de estados brasileiros, por exemplo
cursor.execute("SELECT id FROM vendas")
clientes = cursor.fetchall()

# 3. Atualizar a tabela existente com os estados aleatórios
for cliente in clientes:
    estado_aleatorio = random.choice(estados)
    cursor.execute("UPDATE vendas SET estado = ? WHERE id = ?", (estado_aleatorio, cliente[0]))

# Confirmar a transação
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()