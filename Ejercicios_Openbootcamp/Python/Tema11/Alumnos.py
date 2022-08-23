import sqlite3
def main():
    # Añadimos 8 alumnos
    nuevo_alumno("Juan", "Perico")
    nuevo_alumno("Sergio", "Gonzales")
    nuevo_alumno("Pere", "Curto")
    nuevo_alumno("Alba", "Garvia")
    nuevo_alumno("Maria", "Mato")
    nuevo_alumno("Luis", "Garcia")
    nuevo_alumno("Laia", "Perez")
    nuevo_alumno("Marcos", "Perico")
    # Consulta por nombre
    datos_alumno("Maria")

def nuevo_alumno(nombre, apellido):
    conn = sqlite3.connect('lista_alumnos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Alumnos")
    taula = cursor.fetchall()
    id = len(taula) + 1

    query = '''INSERT INTO Alumnos(id, nombre, apellido) VALUES (?, ?, ?)'''
    cursor.execute(query, (id, nombre, apellido))

    conn.commit()
    cursor.close()
    conn.close()

def datos_alumno(nombre):
    conn = sqlite3.connect('lista_alumnos.db')
    cursor = conn.cursor()

    query = f'SELECT * FROM Alumnos WHERE nombre="{nombre}";'
    cursor.execute(query)
    result = cursor.fetchone()
    print(f'El/La alumno/a de nombre {result[1]} y apellido {result[2]} es el número {result[0]} en la lista')

if __name__ == '__main__':
    main()