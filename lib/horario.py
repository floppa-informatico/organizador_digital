import tkinter as tk
import sys
sys.path.append("/data/")
from data import archivos


def tabla(ventana_principal):
    # Crear subventana
    organizacion = tk.Toplevel(ventana_principal)
    # Crear titulo
    organizacion.title("organizador_digital")

    # Leer txt
    study_days,day,days = archivos.leer_archivo()

    # Transformar a lista para poder trabajar
    study_days = eval(study_days)
    day = eval(day)
    days = eval(days)

    # Boton para volver
    boton_volver = tk.Button(organizacion, text = "Volver al menú", padx = 20,
                             pady = 10, command = lambda: retornar
                             (ventana_principal,organizacion))
    boton_volver.grid(row = 0, column = 0)

    # Cerrar ventana principal
    ventana_principal.withdraw()


def retornar(ventana_principal,organizacion):
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    organizacion.destroy()
