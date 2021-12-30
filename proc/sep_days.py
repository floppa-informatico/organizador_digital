import sys 
from proc.verificador import Verificador
from tkinter import messagebox
import data.archivos as archivos 


def weekly_time(answer,i):
    """
    Esta función se encarga de dejar todas las respuestas relacionadas
    al tiempo semanal en una sola lista para así poder trabajarlas 
    durante el largo del código. El tiempo es separado en horas y
    minutos, además que queda separado por día.
    """
    answers = []
    day = []
    answers_1 = answer[i]
    answers_1 = answers_1.split(";")
    # Se usa un iterador for para separar terminos según su posición
    # dentro de la lista.
    for j in range(len(answers_1)):
        temp = answers_1[j]
        temp = temp.split("-")
        temp_1 = temp[0]
        temp_1_1 = temp_1.split(":")
        temp_1_1[0] = int(temp_1_1[0])
        temp_1_1[1] = int(temp_1_1[1])
        day.append(temp_1_1)
        temp_2 = temp[1]
        temp_2_1 = temp_2.split(":")
        temp_2_1[0] = int(temp_2_1[0])
        temp_2_1[1] = int(temp_2_1[1])
        day.append(temp_2_1)
    # Agrega los horarios de un solo día al listado de horarios por día
    answers.append(day)
    return answers


def daily_time(answer,f):
    """
    Esta función se encarga de separar las horas de los minutos de los
    tiempos especificados como actividades diarias. Para de esta manera
    poder trabajar con estos datos durante el programa.
    """
    answer_1 = answer[f]
    answer_1 = answer_1.split(":")
    for j in range(2):
        answer_1[j] = int(answer_1[j])
    return answer_1


def s_days(answer):
    """
    Esta función se ocupa de separar los días de la pregunta 5 para así
    poder trabajarlos de mejorar manera durante el programa.
    """
    answer_1 = answer[6]
    answer_1 = answer_1.split(";")
    return answer_1


def option_1(answer):
    """
    Esta función es la función para la primera opción que se encarga de
    hacerle las preguntas correspondientes al usuario, para luego
    de manera interna pueda hacer el horario para el usuario totalmente
    adapto a él. El usuario podra ver el horario en la opción 2.
    """
    if Verificador(answer):
        days = []
        day = []
        # Separa las horas de los minutos según mes o día
        for i in range(6):
            time_temp = weekly_time(answer,i)
            days.append(time_temp)
        for f in range(7,10):
            time_temp = daily_time(answer,f)
            day.append(time_temp)
        # Separa los días
        study_days = s_days(answer)
        # Informa al usuario que ha introducido bien los datos
        messagebox.showinfo("Ha sido un éxito","Has introducido los datos correctamente")
        archivos.escribir_archivo(study_days,day,days)
    else:
        # Informa al usuario que no siguió la estructura propuesta.
        messagebox.showerror("Error","Los datos que introduciste no cumplen la estructura planteada")
