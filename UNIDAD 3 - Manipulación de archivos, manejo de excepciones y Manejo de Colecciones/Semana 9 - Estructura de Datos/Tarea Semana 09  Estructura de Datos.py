class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return (f"\nID: {self.id}" 
                f"\nNOMBRE: {self.nombre}"
                f"\nCANTIDAD: {self.cantidad}"
                f"\nPRECIO: {self.precio:.2f}")

    def __repr__(self):
        return f"Producto({self.id}, {self.nombre}, {self.cantidad}, {self.precio})"


class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        if any(p.get_id() == producto.get_id() for p in self.productos):
            print(f"\nError: Ya existe un producto con el ID {producto.get_id()}.")
        else:
            self.productos.append(producto)
            print("\nProducto añadido exitosamente.")

    def eliminar_producto(self, id):
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            self.productos.remove(producto)
            print("\nProducto eliminado exitosamente.")
        else:
            print("\nError: No se encontró un producto con ese ID.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.get_id() == id), None)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("\nProducto actualizado exitosamente.")
        else:
            print("\nError: No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("\nProductos encontrados:")
            for producto in resultados:
                print(producto)
        else:
            print("\nNo se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("\nStock del Inventario Actual:")
            for producto in self.productos:
                print(producto)
        else:
            print("\nEl inventario está vacío.")


def mostrar_menu():
    print("\n--- Sistema de Gestión de Inventarios ---")
    print("1. Añadir Producto")
    print("2. Eliminar Producto")
    print("3. Actualizar Producto")
    print("4. Buscar Producto por Nombre")
    print("5. Mostrar Todos los Productos")
    print("6. Salir")


def obtener_entero(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            if entrada == "":
                return None  # Permite que el usuario deje vacío el campo
            return int(entrada)
        except ValueError:
            print("Error: Ingrese un número entero válido.")


def obtener_float(mensaje):
    while True:
        try:
            entrada = input(mensaje).strip()
            if entrada == "":
                return None
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
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            id = obtener_entero("Ingrese el ID del producto: ")
            if any(p.get_id() == id for p in inventario.productos):
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


if __name__ == "__main__":
    main()
