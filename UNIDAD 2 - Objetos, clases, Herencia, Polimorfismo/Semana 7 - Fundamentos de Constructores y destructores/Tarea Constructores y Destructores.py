
class Universidad:
    def __init__(self, asignatura, profesor, alumnos):
        # Constructor que inicializa los atributos de la clase
        self.asignatura = asignatura # 'asignatura' es el nombre de la materia que se está impartiendo.
        self.profesor = profesor # 'profesor' es el nombre del profesor que enseña la asignatura.
        self.alumnos = alumnos # Lista de alumnos
        print("------El método Constructor de 'Universidad' se ha ejecutado con éxito------")

    def informacion(self):
        # Método para mostrar información general
        print(f"Información de la UEA:") # Título general de la información
        print(f"Asignatura: {self.asignatura}")# Imprime el nombre de la asignatura
        print(f"Profesor: {self.profesor}") # Imprime el nombre del profesor
        print("Alumnos:") # Título para la lista de alumnos
        for alumno in self.alumnos:
            # Imprime cada alumno en la lista de alumnos
            print(f"  - {alumno}")

    def evaluar_alumnos(self, calificaciones):
        # Método para evaluar a los alumnos según sus calificaciones.
        print("\nEvaluación de alumnos:")  # Título de la sección de evaluación
        for alumno, nota in calificaciones.items():
            estado = "Aprobado" if nota >= 18 else "Reprobado" # Para cada alumno y su calificación, determina si aprobó o reprobó
            print(f"Alumno: {alumno}, Nota: {nota}, Estado: {estado}")  # Imprime el nombre del alumno, su calificación y su estado (aprobado/reprobado)

    def __del__(self): # Destructor que se ejecuta cuando el objeto es destruido.
        # Destructor que realiza tareas de limpieza
        print("-El Método Destructor de 'Universidad' se ha ejecutado.")


class Asistencia:
    def __init__(self,lista_asistencia ):
    # Constructor que inicializa la lista de asistencias
        self.lista_asistencia = lista_asistencia # 'lista_asistencia' es un diccionario donde las claves son los nombres de los alumnos
        print("------El método Constructor de 'Asistencia' se ha ejecutado con éxito------")

    def informacion(self):
        # Método para mostrar la lista de asistencia de los alumnos.
        print(f"Revisión de Asistencias de Alumnos de la UEA:")  # Título de la sección
        for alumno, asistencia in self.lista_asistencia.items():
            estado = "Presente" if asistencia else "Ausente" # Imprime el estado de asistencia de cada alumno
            print(f" - Alumno:{alumno},Estado: {estado}") # Muestra si el alumno estuvo presente o ausente

    def __del__(self):
        # Destructor que realiza tareas de limpieza
        print("-El método Destructor de 'Asistencia' se ha ejecutado.")

# Instanciación de la clase Universidad con datos de ejemplo
mi_universidad = Universidad("Matemática","Ing. Luis Cedeño",["Cesar Risco", "Ana Lopez", "Beivy Rivera"])
mi_universidad.informacion() # Muestra la información de la universidad (asignatura, profesor, alumnos)

# Diccionario con las calificaciones de los alumnos
calificaciones_alumnos = {"Cesar Risco": 19,"Ana Lopez": 15,"Beivy Rivera": 20}
mi_universidad.evaluar_alumnos(calificaciones_alumnos) # Evaluación de los alumnos basada en sus calificaciones

# Instanciación de la clase Asistencia con datos de ejemplo sobre la asistencia
mi_asistencias = Asistencia({"Cesar Risco": True, "Ana Lopez": False, "Beivy Rivera": True})
mi_asistencias.informacion() # Muestra la información de asistencia de los alumnos


# Eliminación explícita de los objetos, lo que provoca la ejecución de los destructores
del mi_universidad
del mi_asistencias
