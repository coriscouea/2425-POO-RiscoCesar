"""
Registro de Temperaturas Semanales de Guayaquil (POO)
------------------------------------------------------
Descripción: Programa para calcular el promedio de temperaturas
utilizando Programación Orientada a Objetos.

Características:
- Encapsulamiento de datos de temperatura
- Métodos para ingreso y cálculo
- Ejemplo de Abstracción, Herencia y Polimorfismo

"""

# Encapsulamiento: La clase 'RegistroClima' es responsable de almacenar las temperaturas y gestionarlas de manera encapsulada.
class RegistroClima:
    """
    Clase para gestionar registro de temperaturas semanales.

    Atributos:
    - temperaturas (list): Almacena temperaturas diarias (encapsulado)
    - dias (list): Nombres de los días de la semana
    """

    def __init__(self):
        """
        Inicializa un nuevo registro de clima con listas vacías.
        """
        self.temperaturas = []  # Encapsulamiento de la lista de temperaturas
        self.dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    def ingresar_temperaturas(self):
        """
        Solicita y almacena temperaturas para cada día de la semana.
        """
        print("Registro de Temperaturas Semanales de Guayaquil")

        # Limpiar registros previos
        self.temperaturas.clear()  # Encapsulando la manipulación de temperaturas

        # Ingresar temperatura para cada día
        for dia in self.dias:
            temperatura = float(input(f"Temperatura de {dia}: "))
            self.temperaturas.append(temperatura)

    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas registradas.

        Returns:
        float: Promedio de temperaturas con 2 decimales
        """
        # Abstracción: Se abstrae el cálculo del promedio de las temperaturas.
        return sum(self.temperaturas) / len(self.temperaturas)


# Herencia: 'RegistroClimaAvanzado' hereda de 'RegistroClima' y extiende su funcionalidad.
class RegistroClimaAvanzado(RegistroClima):
    """
    Clase derivada que hereda de 'RegistroClima' y agrega más funcionalidad.
    """

    def __init__(self):
        """
        Llama al constructor de la clase base para inicializar la lista de temperaturas.
        """
        super().__init__()  # Llama al constructor de la clase base (RegistroClima)

    # Polimorfismo: Sobrescribimos el método 'calcular_promedio' para una lógica diferente
    def calcular_promedio(self):
        """
        Calcula el promedio de temperaturas, excluyendo la temperatura más baja.

        Returns:
        float: Promedio ajustado (sin la temperatura mínima)
        """
        # Polimorfismo: Comportamiento diferente de 'calcular_promedio' en la clase derivada
        return (sum(self.temperaturas) - min(self.temperaturas)) / (len(self.temperaturas) - 1)


def main():
    """
    Función principal que coordina el flujo del programa.

    Pasos:
    1. Crear instancia de RegistroClima o RegistroClimaAvanzado
    2. Ingresar temperaturas
    3. Calcular y mostrar promedio
    """
    # Abstracción: Solo interactuamos con la interfaz pública de los objetos sin necesidad de saber cómo funcionan internamente
    registro = RegistroClimaAvanzado()  # Podemos crear un objeto de la clase derivada

    # Ingresar temperaturas de la semana
    registro.ingresar_temperaturas()

    # Calcular y mostrar promedio utilizando el método sobrescrito (Polimorfismo)
    promedio = registro.calcular_promedio()
    print(f"\nPromedio ajustado semanal de Guayaquil: {promedio:.2f}°C")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
