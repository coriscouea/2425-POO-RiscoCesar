"""
Aplicación de Lista de Tareas con Interfaz Gráfica

Este programa permite gestionar una lista de tareas con las siguientes funcionalidades:
- Añadir nuevas tareas
- Marcar tareas como completadas/pendientes
- Eliminar tareas
- Interfaz intuitiva con botones y atajos de teclado

Módulos utilizados:
- tkinter: Para la interfaz gráfica
- ttk: Para widgets temáticos
- messagebox: Para mostrar mensajes al usuario
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# ==============================================
# FUNCIONES PRINCIPALES DE LA APLICACIÓN
# ==============================================

def agregar_tarea(event=None):
    """
    Agrega una nueva tarea a la lista.

    Parámetros:
    event: Objeto de evento (opcional, para el enlace de teclas)
    """
    tarea = entrada_entry.get().strip()

    if tarea:
        # Añadir a la tabla con estado inicial "Pendiente"
        treeview.insert('', tk.END, values=(tarea,"Pendiente"), tags=('Pendiente',))

        # Limpiar el campo de entrada
        entrada_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor ingrese una tarea.")

    # Devolver el foco al campo de entrada
    entrada_entry.focus()

def Cambiar_Estado():
    """Marca la tarea seleccionada como completada"""
    seleccion = treeview.selection()

    if seleccion:
        item = seleccion[0]
        valores = treeview.item(item, "values")
        tarea = valores[0]

        # Alternar entre estados
        nuevo_estado = "Completada" if valores[1] == "Pendiente" else "Pendiente"

        # Actualizar el Treeview
        treeview.item(item, values=(tarea, nuevo_estado), tags=(nuevo_estado,))

    else:
        messagebox.showinfo("Información", "Por favor selecciona una tarea.")

def eliminar_tarea():
    """Elimina la tarea seleccionada"""
    seleccion = treeview.selection()

    if seleccion:
        confirmar= messagebox.askyesno("Confirmar", "¿Eliminar la tarea seleccionada?")
        for item in seleccion:
            treeview.delete(item)
    else:
        messagebox.showinfo("Información", "Por favor selecciona una tarea.")

def doble_clic_tarea(event):
    """Maneja el evento de doble clic en una tarea"""
    Cambiar_Estado()

# ==============================================
# CONFIGURACIÓN DE LA INTERFAZ GRÁFICA
# ==============================================

# Configuración de la ventana principal
aplicacion = tk.Tk()
aplicacion.title("Aplicación GUI")
aplicacion.geometry("800x600")
aplicacion.configure(bg='#f0f0f0')

# Configuración del estilo visual
estilo = ttk.Style()
estilo.theme_use("clam")

# ==============================================
# COMPONENTES DE LA INTERFAZ
# ==============================================

#Título Principal
titulo = tk.Label(aplicacion, text="Lista de Tareas UEA - 2025", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# Marco para la entrada de tareas
marco_entrada = tk.Frame(aplicacion)
marco_entrada.pack(pady=10, fill=tk.X, padx=20)

# Etiqueta y campo de entrada
etiqueta_tarea = tk.Label(marco_entrada,text="Nueva Tarea:",font=("Arial", 11),bg='#f0f0f0')
etiqueta_tarea.pack(side="left")

entrada_entry = tk.Entry(marco_entrada, font=('Arial',11),width=40, relief="solid", borderwidth=1)
entrada_entry.pack(side="left", padx=10,fill="x", expand=True)
entrada_entry.focus()

# Tabla para mostrar las tareas
treeview = ttk.Treeview(aplicacion, columns=('tarea', 'estado'), show='headings', style="Treeview")
treeview.tag_configure("Pendiente", background="#fff3cd", foreground="#856404")
treeview.tag_configure("Completada", background="#d4edda", foreground="#155724")

# Configurar las columnas
treeview.heading('tarea', text='Tarea')
treeview.heading('estado', text='Estado')
treeview.column('tarea', width=500)
treeview.column('estado', width=100, anchor='center')

# Posicionar la tabla y la barra de desplazamiento
treeview.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# ==============================================
# BOTONES DE LA APLICACIÓN
# ==============================================

# Marco para los botones
marco_botones = tk.Frame(aplicacion,bg='#f0f0f0')
marco_botones.pack(pady=10,padx=20, fill="x")

# Botón de agregar tarea
boton_agregar = tk.Button(marco_entrada, text="➕Añadir Tarea", command=agregar_tarea,bg="#4CAF50",fg="white",font=("Arial", 10, "bold"),relief="flat",padx=15)
boton_agregar.pack(side=tk.LEFT)

# Botones de Acción
boton_completar = tk.Button(marco_botones, text="✓ Cambiar de Estado", command=Cambiar_Estado,bg="#2196F3",fg="white",font=("Arial", 10, "bold"),relief="flat",padx=15, )
boton_completar.pack(side=tk.LEFT, padx=5)

boton_eliminar = tk.Button(marco_botones, text="x Eliminar", bg="#f44336", fg='white', command=eliminar_tarea, font=("Arial", 10, "bold"), relief="flat", padx=15,)
boton_eliminar.pack(side=tk.LEFT, padx=5)

# ==============================================
# CONFIGURACIÓN FINAL
# ==============================================

# Barra de desplazamiento
scrollbar = ttk.Scrollbar(treeview, orient=tk.VERTICAL, command=treeview.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Evento de doble clic para marcar como completada
treeview.bind('<Double-1>', doble_clic_tarea)

# Vincular la tecla Enter al campo entrada
entrada_entry.bind('<Return>', agregar_tarea)

# Etiqueta de Instrucciones
instruciones = tk.Label(aplicacion,text="Presiona Enter para añadir tareas o doble clic para cambiar estado.",font=("Arial", 9, "italic"),bg='#f0f0f0')
instruciones.pack(pady=5)

# Iniciar el bucle principal de la aplicación
aplicacion.mainloop()