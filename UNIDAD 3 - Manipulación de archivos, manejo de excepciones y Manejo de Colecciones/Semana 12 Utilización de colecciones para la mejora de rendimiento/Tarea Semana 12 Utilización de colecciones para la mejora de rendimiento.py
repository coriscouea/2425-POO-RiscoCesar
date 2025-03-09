import json

class Libro:
    """
    Clase que representa un libro en la biblioteca.
    Attributes:
        isbn (str): Identificador único del libro.
        datos (tuple): Tupla inmutable que contiene (título, autor).
        categoria (str): Categoría del libro.
        prestado (bool): Indica si el libro está prestado o disponible.
    """
    def __init__(self, isbn, titulo, autor, categoria, prestado=False):
        # Usando tupla para título y autor como se solicitó
        self.isbn = isbn
        self.datos = (titulo, autor)  # Tupla para título y autor (inmutables)
        self.categoria = categoria
        self.prestado = prestado

    def to_dict(self):
        """
        Convierte el objeto Libro a un diccionario para su serialización.
        Returns:
            dict: Diccionario con los atributos del libro.
        """
        return {
            "isbn": self.isbn,
            "titulo": self.datos[0],  # Acceder al título desde la tupla
            "autor": self.datos[1],   # Acceder al autor desde la tupla
            "categoria": self.categoria,
            "prestado": self.prestado
        }

    def __str__(self):
        """Define cómo se representa el libro como una cadena de texto."""
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Libro: {self.datos[0]} por {self.datos[1]} - {estado}"


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca.
    Attributes:
        archivo_json (str): Ruta del archivo para almacenar usuarios.
        id_usuario (str): Identificador único del usuario.
        nombre (str): Nombre del usuario.
        libros_prestados (list): Lista de ISBNs de libros prestados al usuario.
    """
    archivo_json = 'usuarios.json'

    def __init__(self, id_usuario, nombre, libros_prestados=None):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.libros_prestados = libros_prestados if libros_prestados else []

    def to_dict(self):
        """
        Convierte el objeto Usuario a un diccionario para su serialización.
        Returns:
            dict: Diccionario con los atributos del usuario.
        """
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "libros_prestados": self.libros_prestados
        }


# Funciones independientes para manejar usuarios
def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON y devuelve un diccionario."""
    try:
        with open(Usuario.archivo_json, 'r') as archivo:
            datos_usuarios = json.load(archivo)
            return {id_usuario: Usuario(**datos) for id_usuario, datos in datos_usuarios.items()}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON."""
    with open(Usuario.archivo_json, 'w') as archivo:
        json.dump({id_usuario: usuario.to_dict() for id_usuario, usuario in usuarios.items()}, archivo, indent=4)


def mostrar_usuarios():
    """Muestra la lista de usuarios registrados."""
    usuarios = cargar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios.values():
        print(f"ID: {usuario.id_usuario}, Nombre: {usuario.nombre}, Libros prestados: {usuario.libros_prestados}")


def eliminar_usuario(id_usuario):
    """Elimina un usuario por su ID si existe."""
    usuarios = cargar_usuarios()
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        guardar_usuarios(usuarios)
        print(f"Usuario con ID {id_usuario} eliminado.")
    else:
        print("El usuario no existe.")


class Biblioteca:
    def __init__(self, archivo_json='biblioteca.json'):
        self.archivo_json = archivo_json
        self.libros = self.cargar_libros()
        self.usuarios_registrados = set()  # Conjunto para IDs de usuario únicos

    def cargar_libros(self):
        """Carga los libros desde el archivo JSON."""
        try:
            with open(self.archivo_json, 'r') as archivo:
                datos_libros = json.load(archivo)
                return {isbn: Libro(**datos) for isbn, datos in datos_libros.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_libros(self):
        """Guarda los libros en el archivo JSON."""
        with open(self.archivo_json, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def añadir_libro(self, libro):
        """Añade un libro a la biblioteca."""
        self.libros[libro.isbn] = libro
        self.guardar_libros()
        print(f"El libro '{libro}' se guardó correctamente.")  # Aquí se usa __str__

    def quitar_libros(self, isbn):
        """Elimina un libro de la biblioteca por su ISBN."""
        if isbn in self.libros:
            libro = self.libros[isbn]
            del self.libros[isbn]
            self.guardar_libros()
            print(f"Libro '{libro}' eliminado de la biblioteca.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}")

    def prestar_libro(self, isbn, id_usuario):
        """Presta un libro a un usuario."""
        usuarios = cargar_usuarios()  # Usar la función independiente

        if id_usuario not in usuarios:
            print("El usuario no está registrado.")
            return

        usuario = usuarios[id_usuario]

        if len(usuario.libros_prestados) >= 3:
            print("El usuario ya tiene el máximo de libros prestados (3).")
            return

        libro = self.libros.get(isbn)
        if libro and not libro.prestado:
            libro.prestado = True
            usuario.libros_prestados.append(isbn)
            self.guardar_libros()
            guardar_usuarios(usuarios)
            print(f"Libro '{libro}' prestado a {usuario.nombre} con éxito.")
        else:
            print("Libro no disponible para préstamo.")

    def devolver_libro(self, isbn, id_usuario):
        """Devuelve un libro prestado por un usuario."""
        usuarios = cargar_usuarios()  # Usar la función independiente

        if id_usuario not in usuarios:
            print("El usuario no está registrado.")
            return

        usuario = usuarios[id_usuario]

        if isbn not in usuario.libros_prestados:
            print("El usuario no tiene este libro prestado.")
            return

        libro = self.libros.get(isbn)
        if libro and libro.prestado:
            libro.prestado = False
            usuario.libros_prestados.remove(isbn)
            self.guardar_libros()
            guardar_usuarios(usuarios)
            print(f"Libro '{libro}' devuelto por {usuario.nombre} con éxito.")
        else:
            print("Error en la devolución del libro.")

    def mostrar_libros(self):
        """Muestra todos los libros en la biblioteca."""
        if not self.libros:
            print("No hay libros en la biblioteca.")
            return

        for libro in self.libros.values():
            print(libro)  # Aquí se usa __str__

    def buscar_por_titulo(self, titulo):
        """Busca libros por título."""
        resultados = [libro for libro in self.libros.values() if titulo.lower() in libro.datos[0].lower()]
        if resultados:
            print(f"Resultados de búsqueda para '{titulo}':")
            for libro in resultados:
                print(libro)  # Aquí se usa __str__
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")

    def buscar_por_autor(self, autor):
        """Busca libros por autor."""
        resultados = [libro for libro in self.libros.values() if autor.lower() in libro.datos[1].lower()]
        if resultados:
            print(f"Resultados de búsqueda para '{autor}':")
            for libro in resultados:
                print(libro)  # Aquí se usa __str__
        else:
            print(f"No se encontraron libros del autor '{autor}'.")

    def buscar_por_categoria(self, categoria):
        """Busca libros por categoría."""
        resultados = [libro for libro in self.libros.values() if categoria.lower() in libro.categoria.lower()]
        if resultados:
            print(f"Resultados de búsqueda para '{categoria}':")
            for libro in resultados:
                print(libro)  # Aquí se usa __str__
        else:
            print(f"No se encontraron libros en la categoría '{categoria}'.")

    def listar_libros_prestados(self, id_usuario):
        """Lista los libros prestados a un usuario."""
        usuarios = cargar_usuarios()  # Usar la función independiente

        if id_usuario not in usuarios:
            print("El usuario no está registrado.")
            return

        usuario = usuarios[id_usuario]
        if not usuario.libros_prestados:
            print(f"El usuario {usuario.nombre} no tiene libros prestados.")
            return

        print(f"Libros prestados a {usuario.nombre}:")
        for isbn in usuario.libros_prestados:
            libro = self.libros.get(isbn)
            if libro:
                print(libro)  # Aquí se usa __str__


def menu():
    biblioteca = Biblioteca()

    while True:
        try:
            print("\n === Sistema de Gestión de Biblioteca Digital ===")
            print("1. Añadir Libro")
            print("2. Mostrar Libros")
            print("3. Prestar Libro")
            print("4. Devolver Libro")
            print("5. Quitar Libro")
            print("6. Registrar Usuario")
            print("7. Mostrar Usuarios")
            print("8. Eliminar Usuario")
            print("9. Buscar Libro por Título")
            print("10. Buscar Libro por Autor")
            print("11. Buscar Libro por Categoría")
            print("12. Listar Libros Prestados de un Usuario")
            print("13. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                isbn = input("ISBN: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                categoria = input("Categoría: ")
                libro = Libro(isbn, titulo, autor, categoria)
                biblioteca.añadir_libro(libro)
            elif opcion == '2':
                biblioteca.mostrar_libros()
            elif opcion == '3':
                isbn = input("ISBN del libro a prestar: ")
                id_usuario = input("ID del usuario que lo solicita: ")
                biblioteca.prestar_libro(isbn, id_usuario)
            elif opcion == '4':
                isbn = input("ISBN del libro a devolver: ")
                id_usuario = input("ID del usuario que devuelve el libro: ")
                biblioteca.devolver_libro(isbn, id_usuario)
            elif opcion == '5':
                isbn = input("ISBN del libro a quitar: ")
                biblioteca.quitar_libros(isbn)
            elif opcion == '6':
                nombre = input("Nombre del usuario: ")
                id_usuario = input("ID Usuario: ")
                usuarios = cargar_usuarios()
                usuarios[id_usuario] = Usuario(id_usuario, nombre)
                guardar_usuarios(usuarios)
                print(f"Usuario {nombre} registrado con éxito.")
            elif opcion == '7':
                mostrar_usuarios()
            elif opcion == '8':
                id_usuario = input("ID del usuario a eliminar: ")
                eliminar_usuario(id_usuario)
            elif opcion == '9':
                titulo = input("Título a buscar: ")
                biblioteca.buscar_por_titulo(titulo)
            elif opcion == '10':
                autor = input("Autor a buscar: ")
                biblioteca.buscar_por_autor(autor)
            elif opcion == '11':
                categoria = input("Categoría a buscar: ")
                biblioteca.buscar_por_categoria(categoria)
            elif opcion == '12':
                id_usuario = input("ID del usuario: ")
                biblioteca.listar_libros_prestados(id_usuario)
            elif opcion == '13':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Saliendo del programa...")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == "__main__":
    menu()