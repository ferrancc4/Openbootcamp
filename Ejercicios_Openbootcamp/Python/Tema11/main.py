import getpass
import sqlite3

def main():
    crear_usuario(3, "Pepe", "superclave")
def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Loging correcto")
    else:
        print("Loging incorrecto")

def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = '''INSERT INTO users(id, username, password) VALUES(?, ?, ?)'''

    rows = cursor.execute(query, (identificador, usuario, clave))
    print(type(rows))

    conn.commit()
    cursor.close()
    conn.close()
def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)
    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

    if data == None:
        return False

    return True

if __name__ == '__main__':
    main()
