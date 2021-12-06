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
                        "(Ej: viernes;sabado;domingo: ")
    question_7 = input("¿Cuantas horas le dedicas diariamente al estudio?, y" 
                        " si no es así ¿Cuántas horas le gustaría dedicarle"
                        " al estudio? (Siga la siguiente estructura xx:xx): ")
    question_8 = input("¿Juega a algún videojuego?, si es así, ¿Cuantas" 
                            " horas le dedica diariamente? (Siga la siguiente"
                            " estructura (xx:xx): ")
    question_9 = input("¿Cuantas horas le dedicas a tu tiempo con tu" 
                        "familia?: ")
    question_10 = input("¿Como te has sentido? (Escriba bien o mal): ")
    all_questions.extend([question_0,question_1,question_2,question_3,
                        question_4,question_5,question_6,question_7,
                        question_8,question_9,question_10])
    return all_questions


def weekly_time(answer,i):
    """
    Esta función se encarga de dejar todas las respuestas relacionadas
    al tiempo en una sola lista para así poder trabajarlas durante el 
    largo del código. El tiempo d
    """
    answers = []
    day = []
    answers_1 = answer[i]
    answers_1 = answers_1.split(";")
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
    answers.append(day)
    return answers


def daily_time(answer,f):
    answer_1 = answer[f]
    answer_1 = answer_1.split(":")
    for j in range(2):
        answer_1[j] = int(answer_1[j])
    return answer_1


def option_1():
    answer = questions()
    days = []
    day = []
    for i in range(6):
        time_temp = weekly_time(answer,i)
        days.append(time_temp)
    for f in range(7,10):
        time_temp = daily_time(answer,f)
        day.append(time_temp)
    return 0


def main():
    while True:
        option = information_input()
        if option == 1:
            x = option_1()


main()
