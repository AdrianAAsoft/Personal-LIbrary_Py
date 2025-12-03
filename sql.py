#Importar biblioteca de Slq
import sqlite3

def conexionBd():
    return sqlite3.connect("BibliotecaP.db")

#iniciador de tabla
def tabla():
    conn = conexionBd()
    cursor = conn.cursor()
    cursor.execute(""" Create Table if not exists Libro(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   Titulo TEXT NOT NULL, 
                   Autor TEXT NOT NULL,
                   Genero TEXT NOT NULL,
                   Ano INTEGER NOT NULL,
                   Estado_Lectura INTEGER NOT NULL    
                   )""")
    #Tabla con un id, titulo, autor, genero, año y estado el cual es entero, 1 para leido y 0 para no leido 
    conn.commit()
    conn.close()

#Funciones para agregar, actualizar, eliminar, ver listado de libros y buscar libros 

def AddLibro(Titulo,Autor,Genero,Ano,Estado):
    conn=conexionBd()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Libro (Titulo, Autor, Genero, Ano, Estado_Lectura) VALUES (?,?,?,?,?)",
                (Titulo,Autor,Genero,Ano,Estado))
    
    conn.commit()
    conn.close()
    print("Libro Agregado.")

def UpdateLibro(idBook, Titulo, Autor, Genero, Ano, Estado):
    conn = conexionBd()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE Libro
            SET Titulo = ?, Autor = ?, Genero = ?, Ano = ?, Estado_Lectura = ?
            WHERE id = ?
        """, (Titulo,Autor,Genero,Ano,Estado,idBook))
    
    conn.commit()
    conn.close()
    print("Se actualizo el libro exitosamente.")

def DeleteLibro(idBook):
    conn = conexionBd()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Libro WHERE id = ?", (idBook,))

    conn.commit()
    conn.close()
    print("Se ha eliminado un libro de la base de datos.")

def ListLibros():
    conn = conexionBd()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Libro")
    listado = cursor.fetchall()

    conn.close()
    return listado

def GetLibro(campo,idBook):
    conn = conexionBd()
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM Libro WHERE {campo} Like ?", (f"%{idBook}%",))
    libro = cursor.fetchall()

    conn.close()
    return libro