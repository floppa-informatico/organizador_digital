# Bloque por definición
def information_input():
    """
    Esta función le mostrará al usuario, y un menú para lo que el
    usuario estime conveniente.
    """
    option = int(input("Bienvenid@ a Organizador digital, nos adaptamos"
                    " rápidamente a ti :D!\n"
                    "\n"
                    "\n"
                    "¿Qué desea hacer?\n"
                    "  1. Comenzar o volver a responder las preguntas.\n"
                    "  2. Ver mi horario.\n"
                    "  3. Modificar mi horario.\n"
                    "  4. ¿Cómo te sientes?.\n"
                    "  5. ¿Cómo se usa esta aplicación?.\n"
                    "  6. Salir.\n"
                    "Seleccione una opción: "))
    return option


def questions():
    """
    Esta función se encarga de hacer las preguntas y recopilar todas 
    las respuestas que de el usuario
    """
    all_questions = []
    question_0 = input("Para comenzar, ingrese su horario de clases del día"
                    " Lunes separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_1 = input("Ingrese su horario de clases del día"
                    " Martes separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_2 = input("Ingrese su horario de clases del día"
                    " Miércoles separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_3 = input("Ingrese su horario de clases del día"
                    " Jueves separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_4 = input("Ingrese su horario de clases del día"
                    " Viernes separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_5 = input("Ingrese su horario de clases del día"
                    " Sábado separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_6 = input("¿Qué días estudia? Escriba los días separado por ;"
                        "(Ej: viernes;sabado;domingo)")
    question_7 = input("¿Cuantas horas le dedicas diariamente al estudio?, y" 
                        " si no es así ¿Cuántas horas le gustaría dedicarle"
                        " al estudio? (Siga la siguiente estructura xx:xx): ")
    question_8 = input("¿Juega a algún videojuego?, si es así, ¿Cuantas" 
                            " horas le dedica diariamente? (Siga la siguiente"
                            " estructura (xx:xx): ")
    question_9 = input("¿Cuantas horas le dedicas a tu tiempo con tu" 
                        "familia?: ")
    question_10 = input("¿Como te has sentido? (Escriba bien o mal): ")
    # Agrega todas las respuestas de las preguntas a una lista para
    # usar lo menos posibles tantas variables que retornen a la
    # función principal.
    all_questions.extend([question_0,question_1,question_2,question_3,
                        question_4,question_5,question_6,question_7,
                        question_8,question_9,question_10])
    return all_questions


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


def time_assignment():
    """
    Esta función se encarga de asignar las horas de estudio, ocio,
    entre otros. En caso de que no tenga que entrar a la función feel
    sería el horario que debería mostar la opción 2 del programa.
    """


def feel():
    """"
    Esta función se encarga de dividir en jornadas más pequeñas, las
    jornadas de estudio. Esto en caso de que el usuario reporte en la
    decima pregunta que se encuentra mal debido a estrés o ansiedad.
    """


def option_1():
    """
    Esta función es la función para la primera opción que se encarga de
    hacerle las preguntas correspondientes al usuario, para luego
    de manera interna pueda hacer el horario para el usuario totalmente
    adapto a él. El usuario podra ver el horario en la opción 2.
    """
    answer = questions()
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
    return study_days,day,days


def help():
    print("Esta aplicación organizador digital tiene el proposito de \n"
    "mejorar la salud mental de l@s estudiantes.\n\n Esta aplicación consta"
    "de seis opciones distintas, la primera en la que se le pregunta al\n"
    "usuario acerca de sus horarios. Se pide por favor seguir la estructura\n"
    "pedida, ya que es de importancia para que el programa funcione\n"
    "correctamente.\n La segunda opción solo muestra el horario hecho, si"
    "el usuario no ha ingresado nada dará error.\n"
    "La tercera preguntará al usuario ")


# Bloque principal
while True:
    # Entrada
    option = information_input()
    # Procedimiento
    if option == 1:
        x = option_1()
    elif option == 6:
        break
