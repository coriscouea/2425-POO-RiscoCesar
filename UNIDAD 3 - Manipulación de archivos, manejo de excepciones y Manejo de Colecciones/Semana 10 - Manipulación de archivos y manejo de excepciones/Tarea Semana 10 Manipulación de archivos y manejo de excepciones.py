class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.
        Inicializa los atributos del producto.
        Parámetros:
            id (int): Identificador único del producto.
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible del producto.
            precio (float): Precio del producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def convertir_a_texto(self):
        """
        Convierte la información del producto en una cadena de texto formateada
        para su almacenamiento en el archivo de inventario.
        Retorno:
            str: Cadena de texto que representa el producto en un formato legible.
        """
        return \
            f"\n--- Archivo de Inventario ---\n" \
            f"ID del Producto:        |{self.id}\n" \
            f"Nombre del Producto:    |{self.nombre}\n" \
            f"Cantidad del Producto:  |{self.cantidad}\n" \
            f"Precio del Producto $:  |{self.precio:.2f}\n" \
            "-----------------------------"

    def crear_desde_texto(linea):
        """
        Método estático que crea una instancia de Producto a partir de una cadena de texto formateada.
        Parámetros:
            linea (str): Cadena de texto que contiene la información del producto.
        Retorno:
            Producto: Instancia de Producto con los datos extraídos del texto.
        Excepciones:
            ValueError: Si el formato de los datos es incompleto o incorrecto.
        """
        lineas = linea.split('\n')
        datos = {}

        for linea in lineas:
            if '|' in linea:
                # Dividir por | y tomar el valor después del |
                valor = linea.split('|')[1].strip()
                if "ID del Producto" in linea:
                    datos['id'] = int(valor)
                elif "Nombre del Producto" in linea:
                    datos['nombre'] = valor
                elif "Cantidad del Producto" in linea:
                    datos['cantidad'] = int(valor)
                elif "Precio del Producto" in linea:
                    datos['precio'] = float(valor)

        if len(datos) == 4:  # Asegurarse de que tenemos todos los datos
            return Producto(datos['id'], datos['nombre'], datos['cantidad'], datos['precio'])
        raise ValueError("Formato de datos incompleto")

    def __str__(self):
        """
        Devuelve una representación en cadena de texto del producto, incluyendo su estado (Disponible o Agotado).
        Retorno:
            str: Cadena de texto que describe el producto.
        """
        estado = "Agotado" if self.cantidad == 0 else "Disponible"
        return (f"\nID: {self.id}"
                f"\nNOMBRE: {self.nombre}"
                f"\nCANTIDAD: {self.cantidad}"
                f"\nPRECIO: {self.precio:.2f}"
                f"\nESTADO: {estado}")

    def __repr__(self):
        """
        Devuelve una representación formal del producto, útil para depuración.
        Retorno:
            str: Cadena de texto que representa la instancia de Producto.
        """
        return f"Producto({self.id}, {self.nombre}, {self.cantidad}, {self.precio})"


class Inventario:
    """
    Constructor de la clase Inventario.
    Inicializa la lista de productos y carga el inventario desde el archivo.
    """
    def __init__(self):
        self.productos = []
        self.archivo_inventario = 'inventario.txt'
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga los productos desde el archivo de inventario y los almacena en la lista `productos`.
        Excepciones:
            FileNotFoundError: Si el archivo de inventario no existe.
            PermissionError: Si no hay permisos para acceder al archivo.
            Exception: Captura cualquier otro error inesperado.
        """
        try:
            with open(self.archivo_inventario, 'r', encoding='utf-8') as file:
                contenido = file.read()
                # Dividir por los separadores de productos
                productos_texto = contenido.split("-----------------------------")

                for producto_texto in productos_texto:
                    if producto_texto.strip():  # Ignorar espacios vacíos
                        try:
                            producto = Producto.crear_desde_texto(producto_texto)
                            self.productos.append(producto)
                        except (ValueError, IndexError) as e:
                            print(f"\nError al procesar producto: {e}")

                print("\nInventario cargado exitosamente.")

        except FileNotFoundError:
            print("\nNo se encontró archivo de inventario. Se creará uno nuevo.")
            self.guardar_inventario()
        except PermissionError:
            print("\nError: No hay permisos para acceder al archivo de inventario.")
        except Exception as e:
            print(f"\nError inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda todos los productos de la lista `productos` en el archivo de inventario.
        Excepciones:
            PermissionError: Si no hay permisos para escribir en el archivo.
            Exception: Captura cualquier otro error inesperado.
        """
        try:
            with open(self.archivo_inventario, 'w', encoding='utf-8') as file:
                for producto in self.productos:
                    file.write(producto.convertir_a_texto() + '\n')
        except PermissionError:
            print("\nError: No hay permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"\nError al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario y guarda los cambios en el archivo.
        Parámetros:
        producto (Producto): Instancia de Producto que se va a añadir.
        Retorno:
        bool: True si el producto se añadió correctamente, False si ya existe un producto con el mismo ID.
        """
        if any(p.id == producto.id for p in self.productos):
            print(f"\nError: Ya existe un producto con el ID {producto.id}.")
            return False

        self.productos.append(producto)
        self.guardar_inventario()
        self.registrar_cambio(f"Producto agregado: ID={producto.id}, Nombre={producto.nombre}")
        print("\nProducto añadido y guardado exitosamente.")
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID y guarda los cambios en el archivo.
        Parámetros:
        id (int): ID del producto a eliminar.
        Retorno:
        bool: True si el producto se eliminó correctamente, False si no se encontró el producto.
        """
        producto = next((p for p in self.productos if p.id == id), None)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            self.registrar_cambio(f"Producto eliminado: ID={id}")
            print("\nProducto eliminado y guardado exitosamente.")
            return True
        print("\nError: No se encontró un producto con ese ID.")
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto por su ID y guarda los cambios en el archivo.
        Parámetros:
        id (int): ID del producto a actualizar.
        cantidad (int, opcional): Nueva cantidad del producto.
        precio (float, opcional): Nuevo precio del producto.
        Retorno:
        bool: True si el producto se actualizó correctamente, False si no se encontró el producto.
        """
        producto = next((p for p in self.productos if p.id == id), None)
        if producto:
            cambios = []
            if cantidad is not None:
                producto.cantidad = cantidad
                cambios.append(f"Cantidad={cantidad}")
            if precio is not None:
                producto.precio = precio
                cambios.append(f"Precio={precio}")

            self.guardar_inventario()
            if cambios:
                self.registrar_cambio(f"Producto actualizado: ID={id}, " + ", ".join(cambios))
            print("\nProducto actualizado y guardado exitosamente.")
            return True
        print("\nError: No se encontró un producto con ese ID.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre y muestra los resultados.
        Parámetros:
        nombre (str): Nombre o parte del nombre del producto a buscar.
        """
        resultados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if resultados:
            print("\nProductos encontrados:")
            print("\n".join(str(p) for p in resultados))
        else:
            print("\nNo se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.productos:
            print("\nStock del Inventario Actual:")
            for producto in self.productos:
                print(producto)
        else:
            print("\nEl inventario está vacío.")

    def registrar_cambio(self, mensaje):
        """
        Registra un mensaje en el archivo de log (`inventario_log.txt`).
        Parámetros:
        mensaje (str): Mensaje que se va a registrar.
        Excepciones:
        PermissionError: Si no hay permisos para escribir en el archivo de log.
        Exception: Captura cualquier otro error inesperado.
        """
        try:
            with open('inventario_log.txt', 'a', encoding='utf-8') as file:
                file.write(mensaje + '\n')
        except PermissionError:
            print("\nError: No hay permisos para escribir en el archivo de log.")
        except Exception as e:
            print(f"\nError al registrar el cambio: {e}")


def mostrar_menu():
    """
    Muestra el menú de opciones del sistema de gestión de inventarios.
    """
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")


def obtener_entero(mensaje):
    """
    Solicita al usuario un número entero y valida la entrada.
    Parámetros:
    mensaje (str): Mensaje que se muestra al usuario.
    Retorno:
    int: El número entero ingresado por el usuario.
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            if entrada == "":
                print("Este campo es obligatorio.")
                continue
            return int(entrada)
        except ValueError:
            print("Error: Ingrese un número entero válido.")


def obtener_float(mensaje):
    """
    Solicita al usuario un número decimal y valida la entrada.
    Parámetros:
    mensaje (str): Mensaje que se muestra al usuario.
    Retorno:
    float: El número decimal ingresado por el usuario, o None si el campo es opcional.
    """
    while True:
        try:
            entrada = input(mensaje).strip()
            if entrada == "":
                return None
            return float(entrada)
        except ValueError:
            print("Error: Ingrese un número decimal válido.")


def obtener_string(mensaje):
    """
    Solicita al usuario una cadena de texto y valida que no esté vacía.
    Parámetros:
    mensaje (str): Mensaje que se muestra al usuario.
    Retorno:
    str: La cadena de texto ingresada por el usuario.
    """
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

            if opcion == "1":
                id = obtener_entero("Ingrese el ID del producto: ")
                if any(p.id == id for p in inventario.productos):
                    print(f"\nError: Ya existe un producto con el ID {id}.")
                    continue

                nombre = obtener_string("Ingrese el nombre del producto: ")
                cantidad = obtener_entero("Ingrese la cantidad del producto: ")
                precio = obtener_float("Ingrese el precio del producto: ")

                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id = obtener_entero("Ingrese el ID del producto a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "3":
                id = obtener_entero("Ingrese el ID del producto a actualizar: ")
                cantidad = obtener_entero("Ingrese la nueva cantidad (Enter para no cambiar): ")
                precio = obtener_float("Ingrese el nuevo precio (Enter para no cambiar): ")
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "4":
                nombre = obtener_string("Ingrese el nombre del producto a buscar: ")
                inventario.buscar_por_nombre(nombre)

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("\nSaliendo del sistema...")
                break

            else:
                print("\nOpción no válida. Intente de nuevo.")

        except Exception as e:
            print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    main()