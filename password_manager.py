import sqlite3
import os

MASTER_PASSWORD = "123456"

conn = sqlite3.connect('.\dados.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL

);
''')
os.system('cls' if os.name == 'nt' else 'clear')
def menu():
    print("******************************")
    print("* 1 : Inserir nova senha     *")
    print("* 2 : Listar serviços salvos *")
    print("* 3 : Ver uma senha Salva    *")
    print("* 0 : Sair                   *")
    print("******************************")

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (use a opção 2 para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)   
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['1', '2', '3', '0']:
        print("Opção Inválida!")
        continue

    if op == '1':
        service = input('Qual o nome do serviço? ')
        username = input('Qual o nome de usuário? ')
        password = input('Qual a senha? ')
        insert_password(service, username, password)

    if op == '2':
        show_services()

    if op == '3':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_password(service)

    if op == '0':
        print("\n Até Logo!")
        break

print ('Finalizado com Sucesso!')

conn.close()

