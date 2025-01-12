# Función para verificar si un estudiante ha aprobado una materia según su calificación
def verificar_aprobacion():
    # Solicitar el nombre del estudiante (tipo string)
    nombre_estudiante = input("Ingrese el nombre del estudiante: ") #nombre_estudiante identificador descriptivos snake_case

    # Solicitar la calificación final del estudiante (tipo float)
    calificacion = float(input("Ingrese la calificación final: ")) #nombre_estudiante identificador descriptivos snake_case

    # Evaluar si la calificación es suficiente para aprobar (tipo boolean)
    aprobado = calificacion >= 7.0  #nombre_estudiante identificador descriptivos snake_case

    # resultados
    print("\n=== Verificación de Aprobación ===")
    print(f"Estudiante: {nombre_estudiante}")  # Muestra nombre del estudiante
    print(f"Calificación: {calificacion}")  # Muestra calificación obtenida
    print(f"¿Aprobó? {'Sí' if aprobado else 'No'}")  # Muestra resultado de aprobación

# Llamar a la función principal para ejecutar el programa
verificar_aprobacion()
