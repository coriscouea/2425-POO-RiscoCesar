# Importar las bibliotecas necesarias de tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import LabelFrame

# Definir la clase principal de la aplicación
class MyApp:
    def __init__(self, recuadro):
        # Configuración básica de la ventana principal
        self.recuadro = recuadro
        self.recuadro.title("Api de Dialogo") # Título de la ventana principal
        self.recuadro.geometry("550x350") # Dimensiones de la ventana
        self.recuadro.config(bg="grey") # Color de fondo de la ventana

        # Crear y configurar una etiqueta (Label) para instrucciones
        self.Etiqueta = tk.Label(recuadro, text="Ingresa los Datos", bg="white", fg="blue", justify="left")
        self.Etiqueta.config(width=20)
        self.Etiqueta.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # sticky="w" alinea a la izquierda
        # Posicionar la etiqueta en la ventana con el método grid

        # Crear un campo de entrada (Entry) para que el usuario pueda ingresar datos
        self.entrada = tk.Entry(recuadro)
        self.entrada.config(width=30)
        self.entrada.grid(row=0, column=1, padx=10, pady=10, sticky="e")  # sticky="e" alinea a la derecha
        # Posicionar el campo de entrada a la derecha de la etiqueta

        # Crear un botón "Agregar" para insertar datos en la lista
        self.Button_agregar = tk.Button(recuadro, text="Agregar", bg="white", fg="Green",command=self.ingresar_datos)
        self.Button_agregar.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        # Posicionar el botón debajo de la etiqueta

        # Crear un botón "Limpiar" para borrar datos de la lista y el campo de entrada
        self.button_limpiar = tk.Button(recuadro, text="Limpiar", bg="white", fg="Red", command=self.quitar_palabra_ingresada)
        self.button_limpiar.grid(row=1, column=1, padx=10, pady=10)
        # Posicionar el botón al lado del botón "Agregar"

        # Crear un marco (LabelFrame) con el título "RESULTADO"
        self.marco_resultado = LabelFrame(recuadro, text="RESULTADO", bg="grey", fg="white", font=("Arial", 15, "bold"))
        self.marco_resultado.config(width=400, height=400) # Configurar el tamaño del marco
        self.marco_resultado.grid(row=2, column=0, columnspan=2,padx=10, pady=5, sticky="w")
        # Posicionar el marco en la ventana

        # Crear una lista (Listbox) dentro del marco para mostrar los datos ingresados
        self.lista = tk.Listbox(self.marco_resultado,height=5, width=50) # Posicionar la lista dentro del marco
        self.lista.pack(padx=10, pady=10)

    # Función para agregar datos desde el campo de entrada a la lista
    def ingresar_datos(self):
        # Obtener el texto ingresado por el usuario en el campo de entrada.
        palabra = self.entrada.get()

        if palabra:
            # Verificar si el campo de texto no está vacío.
            self.lista.insert(tk.END, palabra)
            # Agregar la palabra ingresada al final de la lista.
            self.entrada.delete(0, tk.END)
            # Limpiar el campo de texto para que quede listo para la próxima entrada.
        else:
            messagebox.showwarning("Advertencia", "Por favor ingrese un dato válido.")
            # Mostrar una advertencia al usuario si intenta agregar un texto vacío.
        print("Gracias por usar la Api de Dialogo")

    # Función para limpiar el campo de entrada y borrar todos los elementos de la lista
    def quitar_palabra_ingresada(self):
        # Limpiar el campo de entrada, eliminando cualquier texto presente.
        self.entrada.delete(0, tk.END)
        # Borrar todos los elementos dentro de la lista (Listbox).
        self.lista.delete(0, tk.END)

# Código principal para inicializar la aplicación
if __name__ =="__main__":
    recuadro = tk.Tk()   # Crear la ventana principal
    MyApp(recuadro)      # Instanciar la clase MyApp
    recuadro.mainloop()  # Iniciar el bucle principal de la aplicación


