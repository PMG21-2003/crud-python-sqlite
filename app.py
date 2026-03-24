import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    idade INTEGER,
    email TEXT
)
''')

def cadastrar():
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("Email: ")

    cursor.execute("INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)",
                   (nome, idade, email))
    conn.commit()
    print("Usuário cadastrado!")

def listar():
    cursor.execute("SELECT * FROM usuarios")
    for usuario in cursor.fetchall():
        print(usuario)

while True:
    print("\n1 - Cadastrar\n2 - Listar\n3 - Sair")
    op = input("Escolha: ")

    if op == "1":
        cadastrar()
    elif op == "2":
        listar()
    else:
        break