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


def time_answers():
    """
    Esta función se encarga de dejar todas las respuestas en una sola
    lista para así poder trabajarlas durante el largo del código.
    """
    answers = []
    day = []
    answers_1 = input("Para comenzar, ingrese su horario de clases del día"
                    " Lunes separado por ; (Ej: 9:00-10:00;10:00-11:00;etc.)"
                    ": ")
    list_temp = answers_1.split(";")
    print(list_temp)
    for i in range (len(list_temp)):
        temp = list_temp[i]
        temp = temp.split("-")
        temp_1 = temp[0]
        day.append(temp_1)
        temp_2 = temp[1]
        day.append(temp_2)
    answers.append(day)
    return answers

def questions():
    return


def main():
    return

