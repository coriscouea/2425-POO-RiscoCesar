"""
Aplicación de Gestión de Tareas
------------------------------
Una aplicación GUI simple para gestionar tareas con las siguientes características:
- Agregar nuevas tareas mediante un campo de texto
- Marcar tareas como pendientes o completadas con indicadores visuales
- Eliminar tareas seleccionadas
- Atajos de teclado para operaciones comunes
Esta aplicación utiliza tkinter para la interfaz gráfica de usuario.
"""

import tkinter as tk
from tkinter import ttk, messagebox

# ==============================================
# FUNCIONES PRINCIPALES DE LA APLICACIÓN
# ==============================================

def agregar_tarea(event=None):
    """
    Agrega una nueva tarea a la lista de tareas.
    Esta función obtiene el texto del campo de entrada, valida que no esté
    vacío y lo agrega a la lista de tareas con estado 'Pendiente'. Si la
    entrada está vacía, muestra un mensaje de advertencia.
    Parámetros:
        event: Parámetro opcional de evento para admitir enlaces a eventos de teclado
    """
    tarea = entrada.get().strip()  # Obtiene y limpia el texto del campo de entrada

    if tarea:  # Comprueba si el texto de la tarea no está vacío

        # Agrega la tarea a la lista con estado 'Pendiente'
        lista_tareas.insert('', 'end', values=(tarea, "Pendiente"), tags=('Pendiente',))
        entrada.delete(0, tk.END)  # Limpia el campo de entrada después de agregar
    else:
        # Muestra una advertencia si se intenta agregar una tarea vacía
        messagebox.showwarning("Advertencia", "No puedes agregar una tarea vacía.")

def cambiar_estado(event=None):
    """
    Alterna el estado de la tarea seleccionada entre 'Pendiente' y 'Completada'.
    Esta función identifica la tarea seleccionada en la lista, obtiene su
    estado actual y lo cambia al estado opuesto. La apariencia visual
    cambia según la etiqueta asignada a la fila de la tarea.
    Parámetros:
        event: Parámetro opcional de evento para admitir enlaces a eventos de teclado
    """
    seleccion = lista_tareas.selection()  # Obtiene los elementos seleccionados

    if seleccion:  # Comprueba si hay algún elemento seleccionado
        item = seleccion[0]  # Obtiene el primer elemento seleccionado
        tarea, estado = lista_tareas.item(item, "values")  # Obtiene los valores actuales

        # Alterna el estado entre 'Pendiente' y 'Completada'
        nuevo_estado = "Completada" if estado == "Pendiente" else "Pendiente"

        # Actualiza el elemento con el nuevo estado y la etiqueta visual correspondiente
        lista_tareas.item(item, values=(tarea, nuevo_estado), tags=(nuevo_estado,))
    else:
        # Informa al usuario si no se ha seleccionado ninguna tarea
        messagebox.showinfo("Información", "Selecciona una tarea.")

def eliminar_tarea(event=None):
    """
    Elimina la(s) tarea(s) seleccionada(s) de la lista después de la confirmación.
    Esta función verifica si hay tareas seleccionadas, pide confirmación
    antes de eliminarlas y luego elimina las tareas seleccionadas de la lista.
    Parámetros:
        event: Parámetro opcional de evento para admitir enlaces a eventos de teclado
    """
    seleccion = lista_tareas.selection()  # Obtiene los elementos seleccionados

    # Confirma la eliminación con un diálogo y procede si se confirma
    if seleccion and messagebox.askyesno("Confirmación", "¿Eliminar tarea seleccionada?"):
        for item in seleccion:
            lista_tareas.delete(item)  # Elimina cada elemento seleccionado
    else:
        messagebox.showinfo("Información", "Por favor selecciona una tarea.")


def salir(event=None):
    """
    Sale de la aplicación.
    Esta función termina la aplicación llamando al metodo quit.
    Parámetros:
        event: Parámetro opcional de evento para admitir enlaces a eventos de teclado
    """
    app.quit()  # Cierra la aplicación

# ==============================================
# CONFIGURACIÓN DE LA INTERFAZ GRÁFICA
# ==============================================

# Inicializa la ventana principal de la aplicación
app = tk.Tk()
app.title("Aplicación GUI")  # Establece el título de la ventana
app.geometry("600x600")  # Define el tamaño inicial de la ventana

# Configura atajos de teclado para funciones comunes
app.bind("<Return>", agregar_tarea)  # Atajo: Enter para agregar tarea
app.bind("<c>", cambiar_estado)  # Atajo: C para cambiar estado
app.bind("<d>", eliminar_tarea)  # Atajo: D para eliminar tarea
app.bind("<Escape>", salir)  # Atajo: Escape para cerrar

# Configuración del estilo visual de la interfaz
estilo = ttk.Style()
estilo.theme_use("clam")  # Establece el tema visual 'clam' para los widgets ttk

# ==============================================
# COMPONENTES DE LA INTERFAZ
# ==============================================

# Título Principal de la aplicación
titulo = tk.Label(app, text="Lista de Tareas", font=("Verdana", 20, "bold"))
titulo.pack(pady=10)  # Agrega espacio vertical alrededor del título

# Campo de entrada y botón para agregar tareas
entrada = tk.Entry(app, font=("Arial", 12))  # Campo de texto para introducir tareas
entrada.pack(pady=10, padx=10, fill=tk.X)  # Expande horizontalmente en la ventana
entrada.focus()  # Coloca el cursor en el campo de entrada al iniciar

# Botón para agregar tareas con estilo personalizado
tk.Button(app, text="➕ Agregar", command=agregar_tarea,
          bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10, padx=10)

# Tabla para mostrar las tareas con columnas definidas
columnas = ("Tarea", "Estado")
lista_tareas = ttk.Treeview(app, columns=columnas, show='headings', height=15)
lista_tareas.heading("Tarea", text="Tarea")  # Título de la columna Tarea
lista_tareas.heading("Estado", text="Estado")  # Título de la columna Estado

# Configuración de las dimensiones de las columnas
lista_tareas.column("Tarea", minwidth=400, width=400)
lista_tareas.column("Estado", minwidth=100, width=100, anchor=tk.CENTER)

# Configuración de los estilos visuales para los diferentes estados de las tareas
lista_tareas.tag_configure("Pendiente", background="#fff3cd", foreground="#856404")  # Amarillo para pendientes
lista_tareas.tag_configure("Completada", background="#d4edda", foreground="#155724")  # Verde para completadas
lista_tareas.pack(fill=tk.BOTH, pady=10, padx=10, expand=True)  # Expande para llenar el espacio disponible

# ==============================================
# BOTONES DE LA APLICACIÓN
# ==============================================

# Marco para contener los botones de acción
botones = tk.Frame(app)

# Botón para cambiar el estado de las tareas
tk.Button(botones, text="Cambiar Estado (C)", command=cambiar_estado,
          bg="#2196F3", fg="white", relief="flat", font=("Arial", 10, "bold")).pack(side=tk.LEFT, padx=5)

# Botón para eliminar tareas
tk.Button(botones, text="Eliminar (D)", command=eliminar_tarea,
          bg="#f44336", fg='white', font=("Arial", 10, "bold"), relief="flat", padx=15).pack(side=tk.LEFT, padx=5)

# Botón para salir de la aplicación
tk.Button(botones, text="Salir (Esc)", command=salir,
          bg="#E0E0E0", font=("Arial", 10, "bold"), relief="flat", padx=15).pack(side=tk.LEFT, padx=5)

# Coloca el marco de botones en la interfaz
botones.pack(pady=10)

# Barra de desplazamiento vertical para la lista de tareas
scrollbar = ttk.Scrollbar(lista_tareas, orient=tk.VERTICAL, command=lista_tareas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Configuración de eventos para interactuar con la lista de tareas
lista_tareas.bind("<Double-1>", cambiar_estado)  # Doble clic para cambiar el estado

# Inicia el bucle principal de la aplicación
try:
    app.mainloop()  # Mantiene la aplicación en ejecución hasta que se cierre
except KeyboardInterrupt:
    print("La aplicación se cerró manualmente mediante Ctrl+C.")  # Manejo de cierre con Ctrl+C