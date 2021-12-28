import tkinter as tk
from tkinter.ttk import Button, Frame, Label
from lib.scrollbar import barra_de_desplazamiento
import sys 
sys.path.append("organizador_digital/proc/")
from proc import sep_days

def interface(ventana_principal):
    # Crear subventana
    preguntas = tk.Tk()

    preguntas.title("organizador digital")

    # Crear Scrollbar
    second_frame = barra_de_desplazamiento(preguntas)
    second_frame.grid(column=0,row=0, rowspan=9)

    # Se crea etiqueta para presentar la opción de preguntas
    introduccion = tk.Label(second_frame, text = "a")

    # Crear etiquetas para preguntas
    pregunta_1 = tk.Label(second_frame, text = "    Para comenzar, ingrese su" 
                    " horario de clases del día Lunes separado por ; (Ej: 9:0"
                    "0-10:00;10:00-11:00;etc.)")
    pregunta_2 = tk.Label(second_frame, text = "Ingrese su horario de clases del" 
                    " día Martes separado por ; (Ej: 9:00-10:00;10:00-11:00;"
                    "etc.)")
    pregunta_3 = tk.Label(second_frame, text = "Ingrese su horario de clases del" 
                    " día Miércoles separado por ; (Ej: 9:00-10:00;10:00-"
                    "11:00;etc.)")
    pregunta_4 = tk.Label(second_frame, text = "Ingrese su horario de clases del día"
                    " Jueves separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")
    pregunta_5 = tk.Label(second_frame, text = "Ingrese su horario de clases del día"
                    " Viernes separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)")           
    pregunta_6 = tk.Label(second_frame, text = "Ingrese su horario de clases del día"
                    " Sábado separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)") 
    pregunta_7 = tk.Label(second_frame, text = "¿Qué días estudia? Escriba los días separado por ;"
                        " (Ej: viernes;sabado;domingo)")
    pregunta_8 = tk.Label(second_frame, text = "¿Cuantas horas le dedicas diariamente al estudio?, y" 
                        " si no es así \n ¿Cuántas horas le gustaría dedicarle"
                        " al estudio? (Siga la siguiente estructura xx:xx)")
    pregunta_9 = tk.Label(second_frame, text = "¿Juega a algún videojuego?, si es así, \n ¿Cuantas" 
                            " horas le dedica diariamente? (Siga la siguiente"
                            " estructura xx:xx)")
    pregunta_10 = tk.Label(second_frame, text = "¿Cuantas horas le dedicas a tu tiempo con tu" 
                        " familia?")
    pregunta_11 = tk.Label(second_frame, text = "¿Como te has sentido? (Escriba bien o mal)")

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
    boton_1 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_1))
    boton_2 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_2))
    boton_3 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_3))
    boton_4 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_4))
    boton_5 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_5))
    boton_6 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_6))
    boton_7 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_7))
    boton_8 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_8))
    boton_9 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_9))
    boton_10 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_10))
    boton_11 = tk.Button(second_frame, text= "Enviar", padx = 20, pady = 10, command = lambda: r_1(todas_las_respuestas,respuesta_11))

    # Se usa método grid para poner en pantalla los widgets
    introduccion.grid(row = 0, column = 0)
    pregunta_1.grid(row = 1, column = 0)
    pregunta_2.grid(row = 3, column = 0)
    pregunta_3.grid(row = 5, column = 0)
    pregunta_4.grid(row = 7, column = 0)
    pregunta_5.grid(row = 9, column = 0)
    pregunta_6.grid(row = 11, column = 0)
    pregunta_7.grid(row = 13, column = 0)
    pregunta_8.grid(row = 15, column = 0)
    pregunta_9.grid(row = 17, column = 0)
    pregunta_10.grid(row = 19, column = 0)
    pregunta_11.grid(row = 21, column = 0)
    respuesta_1.grid(row = 2, column = 0)
    respuesta_2.grid(row = 4, column = 0)
    respuesta_3.grid(row = 6, column = 0)
    respuesta_4.grid(row = 8, column = 0)
    respuesta_5.grid(row = 10, column = 0)
    respuesta_6.grid(row = 12, column = 0)
    respuesta_7.grid(row = 14, column = 0)
    respuesta_8.grid(row = 16, column = 0)
    respuesta_9.grid(row = 18, column = 0)
    respuesta_10.grid(row = 20, column = 0)
    respuesta_11.grid(row = 22, column = 0)
    boton_1.grid(row = 2, column = 1)
    boton_2.grid(row = 4, column = 1)
    boton_3.grid(row = 6, column = 1)
    boton_4.grid(row = 8, column = 1)
    boton_5.grid(row = 10, column = 1)
    boton_6.grid(row = 12, column = 1)
    boton_7.grid(row = 14, column = 1)
    boton_8.grid(row = 16, column = 1)
    boton_9.grid(row = 18, column = 1)
    boton_10.grid(row = 20, column = 1)
    boton_11.grid(row = 22, column = 1)

    # Boton para volver
    boton_volver = tk.Button(second_frame, text = "Volver al menú", padx = 20,
                             pady = 10, command = lambda: retornar
                             (ventana_principal,preguntas,todas_las_respuestas))
    # Se usa grid para poner el botón
    for i_para_etiqueta in range(1,3):
        etiqueta_vacia = Label(second_frame, text="").grid(
                        row = i_para_etiqueta + 22, column = 0)
    boton_volver.grid(row = 25, column = 1)

    # Cerrar ventana principal
    ventana_principal.withdraw()
    preguntas.mainloop()

def retornar(ventana_principal,preguntas,todas_las_respuestas):
    # Pasa todas las respuestas para ser procesadas a sep_days
    sep_days.option_1(todas_las_respuestas)
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    preguntas.destroy()


def r_1(todas_las_respuestas,respuesta):
    elemento = respuesta.get()
    todas_las_respuestas.append(elemento)
    return todas_las_respuestas
