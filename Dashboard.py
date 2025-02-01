import os

def mostrar_codigo(ruta_script):
    """ Muestra el contenido de un archivo de script en la consola.
        Parámetros:
        - ruta_script (str): Ruta relativa o absoluta del archivo de script que se desea mostrar.
        Excepciones:
        - FileNotFoundError: Si el archivo no se encuentra en la ruta especificada.
        - Exception: Si ocurre cualquier otro error al intentar leer el archivo."""

    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abre el archivo en modo lectura y muestra su contenido
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    """Muestra un menú interactivo que permite al usuario seleccionar un script para ver su código.
    El menú muestra una lista de scripts predefinidos, y el usuario puede elegir uno para ver su contenido.
    La función utiliza un bucle infinito para mantener el menú activo hasta que el usuario elija salir."""

    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    # Diccionario que mapea las opciones del menú con las rutas de los scripts
    opciones = {
    '1': 'UNIDAD 1 - Fundamentos de la programación orientada a objetos '
         '- POO/Semana 2 - Técnicas de programación/'
         '1.2.1. Ejemplo Tecnicas de Programacion.py',
    '2': 'UNIDAD 1 - Fundamentos de la programación orientada a objetos '
         '- POO/Semana 3 - La POO frente a la programación tradicional/'
         'Tarea. Programación Orientada a Objeto.py',
    '3': 'UNIDAD 1 - Fundamentos de la programación orientada a objetos '
         '- POO/Semana 3 - La POO frente a la programación tradicional/'
         'Tarea. Programación Tradicional.py',
    '4': 'UNIDAD 1 - Fundamentos de la programación orientada a objetos '
         '- POO/Semana 4 - Características de la programación orientada a objetos/'
         'Sistema de Gestión Escolar.py',
    '5': 'UNIDAD 1 - Fundamentos de la programación orientada a objetos '
         '- POO/Semana 4 - Características de la programación orientada a objetos/'
         'Sistema de Reservas de Hotel.py',
    '6': 'UNIDAD 2 - Objetos, clases, Herencia, Polimorfismo/Semana 5 '
         '- Tipos de datos, Identificadores/'
         'Tarea Semana 5 Tipos de Datos e Identificadores.py',
    '7': 'UNIDAD 2 - Objetos, clases, Herencia, Polimorfismo/Semana 6 '
         '- Definición de - clase, Objeto, Herencia, Polimorfismo/'
         'Tarea  Clases, objetos, herencia, encapsulamiento y polimorfismo.py',
    '8': 'UNIDAD 2 - Objetos, clases, Herencia, Polimorfismo/Semana 7 '
         '- Fundamentos de Constructores y destructores/'
         'Tarea Constructores y Destructores.py',
    '9': 'UNIDAD 2 - Objetos, clases, Herencia, Polimorfismo/Semana 8 '
         '- Organización de un proyecto orientado a objetos/'
         'Tarea Semana 8 Dashboard.py'
}
    # Bucle principal del menú
    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        # Solicita al usuario que elija una opción
        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break # Sale del bucle si el usuario elige '0'
        elif eleccion in opciones:
            # Construye la ruta absoluta del script seleccionado
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            # Llama a la función para mostrar el código del script
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


#Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

