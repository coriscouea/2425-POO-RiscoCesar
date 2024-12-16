"""
Registro de Temperaturas Semanales de Guayaquil
-----------------------------------------------
Descripción: Programa para calcular el promedio de temperaturas de una semana
utilizando programación tradicional con funciones.

Características:
- Ingreso de temperaturas diarias
- Cálculo de promedio semanal

"""

def ingresar_temperaturas():
    """
    Recopila las temperaturas diarias de la semana.

    Variables:
    - temperaturas (list): Almacena las temperaturas de cada día
    - dias (list): Nombres de los días para guiar el ingreso

    Returns:
    list: Temperaturas de los 7 días de la semana
    """
    temperaturas = []
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    # Solicitar temperatura para cada día de la semana
    for dia in dias:
        # Convertir entrada a número decimal
        temperatura = float(input(f"Temperatura del dia {dia}: "))
        temperaturas.append(temperatura)

    return temperaturas


def calcular_promedio(temperaturas):
    """
    Calcula el promedio de las temperaturas recopiladas.

    Parámetro:
    - temperaturas (list): Lista de temperaturas diarias

    Returns:
    float: Promedio de temperaturas con 2 decimales
    """

    # Sumar todas las temperaturas y dividir por número de días
    return sum(temperaturas) / len(temperaturas)


def main():
    """
    Función principal que coordena el flujo del programa.

    Pasos:
    1. Ingresar temperaturas
    2. Calcular promedio
    3. Mostrar resultado final
    """
    print("Registro de Temperaturas Semanales de Guayaquil")

    # Ingresar temperaturas de la semana
    temperaturas = ingresar_temperaturas()

    # Calcular promedio de temperaturas
    promedio = calcular_promedio(temperaturas)

    # Mostrar resultado
    print(f"\nPromedio semanal: {promedio:.2f}°C")



# Ejecutar programa
main()