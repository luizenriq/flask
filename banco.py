import sqlite3

# Função para criar a tabela no banco de dados
def init_sqlite_db():
    conn = sqlite3.connect('uniformes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS uniformes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            modelo TEXT NOT NULL,
            cor TEXT NOT NULL,
            tamanho TEXT NOT NULL,
            vestuario TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def select():
    conn = sqlite3.connect('uniformes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM uniformes")
    uniformes = cursor.fetchall()
    conn.close()
    return uniformes

# Inicializa o banco de dados
#init_sqlite_db()