import tkinter as tk
from tkinter import messagebox

# Función para calcular las horas extras totales
def calcular_total():
    total_horas = 0
    try:
        for entrada in entradas:
            horas = float(entrada.get())
            if horas < 0:
                raise ValueError("Horas no pueden ser negativas.")
            total_horas += horas
        resultado.set(f"Total de horas extras: {total_horas}")
    except ValueError:
        messagebox.showerror("Error", "Introduce solo números válidos y no negativos.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cálculo de Horas Extras")

# Establecer tamaño de la ventana para albergar las dos columnas
ventana.geometry("900x700")  # Ajusta el tamaño según el contenido que desees mostrar

# Crear un frame contenedor para poder agregar el scroll
contenedor = tk.Frame(ventana)
contenedor.pack(fill="both", expand=True)

# Crear el canvas donde estarán los widgets y un scrollbar
canvas = tk.Canvas(contenedor)
scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Configurar la barra de desplazamiento
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Crear una lista para almacenar las entradas de cada día
entradas = []
for dia in range(1, 32):
    # Determinar la fila y columna (dos columnas: una para los días 1-15, otra para 16-30)
    fila = (dia - 1) % 15  # Filas de 0 a 14
    columna = (dia - 1) // 15  # Primera columna (0) para los días 1-15, segunda columna (1) para 16-30
    
    # Crear una etiqueta para el día
    etiqueta = tk.Label(scrollable_frame, text=f"Día {dia}:")
    etiqueta.grid(row=fila, column=columna * 2, padx=10, pady=5)
    
    # Crear un campo de entrada para las horas de ese día
    entrada = tk.Entry(scrollable_frame)
    entrada.grid(row=fila, column=columna * 2 + 1, padx=10, pady=5)
    entradas.append(entrada)

# Botón para calcular el total de horas extras
boton_calcular = tk.Button(scrollable_frame, text="Calcular Total", command=calcular_total)
boton_calcular.grid(row=15, column=0, columnspan=4, pady=20)  # Ocupa las 4 columnas

# Etiqueta para mostrar el resultado
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(scrollable_frame, textvariable=resultado)
etiqueta_resultado.grid(row=16, column=0, columnspan=4)


# Empaquetar scrollbar y canvas
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")



# Ejecutar la ventana
ventana.mainloop()
