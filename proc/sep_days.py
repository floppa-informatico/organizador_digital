from proc.verificador import Verificador
from tkinter import messagebox
import data.archivos as archivos


# Bloque por definición
def weekly_time(answer, i):
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


def lista_sobrante(days):
    """
    Esta funcion tiene el proposito de eliminar una lista extra que se
    nos genera al separar las horas y los minutos en caso de los días
    de la semana.
    Como entrada tiene la lista ya separada, siendo este de tipo list.
    Como salida tiene esta lista sin esta lista extra siendo de tipo
    list.
    """
    for i in range(len(days)):
        # Se verifica la condicional si es que hay una lista sobrante
        # en donde solo hay un elemento, y no así conteniendo de manera
        # innecesaria el resto de elementos. (ej: [[[[9, 0],[10, 0]]]])
        if len(days[i]) == 1 and len(days[i][0]) != 1:
            temp = []
            # Se agrega a una lista temporal en donde se agregan todos
            # los elementos que está dentro de la lista que realmente
            # tiene a los elementos, para poder reemplazarla luego
            # por la lista innecesaria, de esta manera que quede los
            # datos de manera optima.
            for j in range(len(days[i][0])):
                temp.append(days[i][0][j])
            days[i] = temp
    return days


def horas_24_semana(days):
    """
    Esta función tiene el propósito de verificar que el formato de
    24 horas se cumple en las respuestas del usuario.
    Esta función tiene como entrada la lista de horas de los días
    "days" siendo este de tipo list.
    La salida de la función es un booleano.
    """
    primero = False
    segundo = False
    final = False
    contador_0 = 0
    contador_1 = 0
    for i in range(len(days)):
        # Recorre la lista tomando las horas y minutos y verificando
        # que cumplan con el formato de 24 horas.
        contador_0 = 0
        for j in range(len(days[i])):
            if 0 <= days[i][j][0] < 24:
                primero = True
            if 0 <= days[i][j][1] < 60:
                segundo = True
            if primero and segundo:
                contador_0 += 1
        # Verifica que todas las horas de un día cumple con el formato
        # y de esta forma el contador_1 cuenta que el día cumple con el
        # formato.

        if contador_0 == len(days[i]):
            contador_1 += 1
    # Si todos los días cumplen con el formato de 24 horas devuelve
    # un booleano a la función option_1
    if len(days) == contador_1:
        final = True
    return final


def horas_24_dia(day):
    """
    Esta función tiene el propósito de verificar que el formato de
    24 horas se cumple en las respuestas del usuario.
    Esta función tiene como entrada la lista de horas del dia
    "day" siendo este de tipo list.
    La salida de la función es un booleano.
    """
    primero = False
    segundo = False
    final = False
    contador = 0
    for i in range(len(day)):
        # Recorre la lista tomando las horas y minutos y verificando
        # que cumplan con el formato de 24 horas.
        if 0 <= day[i][1] < 24:
            primero = True
        if 0 <= day[i][1] < 60:
            segundo = True
        if primero and segundo:
            contador += 1
    # Verifica que las  todas las horas ingresadas por el usuario
    # destinadas actividades fuera del horario de clases
    if contador == len(day):
        final = True
    return final


def daily_time(answer, f):
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
            time_temp = weekly_time(answer, i)
            days.append(time_temp)
        days = lista_sobrante(days)
        horas_24_days = horas_24_semana(days)
        for f in range(7, 10):
            time_temp = daily_time(answer, f)
            day.append(time_temp)
        horas_24_day = horas_24_dia(day)
        # Separa los días
        study_days = s_days(answer)
        # Informa al usuario que ha introducido bien los datos
        if horas_24_day and horas_24_days:
            messagebox.showinfo(
                            "Ha sido un éxito",
                            "Has introducido los datos correctamente")
            archivos.escribir_archivo(study_days, day, days)
        else:
            messagebox.showerror(
                            "Error",
                            "Las horas ingresadas no cumplen con el formato"
                            " 24 horas")
    else:
        # Informa al usuario que no siguió la estructura propuesta.
        messagebox.showerror(
                            "Error",
                            "Los datos que introduciste no cumplen la"
                            " estructura planteada")
