import json # Se importa el módulo JSON para la manipulación de datos en archivos

# Definición de la clase Producto, que representa un artículo en el inventario
class Producto:
    def __init__(self, id, nombre, cantidad, precio, estado=None):
        """
        Constructor de la clase Producto.
        Inicializa los atributos de un producto en el inventario.

        Parámetros:
        - id (int): Identificador único del producto.
        - nombre (str): Nombre del producto.
        - cantidad (int): Cantidad disponible del producto.
        - precio (float): Precio del producto.
        - estado (str, opcional): Estado del producto. Si no se especifica,
          se asigna "Disponible" si cantidad > 0 o "Agotado" si cantidad es 0.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.estado = "Disponible" if cantidad > 0 else "Agotado"

    def a_diccionario(self):
        """
        Convierte el objeto Producto a un diccionario para su serialización en JSON.
        Retorno:
        dict: Diccionario con los atributos del producto.
        """
        return {
            'id': self.id,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio,
            'estado': self.estado
        }

    def desde_diccionario(datos):
        """
        Crea un objeto Producto a partir de un diccionario.
        Parámetros:
        datos (dict): Diccionario con información del producto.
        Retorno:
        Producto: Instancia de la clase Producto.
        """
        return Producto(
            id=datos['id'],
            nombre=datos['nombre'],
            cantidad=datos['cantidad'],
            precio=datos['precio'],
            estado=datos['estado']
        )

    def __str__(self):
        # Se recalcula el estado para mostrarlo actualizado (opcionalmente podrías usar self.estado)
        estado = "Agotado" if self.cantidad == 0 else "Disponible"
        return (f"\nID: {self.id}"
                f"\nNOMBRE: {self.nombre}"
                f"\nCANTIDAD: {self.cantidad}"
                f"\nPRECIO: ${self.precio:.2f}"
                f"\nESTADO: {estado}")

    def __repr__(self):
        """
        Devuelve una representación formal del producto, útil para depuración.
        Retorno:
        str: Cadena de texto que representa la instancia de Producto.
        """
        return f"Producto({self.id}, {self.nombre}, {self.cantidad}, {self.precio}, {self.estado})"

# Definición de la clase Inventario, encargada de gestionar los productos
class Inventario:
    """
    Clase Inventario que maneja la lista de productos y la persistencia en archivo.
    """
    def __init__(self):
        self.productos = {} # Diccionario donde se almacenarán los productos
        self.archivo_inventario = 'inventario.json' # Nombre del archivo donde se guarda el inventario
        self.archivo_log = 'inventario_log' # Archivo donde se registran los cambios
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario y los almacena en la lista `productos`.
        """
        try:
            with open(self.archivo_inventario, 'r') as f:
                datos = json.load(f)
                # Convertir cada diccionario a objeto Producto
                for producto_dict in datos:
                    producto = Producto.desde_diccionario(producto_dict)
                    self.productos[producto.id] = producto
                print("\nInventario cargado exitosamente.")
        except FileNotFoundError:
            print("\nNo se encontró archivo de inventario. Se creará uno nuevo.")
            self.guardar_inventario()
        except json.JSONDecodeError:
            print("\nError al leer el archivo de inventario. Formato JSON inválido.")
            self.productos = {}
            self.guardar_inventario()
        except Exception as e:
            print(f"\nError inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda todos los productos de la lista `productos` en el archivo de inventario.
        """
        try:
            # Convertir los objetos Producto a diccionarios
            productos_lista = [producto.a_diccionario() for producto in self.productos.values()]

            with open(self.archivo_inventario, 'w') as f:
                json.dump(productos_lista, f, indent=4)

            print("\nInventario guardado exitosamente.")
        except Exception as e:
            print(f"\nError al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        """
        if producto.id in self.productos:
            print(f"\nError: Ya existe un producto con el ID {producto.id}.")
            return False

        self.productos[producto.id] = producto
        self.guardar_inventario()
        self.registrar_cambio(f"Producto agregado: ID={producto.id}, Nombre={producto.nombre}")
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario dado su ID.
        """
        if id in self.productos:
            nombre = self.productos[id].nombre
            del self.productos[id]
            self.guardar_inventario()
            self.registrar_cambio(f"Producto eliminado: ID={id}, Nombre={nombre}")
            print("\nProducto eliminado exitosamente.")
            return True

        print("\nError: No se encontró un producto con ese ID.")
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto en el inventario.
        """
        if id in self.productos:
            producto = self.productos[id]
            cambios = []

            if cantidad is not None:
                antigua_cantidad = producto.cantidad
                producto.cantidad = cantidad
                producto.estado = "Disponible" if cantidad > 0 else "Agotado"
                cambios.append(f"Cantidad={antigua_cantidad} → {cantidad}")

            if precio is not None:
                antiguo_precio = producto.precio
                producto.precio = precio
                cambios.append(f"Precio= ${antiguo_precio:.2f} → $ {precio:.2f}")

            if cambios:
                self.guardar_inventario()
                self.registrar_cambio(f"Producto actualizado: ID={id}, Nombre={producto.nombre}, " + ", ".join(cambios))
                print("\nProducto actualizado y guardado exitosamente.")
                return True
            else:
                print("\nNo se realizaron cambios al producto.")
                return False

        print("\nError: No se encontró un producto con ese ID.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos en el inventario por nombre.
        """
        nombre = nombre.lower()
        resultados = [p for p in self.productos.values() if nombre in p.nombre.lower()]

        if resultados:
            print("\nProductos encontrados:")
            print("\n".join(str(p) for p in resultados))
        else:
            print("\nNo se encontraron productos con ese nombre.")

        return resultados

    def mostrar_todos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            print("\nStock del Inventario Actual:")
            for producto in self.productos.values():
                print(producto)
            print(f"\nTotal de productos: {len(self.productos)}")
        else:
            print("\nEl inventario está vacío.")

    def registrar_cambio(self, mensaje):
        try:
            with open(self.archivo_log, 'a', encoding='utf-8') as file:
                file.write(mensaje + '\n')
        except Exception as e:
            print(f"\nError al registrar el cambio: {e}")

# Función para mostrar el menú del sistema de gestión de inventarios
def mostrar_menu():
    """
    Muestra el menú de opciones del sistema de gestión de inventarios.
    """
    print("\n=== Sistema de Gestión de Inventarios ===")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")
    print("=========================================")

# Función principal que ejecuta el sistema de inventarios
def obtener_entero(mensaje, opcional=False):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "" and opcional:
            return None

        if entrada == "":
            print("Este campo es obligatorio.")
            continue
        try:
            return int(entrada)
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def obtener_float(mensaje, opcional=False):
    while True:
        entrada = input(mensaje).strip()
        if entrada == "" and opcional:
            return None

        if entrada == "":
            print("Este campo es obligatorio.")
            continue
        try:
            return float(entrada)
        except ValueError:
            print("Error: Ingrese un número decimal válido.")

def obtener_string(mensaje):
    while True:
        entrada = input(mensaje).strip()
        if entrada:
            return entrada
        print("Error: El campo no puede estar vacío.")

def main():
    """
    Función principal que ejecuta el sistema de gestión de inventarios.
    Muestra el menú, procesa las opciones del usuario y realiza las operaciones correspondientes.
    """
    inventario = Inventario()

    while True:
        try:
            mostrar_menu()
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1": # Lógica para añadir un producto
                id = obtener_entero("Ingrese el ID del producto: ")
                if id in inventario.productos:
                    print(f"\nError: Ya existe un producto con el ID {id}.")
                    continue

                nombre = obtener_string("Ingrese el nombre del producto: ")
                cantidad = obtener_entero("Ingrese la cantidad del producto: ")
                precio = obtener_float("Ingrese el precio del producto: ")

                producto = Producto(id, nombre, cantidad, precio)
                if inventario.añadir_producto(producto):
                    print("\nProducto añadido exitosamente.")

            elif opcion == "2": # Lógica para eliminar un producto
                id = obtener_entero("Ingrese el ID del producto a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "3": # Actualizar producto
                id = obtener_entero("Ingrese el ID del producto a actualizar: ")
                if id not in inventario.productos:
                    print("\nError: No se encontró un producto con ese ID.")
                    continue

                print(f"\nProducto actual: {inventario.productos[id]}")
                cantidad = obtener_entero("Ingrese la nueva cantidad (Enter para no cambiar): ", opcional=True)

                precio = obtener_float("Ingrese el nuevo precio (Enter para no cambiar): ", opcional=True)
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "4": # Buscar por nombre
                nombre = obtener_string("Ingrese el nombre del producto a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "5": # Mostrar todos
                inventario.mostrar_todos()

            elif opcion == "6": # Salir
                print("\nGuardando inventario...", end="")
                inventario.guardar_inventario()
                print("\n¡Gracias por usar el Sistema de Gestión de Inventarios!")
                break

            else:
                print("\nOpción no válida. Por favor, seleccione una opción del 1 al 6.")

        except KeyboardInterrupt:
            """
            Maneja la interrupción del programa por parte del usuario (Ctrl + C).
            Cuando el usuario presiona Ctrl + C, se captura la excepción KeyboardInterrupt,
            mostrando un mensaje y permitiendo que el programa continúe sin finalizar abruptamente.
            """
            print("\n\nOperación cancelada por el usuario.")
            continue
        except Exception as e:
            print(f"\nError inesperado: {e}")
            """
            Captura cualquier otra excepción inesperada durante la ejecución del programa.
            Esto evita que el programa se detenga debido a errores no previstos y muestra
            un mensaje de error con detalles sobre la excepción ocurrida.
            """
if __name__ == "__main__":
    main()