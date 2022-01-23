import xlsxwriter
import proc.orden_horario as horario
#import orden_horario as horario


# Bloque de definiciones


def imprimir_datos_en_xlsx(
        dia,
        indice_dias_estudio,
        horas_horario,
        estado_animico,
        hoja,
        semana_horario,
        semana_solo_horario,
        dias_con_hora,
        lista_horas_estudio,
        lista_horas_ocio,
        lista_horas_familia):
    """
    Esta función se encarga de imprimir las horas en el archivo .xlsx.
    Esta función tiene como entrada dia siendo de tipo int,
    indice_dias_estudio siendo de tipo list, horas_horario siendo de
    tipo list, estado_animico siendo de tipo string, hoja siendo de
    tipo archivo, semana_horario siendo de tipo list.
    Tiene como salida la escritura en el archivo .xlsx, siendo este
    de tipo archivo.
    """
    # Hacemos una lista de lista de lista para obtener la cantidad de
    # bloques de horario de clases
    semana_solo_horario = eval(semana_solo_horario)
    lista_temporal = []
    lista_temporal_1 = []
    for hora in semana_solo_horario[dia]:
        lista_temporal.append(hora)
        if len(lista_temporal) == 2:
            lista_temporal_1.append(lista_temporal)
            lista_temporal = []
    semana_solo_horario = lista_temporal_1
    # Verifica si el dia estando representado por la variable dia es
    # un dia el que el usuario estudia, estando previamente
    # identificado en indice_dias_estudio
    dia_de_estudio = False
    for estudio in indice_dias_estudio:
        # Verifica que el dia sea de estudio viendo si el dia está
        # dentro de indice_dias_estudio siendo los elementos de este
        # mismo los días de estudio.
        if estudio == dia:
            dia_de_estudio = True
    if dia_de_estudio:
        # Verifica el estado_animico del usuario, ya que si se
        # encuentra en mal estado divide los tiempos de estudio
        if estado_animico == "mal":
            # Escribe los tiempos dedicados si o si a familia y
            # a descansar.
            for hora_descanso in lista_horas_familia[dia]:
                hoja.write(
                    horas_horario.index(hora_descanso) + 1,
                    dia + 1,
                    "Familia y descanso")
            # Si el día es viernes, sabado o domingo, es día en el que
            # el usario tendrá tiempo de ocio.
            if dia == 4 or dia == 5 or dia == 6:
                # Escribe los tiempos destinados a clases.
                for hora_clases in semana_solo_horario:
                    hoja.write(
                        horas_horario.index(hora_clases) + 1,
                        dia + 1,
                        "Clases")

                # Escribe los tiempos destinados a ocio
                for hora_ocio in lista_horas_ocio[dia]:
                    hoja.write(
                        horas_horario.index(hora_ocio) + 1,
                        dia + 1,
                        "Ocio")
                # Finalmente escribe los tipos destinados al estudio
                for hora_estudio in lista_horas_estudio[dia]:
                    if len(lista_horas_estudio[dia]) == 2:
                        hoja.write(
                            horas_horario.index(hora_estudio) + 1,
                            dia + 1,
                            "Estudio")
                    elif lista_horas_estudio[dia].index(hora_estudio) % 2 == 0:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Estudio")
                    else:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Descanso")
            # Si no es viernes, sabado o domingo, escribe los tiempos
            # sin considerar el tiempo dedicado a ocio.
            else:
                # Escribe los tiempos destinados a clases
                for hora_clases in semana_solo_horario:
                    hoja.write(
                        horas_horario.index(hora_clases) + 1,
                        dia + 1,
                        "Clases")

                # Finalmente escribe los tipos destinados al estudio
                for hora_estudio in lista_horas_estudio[dia]:
                    if len(lista_horas_estudio[dia]) == 2:
                        hoja.write(
                            horas_horario.index(hora_estudio) + 1,
                            dia + 1,
                            "Estudio")
                    elif lista_horas_estudio[dia].index(hora_estudio) % 2 == 0:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Estudio")
                    else:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Descanso")
        # Si el usuario se encuentra bien con respecto a su salud
        # mental, no dividirá sus tiempos de estudio.
        else:
            # Escribe los tiempos destinados a familia y a descanso
            for hora_descanso in lista_horas_familia[dia]:
                hoja.write(
                    horas_horario.index(hora_descanso) + 1,
                    dia + 1,
                    "Familia y descanso")
            # Si el día es viernes, sabado o domingo, es día en el que
            # el usario tendrá tiempo de ocio.
            if dia == 4 or dia == 5 or dia == 6:
                # Escribe los tiempos destinados a clases.
                for hora_clases in semana_solo_horario:
                    hoja.write(
                        horas_horario.index(hora_clases) + 1,
                        dia + 1,
                        "Clases")

                # Escribe los tiempos destinados al ocio
                for hora_ocio in lista_horas_ocio[dia]:
                    hoja.write(
                        horas_horario.index(hora_ocio) + 1,
                        dia + 1,
                        "Ocio")
                # Escribe el horario de estudio.
                for hora_estudio in lista_horas_estudio[dia]:
                    if len(lista_horas_estudio[dia]) == 2:
                        hoja.write(
                            horas_horario.index(hora_estudio) + 1,
                            dia + 1,
                            "Estudio")
                    elif lista_horas_estudio[dia].index(hora_estudio) % 2 == 0:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Estudio")
                    else:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Descanso")
            # Si el día que se escribirá no es viernes, sabado o
            # domingo se escribe los tiempos sin considerar el
            # tiempo destinado al ocio
            else:
                # Se escribe el tiempo destinado a las clases
                for hora_clases in semana_solo_horario:
                    hoja.write(
                        horas_horario.index(hora_clases) + 1,
                        dia + 1,
                        "Clases")

                # Se escribe el tiempo destinado al estudio.
                for hora_estudio in lista_horas_estudio[dia]:
                    if len(lista_horas_estudio[dia]) == 2:
                        hoja.write(
                            horas_horario.index(hora_estudio) + 1,
                            dia + 1,
                            "Estudio")
                    elif lista_horas_estudio[dia].index(hora_estudio) % 2 == 0:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Estudio")
                    else:
                        hoja.write(
                            horas_horario.index(hora_estudio),
                            dia + 1,
                            "Descanso")
    # Escriben el tiempo sin considerar los tiempos destinados al
    # estudio ya que el usuario así lo especificó.
    else:
        # Se esribe el tiempo destinado a la familia y descanso
        for hora_descanso in lista_horas_familia[dia]:
            hoja.write(
                horas_horario.index(hora_descanso) + 1,
                dia + 1,
                "Familia y descanso")
        # Si el dia es viernes, sabado, o domingo se considera
        # el tiempo destinado al ocio
        if dia == 4 or dia == 5 or dia == 6:
            # Se escribe el tiempo destinado a clases.
            for hora_clases in semana_solo_horario:
                hoja.write(
                    horas_horario.index(hora_clases) + 1,
                    dia + 1,
                    "Clases")

            # Se escribe el tiempo destinado al ocio.
            for hora_ocio in lista_horas_ocio[dia]:
                hoja.write(
                    horas_horario.index(hora_ocio) + 1,
                    dia + 1,
                    "Ocio")
        # Si no es viernes, sabado, o domigno se escribe sin
        # considerar el tiempo de ocio.
        else:
            # Se escriben los horarios de clase.
            for hora_clases in semana_solo_horario:
                hoja.write(
                    horas_horario.index(hora_clases) + 1,
                    dia + 1,
                    "Clases")


def escribir_xlsx():
    """
    Esta función tiene el propósito de recopilar todo lo necesario
    para poder escribir finalmente en el archivo .xlsx que luego se
    pasará a tkinter. Por lo que se crea la hoja del archivo .xlsx y
    el respectivo archivo de esta extensión, escribe los días, las
    horas previamente hecha, y por ultimo escribe los horarios.
    """
    # Se leen y se trabajan los datos en la función orden del archivo
    # orden_horario.py ubicado dentro del directorio proc.
    # Se obtienen los datos ya trabajados.
    horas_horario, semana_horario, horas_con_formato,\
        indice_dias_estudio, semana_solo_horario, \
        dias_con_hora, lista_horas_estudio, \
        lista_horas_ocio, lista_horas_familia = horario.orden()
    # Se obtiene el estado animico, ya que este no sufre modificaciones
    # en orden_horario.py
    with open("./data/datos.txt", "r") as txt:
        lista_vacia = []
        for linea in txt:
            lista_vacia.append(linea)
        estado_animico = lista_vacia[3]

    # Se crea el archivo de extensión .xlsx
    archivo = xlsxwriter.Workbook("./data/datos.xlsx")
    # Se crea la hoja en el que se escribiran los datos del archivo
    # .xlsx
    hoja = archivo.add_worksheet()
    # Se escribe la primera fila que contiene los titulos del horario
    # o sea los días.
    hoja.write(0, 0, "Horas")
    hoja.write(0, 1, "Lunes")
    hoja.write(0, 2, "Martes")
    hoja.write(0, 3, "Miercoles")
    hoja.write(0, 4, "Jueves")
    hoja.write(0, 5, "Viernes")
    hoja.write(0, 6, "Sabado")
    hoja.write(0, 7, "Domingo")

    # Se comienza a escribir los horarios del usuario.
    # Se recorre la lista representando el indice de esta lista los
    # dias.
    for dia in range(len(semana_horario)):
        # Recorre los días siendo la lista de listas que representan
        # los dias
        for hora in range(len(semana_horario[dia])):
            # Se imprime los horarios del día lunes
            if dia == 0:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)
            # Se imprime los horarios del día Martes
            if dia == 1:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)
            # Se imprime los horarios del día miercoles
            if dia == 2:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)
            # Se imprime los horarios del día Jueves
            if dia == 3:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)
            # Se imprime los horarios del día Viernes
            if dia == 4:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)
            # Se imprime los horarios del día Sábado.
            if dia == 5:
                imprimir_datos_en_xlsx(
                    dia,
                    indice_dias_estudio,
                    horas_horario,
                    estado_animico,
                    hoja,
                    semana_horario,
                    semana_solo_horario,
                    dias_con_hora,
                    lista_horas_estudio,
                    lista_horas_ocio,
                    lista_horas_familia)

    # Se imprimen las horas para que el usuario tenga una mejor
    # comprensión del horario.
    for horas in range(len(horas_con_formato)):
        hoja.write(
            horas + 1,
            0,
            horas_con_formato[horas][0] + " - " + horas_con_formato[horas][1])
    # Cierra el archivo .xlsx
    archivo.close()


# Bloque principal
# Se ejecuta solamente si se ejecuta solamente este archivo .py no así
# si este archivo es llamado desde otro archivo.
if __name__ == "__main__":
    escribir_xlsx()
