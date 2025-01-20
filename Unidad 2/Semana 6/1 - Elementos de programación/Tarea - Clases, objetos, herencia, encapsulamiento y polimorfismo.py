# Clase base que representa una Laptop genérica
class Laptop:
    def __init__(self, marca, procesador, color, numeroDeGeneracion):
        # Atributos encapsulados (privados)
        self._marca = marca
        self._procesador = procesador
        self._color = color
        self._numeroDeGeneracion = numeroDeGeneracion

    # Metodos getter para acceder a los atributos encapsulados
    def get_marca(self):
        return self._marca

    def get_procesador(self):
        return self._procesador

    def get_color(self):
        return self._color

    def get_numeroDeGeneracion(self):
        return self._numeroDeGeneracion

    # Metodo para mostrar información de la laptop
    def mostrar_informacion(self):
        return (f"Marca: {self._marca}, Procesador: {self._procesador}, "
                f"Color: {self._color}, Generación: {self._numeroDeGeneracion}")

    # Metodo que puede ser sobrescrito por clases derivadas (Polimorfismo)
    def tipo_de_laptop(self):
        return "Esta es una laptop genérica."


# Clase derivada que representa una Laptop Gamer, hereda de Laptop
class LaptopGamer(Laptop):
    def __init__(self, marca, procesador, color, numeroDeGeneracion, tarjeta_grafica):
        # Llama al constructor de la clase base (Laptop)
        super().__init__(marca, procesador, color, numeroDeGeneracion)
        # Atributo adicional específico de LaptopGamer
        self._tarjeta_grafica = tarjeta_grafica

    # Metodo getter para el atributo adicional
    def get_tarjeta_grafica(self):
        return self._tarjeta_grafica

    # Sobrescribe el metodo de la clase base (Polimorfismo)
    def tipo_de_laptop(self):
        return "Esta es una laptop gamer."

    # Extiende el metodo para mostrar información adicional
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        return f"{info_base}, Tarjeta gráfica: {self._tarjeta_grafica}"


# Creación de instancias y demostración de funcionalidad
if __name__ == "__main__":
    # Instancia de la clase base Laptop
    mi_laptop = Laptop("Dell", "Intel i5", "Negro", 10)
    print(mi_laptop.mostrar_informacion())  # Muestra información de la laptop
    print(mi_laptop.tipo_de_laptop())  # Muestra el tipo de laptop (genérica)

    # Instancia de la clase derivada LaptopGamer
    mi_laptop_gamer = LaptopGamer("Asus", "Intel i7", "Rojo", 11, "NVIDIA RTX 3060")
    print(mi_laptop_gamer.mostrar_informacion())  # Muestra información de la laptop gamer
    print(mi_laptop_gamer.tipo_de_laptop())  # Muestra el tipo de laptop (gamer)

    # Demostración de encapsulación usando getters
    print(f"Marca de la laptop gamer: {mi_laptop_gamer.get_marca()}")  # Accede a la marca encapsulada
    print(f"Tarjeta gráfica de la laptop gamer: {mi_laptop_gamer.get_tarjeta_grafica()}")  # Accede a la tarjeta gráfica encapsulada







