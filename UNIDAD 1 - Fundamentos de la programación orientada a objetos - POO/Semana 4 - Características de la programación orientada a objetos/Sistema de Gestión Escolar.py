# Clase que representa a un Estudiante
class Estudiante:
    # El constructor (__init__) se utiliza para crear una instancia del estudiante.
    # Inicializa el nombre, matrícula y una lista vacía de cursos.
    def __init__(self, nombre, matricula):
        self.nombre = nombre  # Atributo para el nombre del estudiante
        self.matricula = matricula  # Atributo para la matrícula del estudiante
        self.cursos = []  # Lista vacía que almacenará los cursos en los que está inscrito el estudiante

    # Metodo para inscribir al estudiante en un curso.
    def inscribir_curso(self, curso):
        self.cursos.append(curso)  # Agrega el curso a la lista de cursos
        print(f"{self.nombre} Se ha inscrito en {curso.nombre}.")  # Muestra un mensaje con la inscripción

# Clase que representa a un Curso
class Curso:
    # El constructor (__init__) inicializa el nombre, código y una lista vacía de estudiantes.
    def __init__(self, nombre, codigo):
        self.nombre = nombre  # Atributo para el nombre del curso
        self.codigo = codigo  # Atributo para el código del curso
        self.estudiantes = []  # Lista vacía que almacenará los estudiantes inscritos en el curso

    # Metodo para agregar un estudiante al curso.
    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)  # Agrega el estudiante a la lista de estudiantes
        print(f"{estudiante.nombre} Se ha agregado {self.nombre}.")  # Muestra un mensaje confirmando que el estudiante fue agregado

# Clase que representa a un Profesor
class Profesor:
    # El constructor (__init__) inicializa el nombre del profesor y una lista vacía de cursos que imparte.
    def __init__(self, nombre):
        self.nombre = nombre  # Atributo para el nombre del profesor
        self.cursos = []  # Lista vacía que almacenará los cursos que el profesor imparte

    # Metodo para asignar un curso al profesor.
    def asignar_curso(self, curso):
        self.cursos.append(curso)  # Agrega el curso a la lista de cursos del profesor
        print(f"{self.nombre} ahora imparte el curso {curso.nombre}.")  # Muestra un mensaje indicando el curso asignado

# Crear instancias de estudiantes, curso y profesor
estudiante1 = Estudiante("Evelyn Loor", "E001")  # Crea un estudiante llamado Evelyn Loor
estudiante2 = Estudiante("Ana López", "E002")  # Crea un estudiante llamado Ana López

curso1 = Curso("Matemáticas", "M001")  # Crea un curso llamado Matemáticas con el código M001
profesor1 = Profesor("Ing. Cesar Risco")  # Crea un profesor llamado Ing. Cesar Risco

# Inscribir a los estudiantes en el curso
estudiante1.inscribir_curso(curso1)  # Evelyn Loor se inscribe en el curso Matemáticas
estudiante2.inscribir_curso(curso1)  # Ana López se inscribe en el curso Matemáticas

# Agregar a los estudiantes al curso
curso1.agregar_estudiante(estudiante1)  # Se agrega a Juan Pérez al curso Matemáticas
curso1.agregar_estudiante(estudiante2)  # Se agrega a Ana López al curso Matemáticas

# Asignar el curso al profesor
profesor1.asignar_curso(curso1)  # Ing. Cesar Risco  asigna el curso Matemáticas
