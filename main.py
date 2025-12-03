#Importar libreria de sql 
from ast import Try
import sql 

#Crear la tabla 
sql.tabla()

#Menu principal 

def menu():
    while True:
        print("""======= BIBLIOTECA =======
        1. Agregar nuevo libro
        2. Actualizar información de un libro
        3. Eliminar libro existente
        4. Ver listado de libros
        5. Buscar libros
        6. Salir""")
        
        try:
            opcion = int(input("Seleccione una opcion 1-6: "))
        except ValueError:
            print("Ingrese un dato numerico.")

        #Opciones Agregar un libre
        if opcion == 1:
            t = input("Titulo: ")
            au = input("Autor: ")
            g = input("Genero: ")
            an = input("Año del libro: ") 
            e = input("Estado (Leido / No leido): ")
            sql.AddLibro(t, au, g,an, e)

        #Actualizar un libro
        elif opcion == 2:
            listar = sql.ListLibros()

            if not listar:
                    print("\n❌ No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for libro in listar:
                        id_, titulo, autor, genero, ano, estado = libro
                        print(f"""
                ID: {id_}
                Título: {titulo}
                Autor: {autor}
                Genero: {genero}
                Año: {ano}
                Estado: {estado}
                ------------------------------
                """)
                    
            try:
                id = int(input("Ingrese el ID del libro a actualizar: "))
            except:
                print("ID invalido.")
                continue

            t = input("Nuevo titulo: ")
            au = input("Nuevo autor: ")
            g = input("Nuevo genero: ")
            an = input("Nuevo año del libro: ") 
            es = input("Nuevo estado (Leido/No leido): ")

            sql.UpdateLibro(id, t, au, g,an, es)

        #Eliminar un libro
        elif opcion == 3:
            listar = sql.ListLibros()

            if not listar:
                    print("\n❌ No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for libro in listar:
                        id_, titulo, autor, genero, ano, estado = libro
                        print(f"""
                ID: {id_}
                Título: {titulo}
                Autor: {autor}
                Genero: {genero}
                Año: {ano}
                Estado: {estado}
                ------------------------------
                """)
                        
            try:
                id = int(input("Ingrese el ID del libro a eliminar: "))
            except:
                print("ID invalido.")
                continue

            sql.DeleteLibro(id)

        #Listado de libros
        elif opcion == 4:
            listar = sql.ListLibros()
            if not listar:
                    print("\n❌ No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for libro in listar:
                        id_, titulo, autor, genero, ano, estado = libro
                        print(f"""
                ID: {id_}
                Título: {titulo}
                Autor: {autor}
                Genero: {genero}
                Año: {ano}
                Estado: {estado}
                ------------------------------
                """)
        #Busqueda de libros    
        elif opcion == 5:
            print("\nBuscar por:")
            print("1. Título")
            print("2. Autor")
            print("3. Género")

            tipo = input("Seleccione opcion: ")

            if tipo == "1":
                valor = input("Ingrese título: ")
                resultados = sql.GetLibro("titulo", valor)

            elif tipo == "2":
                valor = input("Ingrese autor: ")
                resultados = sql.GetLibro("autor", valor)

            elif tipo == "3":
                valor = input("Ingrese género: ")
                resultados = sql.GetLibro("genero", valor)

            else:
                print("Opción inválida.")
                continue

            if not resultados:
                    print("\n❌ No hay resultados.\n")
            else:
                print("\n===== LISTADO DE LIBROS =====")
                for libro in resultados:
                        id_, titulo, autor, genero, ano, estado = libro
                        print(f"""
                ID: {id_}
                Título: {titulo}
                Autor: {autor}
                Genero: {genero}
                Año: {ano}
                Estado: {estado}
                ------------------------------
                """)
                        
        elif opcion == 6:
            print("Hasta luego")
            break

        else:
            print("La opcion no existe, intente nuevamente.")

if __name__ == "__main__":
    menu()