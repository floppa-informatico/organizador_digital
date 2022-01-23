import tkinter as tk
from tkinter import messagebox
import os
from data.xlsx import escribir_xlsx


# Bloque de definiciones


def Sientes(ventana_principal):
    """
    Esta función es la encargada de crear la subventana para la
    sección "¿como te sientes?" que tendrá acceso el usuario.
    Esta función tiene como entrada la ventana del menú, siendo
    este un dato propio de tkinter.
    """
    # Leer txt para comprobar que el archivo tenga datos o no
    if not(os.path.exists("./data/datos.txt")
           and os.path.exists("./data/datos.xlsx")):
        messagebox.showerror(
            "Error", "¡Primero debes completar las preguntas!")
    else:
        # Se declara la variable respuesta_0 en caso de que el usuario no
        # escriba nada
        # Crear subventana
        sentir_ventana = tk.Toplevel(ventana_principal)
        # Crear titulo
        sentir_ventana.title("organizador_digital")

        # Crear etiqueta para pregunta
        pregunta_0 = tk.Label(
            sentir_ventana,
            text="¿Como te has sentido? (Escriba bien o mal)")

        # Entrada para introducir texto
        respuesta_0 = tk.Entry(sentir_ventana)

        # Poner los widgets en pantalla
        pregunta_0.grid(column=0, row=0)
        respuesta_0.grid(column=0, row=1)

        # Boton para volver
        for i_para_etiqueta in range(1, 3):
            etiqueta_vacia = tk.Label(sentir_ventana, text="").grid(
                row=i_para_etiqueta + 2, column=1)

        boton_volver = tk.Button(
            sentir_ventana,
            text="Volver al menú",
            padx=20, pady=10,
            command=lambda:
            retornar(
                ventana_principal,
                sentir_ventana,
                respuesta_0
            )
        )
        boton_volver.grid(row=5, column=1)

        # Cerrar ventana principal
        ventana_principal.withdraw()


def retornar(ventana_principal, sentir_ventana, respuesta_0):
    """
    Esta funcion tiene el propósito de cerrar la subventana
    y volver al menu.
    """
    respuesta = respuesta_0.get()
    # Verifica si la respuesta del usuario es la respuesta que se pide
    final = False
    if respuesta.lower() == "bien" or respuesta.lower() == "mal":
        final = True

    if final:
        # Si es "bien" o "mal", entonces la introduccion de datos ha
        # sido exitoso.
        messagebox.showinfo("Ha sido un éxito", "Has introducido el dato"
                            " correctamente")
        # Se escribe la nueva respuesta
        with open("./data/datos.txt", "r") as archivo:
            respuestas = []
            for linea in archivo:
                respuestas.append(linea)
            # Dejar todas las lineas en su respectiva variable
            dias_especificos = eval(respuestas[0])
            dias_con_horas = eval(respuestas[1])
            semana_horario = eval(respuestas[-2])
            estado_animico = respuesta
        with open("./data/datos.txt", "w") as archivo:
            archivo.write(str(dias_especificos))
            archivo.write("\n")
            archivo.write(str(dias_con_horas))
            archivo.write("\n")
            archivo.write(str(semana_horario))
            archivo.write("\n")
            archivo.write(str(estado_animico))
        # Se ajusta el horario
        escribir_xlsx()
        # Vuelve a abrir la ventana principal
        ventana_principal.deiconify()
        # Cierra la subventana
        sentir_ventana.destroy()
    else:
        # Informa al usuario que no siguió la estructura propuesta.
        if respuesta == "":
            respuesta = messagebox.askquestion(
                "Advertencia",
                "No ha completado la pregunta, ¿Quieres salir?")
            if respuesta == "yes":
                # Vuelve a abrir la ventana principal
                ventana_principal.deiconify()
                # Cierra la subventana
                sentir_ventana.destroy()
        elif respuesta[0] == " ":
            messagebox.showerror(
                "Error",
                "¡Hay un espacio al inicio en la respuesta!")
            if respuesta[-1] == " ":
                messagebox.showerror(
                    "Error",
                    "¡Hay un espacio al final en la respuesta!")
        elif respuesta[-1] == " ":
            messagebox.showerror(
                "Error",
                "¡Hay un espacio al final en la respuesta!")
        else:
            messagebox.showerror(
                "Error",
                "No escribiste una respuesta"
                " acorde a la pregunta :(")
