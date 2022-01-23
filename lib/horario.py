# Bloque de importaciones
import tkinter as tk
from tkinter import messagebox, ttk
import os
import pandas as pd


# Bloque de definiciones
# Bloque de definición de funciones


def tabla(ventana_principal):
    """
    Esta función es la encargada de crear la subventana para el
    horario que tendrá acceso el usuario.
    Esta función tiene como entrada la ventana del menú, siendo
    este un dato propio de tkinter.
    """
    # Leer txt para comprobar que el archivo tenga datos o no
    if not(os.path.exists("./data/datos.txt")
           and os.path.exists("./data/datos.xlsx")):
        messagebox.showerror(
            "Error", "¡Primero debes completar las preguntas!")
    else:
        # Crear subventana
        organizacion = tk.Toplevel(ventana_principal)
        # Crear titulo
        organizacion.title("organizador_digital")

        # Creamos un frame donde se pondrán todos los widgets.
        marco = tk.Frame(organizacion)
        marco.grid(row=1, column=0, pady=20)
        # Creamos el treeview en donde se pondrán los datos del .xlsx
        arbol = ttk.Treeview(marco)
        # Leemos datos.xlsx
        df = pd.read_excel("./data/datos.xlsx")
        # Se elimina el treeview antiguo en caso de existir
        arbol.delete(*arbol.get_children())
        # Se imprime en la ventana el nuevo treeview
        arbol["column"] = list(df.columns)
        arbol["show"] = "headings"
        # Se recorre la lista de columnas de encabezado
        for columna in arbol["column"]:
            arbol.heading(columna, text=columna)

        # Poner los datos en el treeview
        df_filas = df.to_numpy().tolist()
        for fila in df_filas:
            arbol.insert("", "end", values=fila)

        # Se pone el treeview en pantalla
        arbol.pack()

        # Boton para volver
        boton_volver = tk.Button(
            organizacion,
            text="Volver al menú", padx=20, pady=10,
            command=lambda:
            retornar(ventana_principal, organizacion))

        for i_para_etiqueta in range(1, 3):
            etiqueta_vacia = tk.Label(organizacion, text="").grid(
                row=i_para_etiqueta + 22, column=0)

        boton_volver.grid(row=4, column=1, pady=20)

        # Cerrar ventana principal
        ventana_principal.withdraw()


def retornar(ventana_principal, organizacion):
    """
    Esta función tiene el propósito de cerrar la subventana
    y volver al menú.
    """
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    organizacion.destroy()
