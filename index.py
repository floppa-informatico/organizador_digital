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


def time_answers(answer,i):
    """
    Esta función se encarga de dejar todas las respuestas relacionadas
    al tiempo en una sola lista para así poder trabajarlas durante el 
    largo del código.
    """
    i = "10:00-11:00;21:00-22:00"
    answers = []
    day = []
    answers_1 = answer[i]
    list_temp = answers_1.split(";")
    for i in range(len(list_temp)):
        temp = list_temp[i]
        temp = temp.split("-")
        temp_1 = temp[0]
        day.append(temp_1)
        temp_2 = temp[1]
        day.append(temp_2)
    answers.append(day)
    return answers


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
    question_6 = input("Ingrese su horario de clases del día"
                    " Domingo separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    question_7 = int(input("¿Cuantas horas le dedicas diariamente al estudio?, y" 
                        " si no es así ¿Cuántas horas le gustaría dedicarle"
                        " al estudio? (Ingrese un número entero en horas)"))
    question_8 = int(input("¿Juega a algún videojuego?, si es así, ¿Cuantas" 
                            " horas le dedica? (Ingrese un número entero en" 
                            " horas)"))
    question_9 = int(input("¿Cuantas horas le dedicas a tu tiempo con tu" 
                        "familia?"))
    question_10 = int(input("¿Como te has sentido? (Escriba bien o mal)"))
    all_questions.extend([question_0,question_1,question_2,question_3,
                        question_4,question_5,question_6,question_7,
                        question_8,question_9,question_10])
    return all_questions


def option_1(option):
    answer = questions()
    day = []
    for i in range(7):
        time = time_answers(answer,i)
        day.append(time)
    return


def main():
    while True:
        option = information_input()
        if option == 1:
            u = option_1(option)
