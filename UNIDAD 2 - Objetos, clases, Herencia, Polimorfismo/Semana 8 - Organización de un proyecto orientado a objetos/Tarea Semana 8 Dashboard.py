import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

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
         'Ejemplo Organización Proyecto.py'
}
        # Agrega aquí el resto de las rutas de los scripts
    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()

