import tkinter as tk
from tkinter.ttk import Button, Frame, Label
from lib.scrollbar import barra_de_desplazamiento
from proc.sep_days import option_1
from tkinter import messagebox
import data.archivos as archivos


# Bloque por definición
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
                            "11:00:12:00 ). Cada vez que responda a una"
                            " pregunta\npulse el botón de enviar. Una vez que"
                            " haya respondido todos las preguntas, pulsando"
                            " su\nrespectivo botón, ya puede volver al menú"
                            " pulsando en el botón correspondiente.")

    # Crear etiquetas para preguntas
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

    # Boton para introducir texto
    todas_las_respuestas = []
    boton_1 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_1))
    boton_2 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_2))
    boton_3 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_3))
    boton_4 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_4))
    boton_5 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_5))
    boton_6 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_6))
    boton_7 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_7))
    boton_8 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_8))
    boton_9 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_9))
    boton_10 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_10))
    boton_11 = tk.Button(
                    second_frame,
                    text="Enviar", padx=20, pady=10, command=lambda:
                    r_1(todas_las_respuestas, respuesta_11))

    # Se usa método grid para poner en pantalla los widgets
    introduccion.grid(row=0, column=0)
    pregunta_1.grid(row=1, column=0)
    pregunta_2.grid(row=3, column=0)
    pregunta_3.grid(row=5, column=0)
    pregunta_4.grid(row=7, column=0)
    pregunta_5.grid(row=9, column=0)
    pregunta_6.grid(row=11, column=0)
    pregunta_7.grid(row=13, column=0)
    pregunta_8.grid(row=15, column=0)
    pregunta_9.grid(row=17, column=0)
    pregunta_10.grid(row=19, column=0)
    pregunta_11.grid(row=21, column=0)
    respuesta_1.grid(row=2, column=0)
    respuesta_2.grid(row=4, column=0)
    respuesta_3.grid(row=6, column=0)
    respuesta_4.grid(row=8, column=0)
    respuesta_5.grid(row=10, column=0)
    respuesta_6.grid(row=12, column=0)
    respuesta_7.grid(row=14, column=0)
    respuesta_8.grid(row=16, column=0)
    respuesta_9.grid(row=18, column=0)
    respuesta_10.grid(row=20, column=0)
    respuesta_11.grid(row=22, column=0)
    boton_1.grid(row=2, column=1)
    boton_2.grid(row=4, column=1)
    boton_3.grid(row=6, column=1)
    boton_4.grid(row=8, column=1)
    boton_5.grid(row=10, column=1)
    boton_6.grid(row=12, column=1)
    boton_7.grid(row=14, column=1)
    boton_8.grid(row=16, column=1)
    boton_9.grid(row=18, column=1)
    boton_10.grid(row=20, column=1)
    boton_11.grid(row=22, column=1)

    # Boton para volver
    boton_volver = tk.Button(
                            second_frame,
                            text="Volver al menú",
                            padx=20,
                            pady=10,
                            command=lambda:
                            retornar(
                                ventana_principal, preguntas,
                                todas_las_respuestas)
                            )
    # Se usa grid para poner el botón
    for i_para_etiqueta in range(1, 3):
        etiqueta_vacia = Label(second_frame, text="").grid(
                        row=i_para_etiqueta + 22, column=0)
    boton_volver.grid(row=25, column=1)

    # Cerrar ventana principal
    ventana_principal.withdraw()


def retornar(ventana_principal, preguntas, todas_las_respuestas):
    """
    Esta función se encarga de cerrar la ventana de las preguntas para
    retornas al menú principal, así también verificando que todas las
    preguntas hayan sido contestadas.
    Esta función tiene como entrada la ventana del menú principal,
    también la ventana de las preguntas, siendo estos dos ultimos datos
    propios de tkinter.
    Además esta función en caso de que hayan sido contestadas todas las
    preguntas se ejecuta la función option_1 del archivo sep_days.py
    para poder trabajar los datos.
    """
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    preguntas.destroy()
    # Pasa todas las respuestas para ser procesadas a sep_days
    if len(todas_las_respuestas) == 11:
        # Borra el txt existente
        archivos.borrar_archivo()
        # Pasa todas las respuestas del usuario para ser procesadas
        option_1(todas_las_respuestas)
    else:
        messagebox.showwarning(
                            "Advertencia",
                            "No ha completado todas las preguntas")


def r_1(todas_las_respuestas, respuesta):
    """
    Esta funcion se encarga se obtener todas las respuestas y poder
    pasarlo de un tipo de dato propio de tkinter a un string, además
    de un primer filtro si es que los datos corresponde a la estructura
    que se pide.
    Esta función tiene como entrada la lista en un principio vacía que
    en caso de cumplir con este primer filtro es agregada a la lista,
    también la respuesta al widget "Entry" llamada "respuesta".
    Esta función tiene como salida la lista "todas_las_respuestas"
    siendo este de tipo list, en donde se agrega el elemento si es que
    cumple con lo ya mencionado.
    """
    # Se obtiene la respuesta y lo pasa a string
    elemento = respuesta.get()
    # Clasifica si es que lo que ingresó el usuario corresponde en una
    # primera instancia a lo pedido
    if elemento == "" or elemento == " ":
        messagebox.showerror("Error", "¡Es espacio está vacío!")
    elif elemento[0] == " " and elemento[1] != " ":
        messagebox.showerror("Error", "¡Hay un espacio al inicio!")
    else:
        # Si cumple, se agrega a la lista y se retorna a la funcion
        # interface
        todas_las_respuestas.append(elemento)
        return todas_las_respuestas
