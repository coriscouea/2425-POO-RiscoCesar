# Clase que representa un Hotel
class Hotel:
    # El constructor (__init__) inicializa el nombre, la ubicación y una lista vacía de habitaciones.
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre  # Atributo para el nombre del hotel
        self.ubicacion = ubicacion  # Atributo para la ubicación del hotel
        self.habitaciones = []  # Lista vacía que almacenará las habitaciones del hotel


    # Metodo para agregar una habitación al hotel.
    def agregar_habitacion(self, numero):
        """Agrega una habitación con su número al hotel."""
        self.habitaciones.append({"numero": numero, "estado": "disponible"})  # Agrega un diccionario con el número y estado de la habitación (disponible)


    # Metodo para mostrar todas las habitaciones y su estado (disponible o reservada).
    def mostrar_habitaciones(self):
        """Muestra todas las habitaciones y su estado."""
        if not self.habitaciones:  # Verifica si la lista de habitaciones está vacía
            print("No hay habitaciones registradas.")  # Si no hay habitaciones, muestra este mensaje
        for habitacion in self.habitaciones:  # Recorre todas las habitaciones en la lista
            print(f"Habitación {habitacion['numero']}: {habitacion['estado']}")  # Muestra el número de la habitación y su estado (disponible o reservada)


    # Metodo para reservar una habitación (cambiar su estado a 'reservada').
    def reservar_habitacion(self, numero):
        """Cambia el estado de una habitación a 'reservada'."""
        for habitacion in self.habitaciones:  # Recorre todas las habitaciones
            if habitacion["numero"] == numero and habitacion["estado"] == "disponible":  # Si la habitación es la que se busca y está disponible
                habitacion["estado"] = "reservada"  # Cambia el estado de la habitación a "reservada"
                print(f"Habitación {numero} reservada con éxito.")  # Muestra un mensaje de confirmación
                return  # Sale del me|todo
        print(f"Habitación {numero} no está disponible.")  # Si no se encuentra o la habitación no está disponible, muestra este mensaje


    # Metodo para liberar una habitación (cambiar su estado a 'disponible').
    def liberar_habitacion(self, numero):
        """Cambia el estado de una habitación a 'disponible'."""
        for habitacion in self.habitaciones:  # Recorre todas las habitaciones
            if habitacion["numero"] == numero and habitacion["estado"] == "reservada":  # Si la habitación es la que se busca y está reservada
                habitacion["estado"] = "disponible"  # Cambia el estado de la habitación a "disponible"
                print(f"Habitación {numero} está ahora disponible.")  # Muestra un mensaje de confirmación
                return  # Sale del metodo
        print(f"Habitación {numero} no está reservada.")  # Si la habitación no estaba reservada, muestra este mensaje


# Instancia del Hotel
mi_hotel = Hotel("Hotel Paraíso", "Ciudad Central")  # Crea un objeto de la clase Hotel con el nombre "Hotel Paraíso" y la ubicación "Ciudad Central"

# Agregar habitaciones
mi_hotel.agregar_habitacion(101)  # Agrega una habitación con el número 101
mi_hotel.agregar_habitacion(102)  # Agrega una habitación con el número 102
mi_hotel.agregar_habitacion(103)  # Agrega una habitación con el número 103

# Mostrar habitaciones
mi_hotel.mostrar_habitaciones()  # Muestra todas las habitaciones y su estado (disponible)

# Reservar una habitación
mi_hotel.reservar_habitacion(102)  # Reserva la habitación 102

# Mostrar habitaciones después de reservar
mi_hotel.mostrar_habitaciones()  # Muestra las habitaciones después de la reserva (la habitación 102 debería aparecer como reservada)

# Liberar una habitación
mi_hotel.liberar_habitacion(102)  # Libera la habitación 102

# Mostrar habitaciones después de liberar
mi_hotel.mostrar_habitaciones()  # Muestra las habitaciones después de liberar (la habitación 102 debería aparecer como disponible)


