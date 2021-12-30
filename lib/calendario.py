import tkinter as tk
from tkinter import messagebox
import data.archivos as archivos
import tkcalendar as calendar
import datetime
from lib.preguntas import retornar


# Bloque por definición
def Calendario(ventana_principal):
    """
    Esta función es la encargada de crear la subventana para el 
    calendario que tendrá acceso el usuario.
    Esta función tiene como entrada la ventana del menú, siendo
    este un dato propio de tkinter.
    """
    # Leer txt para comprobar que el archivo tenga datos o no
    lista_comprobacion = archivos.leer_archivo_2()
    if lista_comprobacion == []:
        messagebox.showerror("Error","¡Primero debes completar las"
                            " preguntas!")
    else: 
        # Crear subventana
        calendari0 = tk.Toplevel(ventana_principal)
        # Crear titulo
        calendari0.title("organizador_digital")
        
        # Obtener fecha actual
        tiempo = datetime.datetime.now()
        dia = int(tiempo.strftime("%d"))
        mes = int(tiempo.strftime("%m"))
        year = int(tiempo.strftime("%Y"))

        # Crear calendario
        cal = calendar.Calendar(calendari0, selectmode = "day", year = year, 
                                mouth = mes, day = dia)
        cal.grid(column = 0, row = 0)
        

        # Boton para volver
        boton_volver = tk.Button(calendari0, text = "Volver al menú", 
                            padx = 20, pady = 10, command = lambda: 
                             retornar(ventana_principal,calendari0))
                             
    
        # Se usa grid para poner el botón
        for i_para_etiqueta in range(1,3):
            etiqueta_vacia = tk.Label(calendari0, text="").grid(
                            row = i_para_etiqueta + 1, column = 4)
        boton_volver.grid(row = 5, column = 4)

        # Cerrar ventana principal
        ventana_principal.withdraw()


def retornar(ventana_principal,calendar):
    """
    Esta función tiene el propósito de cerrar la subventana
    y volver al menú.
    """
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    calendar.destroy()
