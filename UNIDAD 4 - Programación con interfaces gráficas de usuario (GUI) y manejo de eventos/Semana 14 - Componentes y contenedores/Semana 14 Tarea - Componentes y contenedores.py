from tkinter import Tk, Label, Entry, Frame, messagebox, Button
from tkinter import ttk # Módulo de widgets mejorados de tkinte
from tkcalendar import DateEntry # Widget especial para selección de fechas
from datetime import datetime

# Configuración de la ventana principal
agenda = Tk() # Crear la ventana raíz de la aplicación
agenda.title("Agenda Personal") # Establecer el título de la ventana
agenda.geometry("600x550")  # Dimensiones iniciales de la ventana (ancho x alto)
agenda.configure(bg="lightblue") # Color de fondo para la ventana

def validar_hora(hora):
    """
    Valida que la hora tenga el formato correcto (HH:MM).
    Args:
    hora (str): String con la hora a validar
    Returns:
    bool: True si la hora tiene formato válido, False en caso contrario
    """
    try:
        # Intenta convertir la cadena a un objeto datetime con el formato especificado
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        # Si hay un error al convertir, el formato es incorrecto
        return False

def agregar_evento():
    """Agrega un nuevo evento a la lista (TreeView)."""
    fecha = fecha_entry.get() # Obtener la fecha seleccionada
    hora = hora_entry.get().strip() # Obtener la hora y eliminar espacios en blanco
    descripcion = descripcion_entry.get().strip() # Obtener la descripción y eliminar espacios

    if not descripcion:
        messagebox.showwarning("Campos Vacíos", "Por favor ingresa una descripción.")
        return

    # Manejar el campo de hora
    if not hora: # Si el campo de hora está vacío, usar la hora actual
        hora = datetime.now().strftime("%H:%M:%S")
    elif not validar_hora(hora): # Si la hora ingresada es incorrecta
        messagebox.showwarning("Formato incorrecto", "Por favor ingresa la hora en formato HH:MM")
        return

    # Insertar el evento en el TreeView
    eventos_tree.insert("", "end", values=(fecha, hora, descripcion))
    limpiar_campos() # Limpiar los campos después de agregar el evento

def eliminar_evento():
    """Elimina el evento seleccionado del TreeView."""
    try:
        seleccion = eventos_tree.selection()[0] # Obtener el ítem seleccionado
        eventos_tree.delete(seleccion) # Eliminar el ítem seleccionado
    except IndexError:
        # Si no hay ningún elemento seleccionado, mostrar advertencia
        messagebox.showwarning("Sin Selección", "Por favor selecciona un evento para eliminar.")

def salir():
    """Cierra la aplicación con confirmación."""
    if messagebox.askyesno("Salir", "¿Seguro que deseas salir de la aplicación?"):
        agenda.destroy() # Cerrar la ventana y terminar la aplicación

def limpiar_campos():
    """Limpia los campos de entrada después de agregar un evento."""
    fecha_entry.set_date(datetime.today()) # Restablecer la fecha al día actual
    hora_entry.delete(0, "end") # Borrar el campo de hora
    descripcion_entry.delete(0, "end") # Borrar el campo de descripción

# ----- SECCIÓN DE INTERFAZ GRÁFICA -----

# Frame para el TreeView (lista de eventos)
tree_frame = Frame(agenda)
tree_frame.pack(pady=10, fill="both", expand=True, padx=10)

# Configuración del TreeView (tabla para mostrar los eventos)
columnas = ("Fecha", "Hora", "Descripción")
eventos_tree = ttk.Treeview(tree_frame, columns=columnas, show="headings", height=10)

# Definir los encabezados de las columnas
eventos_tree.heading("Fecha", text="Fecha")
eventos_tree.heading("Hora", text="Hora")
eventos_tree.heading("Descripción", text="Descripción")

# Configurar el ancho de las columnas
eventos_tree.column("Fecha",width=120)
eventos_tree.column("Hora",width=80)
eventos_tree.column("Descripción",width=300, stretch=True) # Permitir expansión automática

# Colocar el TreeView en su frame
eventos_tree.pack(side="left", fill="both",expand=True)

# Configuración del scrollbar (barra de desplazamiento) para el TreeView
tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=eventos_tree.yview)
tree_scroll.pack(side="right", fill="y")
eventos_tree.configure(yscrollcommand=tree_scroll.set)

# Frame para los campos de entrada de datos
input_frame = Frame(agenda, bg="lightblue")
input_frame.pack(pady=10, fill="x", padx=10)

# ----- CAMPOS DE ENTRADA -----

# Campo para la fecha
Label(input_frame, text="Fecha:", bg="lightblue", font=("Aptos", 15, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
fecha_entry = DateEntry(input_frame, width=18, background='darkblue', foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy') # Formato de fecha día/mes/año
fecha_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Campo para la hora
Label(input_frame, text="Hora (HH:MM):", bg="lightblue", font=("Aptos", 15, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
hora_entry = Entry(input_frame, width=20)  # Ahora correctamente definido como Entry de tkinter
hora_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Campo para la descripción
Label(input_frame, text="Descripción:", bg="lightblue", font=("Aptos", 15, "bold")).grid(row=2, column=0, padx=5, pady=5, sticky="w")
descripcion_entry = Entry(input_frame, width=40)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# ----- BOTONES DE ACCIÓN -----

# Frame para los botones
button_frame = Frame(agenda, bg="lightblue")
button_frame.pack(pady=10)

# Estilo común para los botone
estilo_botones = {'font': ('Aptos', 10, 'bold'), 'bg': '#4CAF50', 'fg': 'white', 'padx': 10, 'pady': 5, 'width': 15} # Color verde para botones principales

# Botones de acción
Button(button_frame, text="Agregar Evento", command=agregar_evento,**estilo_botones).grid(row=0, column=0, padx=10)
Button(button_frame, text="Eliminar Evento", command=eliminar_evento,**estilo_botones).grid(row=0, column=1, padx=10)
Button(button_frame, text="Salir", command=salir, bg='#f44336', fg='white', font=('Arial', 10, 'bold'), width=15).grid(row=0, column=3, padx=10) # Color rojo para el botón de salir

# ----- INICIO DE LA APLICACIÓN -----

# Bucle principal de la aplicación con manejo de excepciones
try:
    agenda.mainloop() # Iniciar el bucle de eventos de la aplicación
except Exception as e:
    # Capturar cualquier error inesperado y mostrarlo en un mensaje
    messagebox.showerror("Error Crítico", f"Se ha producido un error inesperado: {str(e)}")

