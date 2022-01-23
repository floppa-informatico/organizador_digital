# Bloque de importaciones
import tkinter as tk
from tkinter.ttk import Label
from lib.scrollbar import barra_de_desplazamiento
from proc.sep_days import option_1
from tkinter import messagebox


# Bloque de definiciones
# Bloque de definición de funciones


def interface(ventana_principal):
    """
    Esta función tiene la función de mostar la ventana de las preguntas
    que se la hara al usuario. Tiene como entrada la ventana del menú,
    siendo este dato propio del módulo de tkinter.
    """
    # Crear subventana
    preguntas = tk.Toplevel(ventana_principal)

    # Crear titulo
    preguntas.title("organizador digital")

    # Crear Scrollbar
    second_frame = barra_de_desplazamiento(preguntas)
    second_frame.grid(column=0, row=0, rowspan=9)

    # Se crea etiqueta para presentar la opción de preguntas
    introduccion = tk.Label(second_frame, text="Bienvenid@ a la sección de"
                            " preguntas. Para obtener un horario 100%"
                            " adaptado a sus necesidades\ndebe responder"
                            " estas preguntas. Siga cuidadosamente la"
                            " estructura pedida en cada pregunta. En\n"
                            "aquellas preguntas en donde debe ingresar más de"
                            " un dato, debe ir separado con “;”, sin que esta"
                            "\nquede al final (ejemplo: 9:00-10:00;"
                            "11:00:12:00 ). Además procure que las horas"
                            " esten en formato\n24 horas. Cada vez que"
                            " responda a una pregunta pulse el botón de"
                            " enviar.\n Una vez que haya respondido todos las"
                            " preguntas, pulsando su respectivo botón, ya"
                            " puede\nvolver al menú pulsando en el botón"
                            " correspondiente.\nNote que si el numero lleva"
                            " un cero adelante, debe omitirlo. (ej: escribir"
                            " las nueve en punto\n de esta manera 9:00, no de"
                            " esta manera 09:00).")

    # Crear etiquetas para preguntas
    # Entrada
    pregunta_1 = tk.Label(
        second_frame,
        text="    Para comenzar, ingrese su horario de clases del"
        " día Lunes separado por ; (Ej: 9:00-10:00;10:00-11:00;"
        "etc.)")
    pregunta_2 = tk.Label(
        second_frame,
        text="Ingrese su horario de clases del día Martes"
        " separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_3 = tk.Label(
        second_frame,
        text="Ingrese su horario de clases del día Miércoles"
        " separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_4 = tk.Label(
        second_frame,
        text="Ingrese su horario de clases del día Jueves"
        " separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_5 = tk.Label(
        second_frame,
        text="Ingrese su horario de clases del día Viernes"
        " separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_6 = tk.Label(
        second_frame,
        text="Ingrese su horario de clases del día Sábado"
        " separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_7 = tk.Label(
        second_frame,
        text="¿Qué días estudia? Escriba los días separado por ;"
        " (Ej: viernes;sabado;domingo)")
    pregunta_8 = tk.Label(
        second_frame,
        text="¿Cuantas horas le dedicas diariamente al estudio?,"
        " y si no es así \n ¿Cuántas horas le gustaría dedicarle"
        " al estudio? (Siga la siguiente estructura xx:xx)")
    pregunta_9 = tk.Label(
        second_frame,
        text="Si tiene algún ocio, ¿Cuantas horas le dedica?"
        " (Siga la siguiente estructura xx:xx)")
    pregunta_10 = tk.Label(
        second_frame,
        text="¿Cuantas horas le dedicas a tu tiempo con tu"
        " familia? (Siga la siguiente estructura xx:xx)")
    pregunta_11 = tk.Label(
        second_frame,
        text="¿Como te has sentido? (Escriba bien o mal)")

    # Procesamiento
    # Entrada para introducir texto
    respuesta_1 = tk.Entry(second_frame)
    respuesta_2 = tk.Entry(second_frame)
    respuesta_3 = tk.Entry(second_frame)
    respuesta_4 = tk.Entry(second_frame)
    respuesta_5 = tk.Entry(second_frame)
    respuesta_6 = tk.Entry(second_frame)
    respuesta_7 = tk.Entry(second_frame)
    respuesta_8 = tk.Entry(second_frame)
    respuesta_9 = tk.Entry(second_frame)
    respuesta_10 = tk.Entry(second_frame)
    respuesta_11 = tk.Entry(second_frame)

    # Se usa método grid para poner en pantalla los widgets
    introduccion.grid(row=0, column=0)
    pregunta_1.grid(row=3, column=0)
    pregunta_2.grid(row=5, column=0)
    pregunta_3.grid(row=7, column=0)
    pregunta_4.grid(row=9, column=0)
    pregunta_5.grid(row=11, column=0)
    pregunta_6.grid(row=13, column=0)
    pregunta_7.grid(row=15, column=0)
    pregunta_8.grid(row=17, column=0)
    pregunta_9.grid(row=19, column=0)
    pregunta_10.grid(row=21, column=0)
    pregunta_11.grid(row=23, column=0)
    respuesta_1.grid(row=4, column=0)
    respuesta_2.grid(row=6, column=0)
    respuesta_3.grid(row=8, column=0)
    respuesta_4.grid(row=10, column=0)
    respuesta_5.grid(row=12, column=0)
    respuesta_6.grid(row=14, column=0)
    respuesta_7.grid(row=16, column=0)
    respuesta_8.grid(row=18, column=0)
    respuesta_9.grid(row=20, column=0)
    respuesta_10.grid(row=22, column=0)
    respuesta_11.grid(row=24, column=0)

    # Boton para volver
    boton_volver = tk.Button(
        second_frame,
        text="Volver al menú",
        padx=20,
        pady=10,
        command=lambda:
        retornar(
            ventana_principal, preguntas,
            respuesta_1,
            respuesta_2,
            respuesta_3,
            respuesta_4,
            respuesta_5,
            respuesta_6,
            respuesta_7,
            respuesta_8,
            respuesta_9,
            respuesta_10,
            respuesta_11)
    )
    # Se usa grid para poner el botón
    for i_para_etiqueta in range(1, 3):
        etiqueta_vacia = Label(second_frame, text="").grid(
            row=i_para_etiqueta + 22, column=0)
    boton_volver.grid(row=25, column=1)

    for i_para_etiqueta_2 in range(1, 3):
        etiqueta_vacia_2 = Label(second_frame, text="").grid(
            row=i_para_etiqueta, column=0)

    # Cerrar ventana principal
    ventana_principal.withdraw()


def retornar(
        ventana_principal,
        preguntas,
        respuesta_1,
        respuesta_2,
        respuesta_3,
        respuesta_4,
        respuesta_5,
        respuesta_6,
        respuesta_7,
        respuesta_8,
        respuesta_9,
        respuesta_10,
        respuesta_11
):
    """
    Esta función se encarga de cerrar la ventana de las preguntas para
    retornas al menú principal, así también verificando que todas las
    preguntas hayan sido contestadas.
    Esta función tiene como entrada la ventana del menú principal,
    también la ventana de las preguntas, siendo estos dos ultimos datos
    propios de tkinter, también la respuesta al widget "Entry" llamada
    "respuesta_x" siendo x el número de cualquiera de las 11 preguntas,
    no es posible meterlos todos a una lista, debido que al obtener la
    respuesta da error.
    Esta funcion también se encarga se obtener todas las respuestas y
    poder pasarlo de un tipo de dato propio de tkinter a un string,
    además de un primer filtro si es que los datos corresponde a la
    estructura que se pide.
    Además esta función en caso de que hayan sido contestadas todas las
    preguntas se ejecuta la función option_1 del archivo sep_days.py
    para poder trabajar los datos.
    """

    todas_las_respuestas = []
    elemento_1 = respuesta_1.get()
    elemento_2 = respuesta_2.get()
    elemento_3 = respuesta_3.get()
    elemento_4 = respuesta_4.get()
    elemento_5 = respuesta_5.get()
    elemento_6 = respuesta_6.get()
    elemento_7 = respuesta_7.get()
    elemento_8 = respuesta_8.get()
    elemento_9 = respuesta_9.get()
    elemento_10 = respuesta_10.get()
    elemento_11 = respuesta_11.get()
    todas_las_respuestas.extend([
        elemento_1,
        elemento_2,
        elemento_3,
        elemento_4,
        elemento_5,
        elemento_6,
        elemento_7,
        elemento_8,
        elemento_9,
        elemento_10,
        elemento_11])

    contador_0 = 0
    respuestas_no_vacias = True
    for elemento in todas_las_respuestas:
        if elemento == "" or elemento == " ":
            contador_0 += 1
        if contador_0 == len(todas_las_respuestas):
            respuesta_vacio = messagebox.askquestion(
                "Advertencia",
                "No ha completado todas las preguntas,"
                " ¿Quiere salir de todas formas?")
            if respuesta_vacio == "yes":
                respuestas_no_vacias = False
                respuesta_salida = "salir"
            if respuesta_vacio == "no":
                respuestas_no_vacias = False

    if respuestas_no_vacias:
        contador_de_errores = 0
        for i in range(len(todas_las_respuestas)):
            elemento = todas_las_respuestas[i]
            if elemento == "" or elemento == " ":
                messagebox.showerror(
                    "Error",
                    f"¡El espacio está vacío en la pregunta {i + 1}!")
                contador_de_errores += 1
            elif elemento[0] == " ":
                messagebox.showerror(
                    "Error",
                    f"¡Hay un espacio al inicio en la pregunta {i + 1}")
                contador_de_errores += 1
                if elemento[-1] == " ":
                    messagebox.showerror(
                        "Error",
                        f"¡Hay un espacio al final en la pregunta {i + 1}!")
                    contador_de_errores += 1
            elif elemento[-1] == " ":
                messagebox.showerror(
                    "Error",
                    f"¡Hay un espacio al final en la pregunta {i + 1}!")
                contador_de_errores += 1

        # Pasa todas las respuestas para ser procesadas a sep_days
        if contador_de_errores == 0:
            # Pasa todas las respuestas del usuario para ser procesadas
            errores = option_1(todas_las_respuestas)
            if errores == 0:
                # Vuelve a abrir la ventana principal
                ventana_principal.deiconify()
                # Cierra la subventana
                preguntas.destroy()
            else:
                todas_las_respuestas = []
        else:
            todas_las_respuestas = []

    elif respuesta_salida == "salir":
        # Vuelve a abrir la ventana principal
        ventana_principal.deiconify()
        # Cierra la subventana
        preguntas.destroy()
