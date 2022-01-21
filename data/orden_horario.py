# Bloque por definición


def orden():
    """
    Esta función está encargada de dar el formato para escribir
    un archivo de extensión xlsx para luego plasmar este archivo en
    horario.py
    Esta función tiene como entrada datos.txt siendo este de tipo
    archivo, y tiene como salida horas_horario, semana_horario,
    y horas_con_formato siendo estos tres de tipo list.
    """
    respuestas = []
    # Lee el archivo datos.txt para trabajar los datos
    with open("./data/datos.txt", "r") as archivo:
        for linea in archivo:
            respuestas.append(linea.strip())
    # Dejar todas las lineas en su respectiva variable
    dias_especificos = eval(respuestas[0])
    dias_con_horas = eval(respuestas[1])
    semana_horario = eval(respuestas[-2])
    estado_animico = respuestas[-1]
    #archivo = open("./data/datos.txt", "w")
    # archivo.write(str(dias_especificos))
    semana_para_escribir = semana_horario

    # A partir desde las 8:00 genera las demás horas hasta
    # las 23:00, para poder ubicar semana_horario en el horario
    horas_horario = [480]
    for hora_nueva in range(15):
        horas_horario.append(horas_horario[hora_nueva] + 60)

    # Transformar las horas a minutos y guardarlos en su respectivo día
    semana_horario_temp = []
    # Se recorre la lista
    for dia in range(len(semana_horario)):
        dia_0 = []
        # Se recorre el elemento correspondiente a un día
        for horas in semana_horario[dia]:
            hora_0 = horas[0]
            # Se transforma la hora a minutos
            hora_0 = hora_0 * 60
            # Se suma las horas con los minutos
            hora_final = hora_0 + horas[-1]
            # Se agrega la hora ya sumada a la lista correspondiente
            # al día
            dia_0.append(hora_final)
        # Se agrega las horas del día transformada en un lista propia
        # del día a la lista donde están todas las demas de los otros
        # dias
        semana_horario_temp.append(dia_0)
    semana_horario = semana_horario_temp

    # Se ubica las horas de estudio según el día que se especifica.

    # Se elimina si hay días repetidos.
    for elemento in dias_especificos:
        while dias_especificos.count(elemento) > 1:
            dias_especificos.pop(dias_especificos.index(elemento))

    # Se transforma las horas a minutos
    if not(str(dias_con_horas[-1]).isdigit()):
        dia_1 = []
        for hora in dias_con_horas:
            hora_0 = hora[0]
            # Se transforma la hora a minutos
            hora_0 = hora_0 * 60
            # Se suma las horas con los minutos
            hora_final = hora_0 + hora[-1]
            # Se agrega la hora ya sumada a la lista correspondiente
            # al día
            dia_1.append(hora_final)
        dias_con_horas = dia_1

    # Se busca el indice según el día que estudia
    indice_dias_estudio = []
    for dias_estudio in dias_especificos:
        if dias_estudio.lower() == "lunes":
            indice_dias_estudio.append(0)
        if dias_estudio.lower() == "martes":
            indice_dias_estudio.append(1)
        if dias_estudio.lower() == "miercoles":
            indice_dias_estudio.append(2)
        if dias_estudio.lower() == "jueves":
            indice_dias_estudio.append(3)
        if dias_estudio.lower() == "viernes":
            indice_dias_estudio.append(4)
        if dias_estudio.lower() == "sabado":
            indice_dias_estudio.append(5)
        if dias_estudio.lower() == "domingo":
            indice_dias_estudio.append(6)

    # Se le agregan las horas de ocio a las horas de la semana
    comprobar = horas_horario
    for ocio in range(4, 7):
        if ocio == 4 or ocio == 5:
            elemento_anterior = int(semana_horario[ocio][-1])
            # Se suma la hora anterior con el correspondiente
            # tiempo destinado al ocio
            hora_ocio = semana_horario[ocio][-1] + dias_con_horas[-2]
            semana_horario[ocio].append(hora_ocio)
            # Se agregan las horas que están entre estas
            comprobar.append(hora_ocio)
            comprobar.append(elemento_anterior)
            comprobar.sort()
            for ocio_i in comprobar[comprobar.index(elemento_anterior):comprobar.index(hora_ocio)]:
                semana_horario[ocio].append(ocio_i)

    # Se agregan las horas de estudio a los días de la semana
    lista_estudio = []
    comprobar = horas_horario
    for dias_estudio in indice_dias_estudio:
        if estado_animico == "mal":
            # Comprueba si no se ha dividido antes el tiemo
            if str(dias_con_horas[0]).isdigit():
                # Si el tiempo sugerido es mayor a 20
                if dias_con_horas[0] >= 40:
                    # Divide el tiempo de estudios en dos.
                    nuevo_tiempo_0 = dias_con_horas[0] / 2
                    nuevo_tiempo_1 = round(nuevo_tiempo_0)

                    # Hace una proporcion de 1:5 usada en técnica pomodoro
                    # Al ser dos tiempos iguales, solo se ocupará uno para
                    # determinar los tiempos de descanso.
                    tiempo_de_descanso = round((nuevo_tiempo_1 * 1) / 5)
                    # Se agrega este nuevo tiempo de estudio a
                    # lista_estudio
                    lista_estudio.append(int(nuevo_tiempo_0))
                    lista_estudio.append(int(tiempo_de_descanso))
                    lista_estudio.append(int(nuevo_tiempo_1))
                    # Se agrega esta lista al elemento [0] de
                    # dias_con_horas
                    dias_con_horas[0] = lista_estudio
                    for hora_estudio in lista_estudio:
                        elemento_anterior = int(
                            semana_horario[dias_estudio][-1])
                        # Se agregan estos dos anteriores a la lista semana_horario
                        hora = int(
                            semana_horario[dias_estudio][-1]) + int(hora_estudio)
                        semana_horario[dias_estudio].append(hora)
                        # Se agregan las horas que están entre estas
                        comprobar.append(hora)
                        comprobar.append(elemento_anterior)
                        comprobar.sort()
                        for estudio in comprobar[comprobar.index(elemento_anterior):comprobar.index(hora_0)]:
                            semana_horario[dias_estudio].append(estudio)
            # Si se ha dividido antes el tiempo
            else:
                # Recorre la lista para poder dividir nuevamente el
                # tiempo
                for estudio in range(len(dias_con_horas[0])):
                    if estudio % 2 == 0:
                        if dias_con_horas[0][estudio] >= 40:
                            # Divide el tiempo de estudios en dos.
                            nuevo_tiempo_0 = dias_con_horas[0][estudio] / 2
                            nuevo_tiempo_1 = round(nuevo_tiempo_0)

                            # Hace una proporcion de 1:5 usada en técnica pomodoro
                            # Al ser dos tiempos iguales, solo se ocupará uno para
                            # determinar los tiempos de descanso.
                            tiempo_de_descanso = round(
                                (nuevo_tiempo_1 * 1) / 5)
                            # Se agrega este nuevo tiempo de estudio a lista_estudio
                            lista_estudio.append(int(nuevo_tiempo_0))
                            lista_estudio.append(int(tiempo_de_descanso))
                            lista_estudio.append(int(nuevo_tiempo_1))
                    elif estudio % 2 != 0:
                        lista_estudio.append(dias_con_horas[0][estudio])
                # Se agrega esta lista al elemento [0] de dias_con_horas
                dias_con_horas[0] = lista_estudio
                # Se agrega este nuevo tiempo de estudio a lista_estudio
                for hora_estudio in lista_estudio:
                    elemento_anterior = int(semana_horario[dias_estudio][-1])
                    # Se agregan estos dos anteriores a la lista semana_horario
                    hora = int(
                        semana_horario[dias_estudio][-1]) + int(hora_estudio)
                    semana_horario[dias_estudio].append(hora)
                    # Se agregan las horas que están entre estas
                    comprobar.append(hora)
                    comprobar.append(elemento_anterior)
                    comprobar.sort()
                    # Se recorre la lista comprobar para agregar todos los tiempos
                    # que esta entre los tiempos de estudio a la lista
                    for estudio in comprobar[comprobar.index(elemento_anterior):comprobar.index(hora_0)]:
                        semana_horario[dias_estudio].append(estudio)

        else:
            if str(dias_con_horas[0]).isdigit():
                elemento_anterior = int(semana_horario[dias_estudio][-1])
                hora_0 = int(semana_horario[dias_estudio]
                             [-1]) + int(dias_con_horas[0])
                semana_horario[dias_estudio].append(hora_0)
                # Se agregan las horas que están entre estas
                comprobar.append(hora_0)
                comprobar.append(elemento_anterior)
                comprobar.sort()
                # Se recorre la lista comprobar para agregar todos los tiempos
                # que esta entre los tiempos de estudio a la lista
                for estudio in comprobar[comprobar.index(elemento_anterior):comprobar.index(hora_0)]:
                    semana_horario[dias_estudio].append(estudio)
    #archivo = archivo.write(dias_con_horas)
    #archivo = archivo.write(semana_para_escribir)
    #archivo = archivo.write(estado_animico)
    # archivo.close()

    # Se le agregan las horas de familia a las horas de la semana
    comprobar = horas_horario
    for agregar_dia in range(len(semana_horario)):
        hora_familia = 1380 - dias_con_horas[-1]
        semana_horario[agregar_dia].append(hora_familia)
        comprobar.append(hora_familia)
        comprobar.sort()
        for familia in comprobar[comprobar.index(hora_familia):]:
            semana_horario[agregar_dia].append(familia)

    # Se busca en la lista elementos repetidos para eliminarlos
    for dia in range(len(semana_horario)):
        for elemento in semana_horario[dia]:
            while semana_horario[dia].count(elemento) > 1:
                semana_horario[dia].pop(semana_horario[dia].index(elemento))

    # Se duplica la lista de cada día y se eliminan los elementos de
    # los extremos
    for dia in semana_horario:
        dia *= 2
        dia.sort()
        dia.pop(0)
        dia.pop(-1)

    # Hacemos una lista de listas de listas para semana_horario
    semana_horario_2 = semana_horario
    lista_temporal = []
    lista_temporal_2 = []
    lista_temporal_3 = []
    for dia in range(len(semana_horario)):
        for elemento in semana_horario[dia]:
            lista_temporal.append(elemento)
            if len(lista_temporal) == 2:
                lista_temporal_2.append(lista_temporal)
                lista_temporal = []
        lista_temporal_3.append(lista_temporal_2)
        lista_temporal_2 = []
    semana_horario = lista_temporal_3

    # Ubica las horas ubicadas en semana_horario en horas_horario
    # Se recorre la lista semana_horario para poder agregar la lista
    # de listas representando un día entero a la lista lista_temporal
    acumulador = []
    for dia in semana_horario_2:
        acumulador += dia
    horas_horario += acumulador
    horas_horario.sort()

    # Se verifica que no hayan horas repetidas
    for elemento in horas_horario:
        while horas_horario.count(elemento) > 1:
            horas_horario.pop(horas_horario.index(elemento))

    # Ahora duplicamos las horas a excepción de las horas de los
    # extremos para que quede de la siguiente forma x:xx - x:xx
    horas_horario *= 2
    horas_horario.sort()
    horas_horario.pop(0)
    horas_horario.pop(-1)

    # Hacemos que quede una lista de listas
    lista_temporal = []
    lista_temporal_2 = []
    for hora in horas_horario:
        lista_temporal.append(hora)
        if len(lista_temporal) == 2:
            lista_temporal_2.append(lista_temporal)
            lista_temporal = []
    horas_horario = lista_temporal_2

    # Elimina de semana_horario horas sobrantes.
    for dia in range(len(semana_horario)):
        for horas in semana_horario[dia]:
            if horas not in horas_horario:
                semana_horario[dia].pop(semana_horario[dia].index(horas))

    # Vuelve a pasar los minutos a horas
    horas_con_formato = []
    for rango_hora in range(len(horas_horario)):
        for hora in range(len(horas_horario[rango_hora])):
            hora_entera = str(int(
                (horas_horario[rango_hora][hora] / 60) - ((horas_horario[rango_hora][hora] % 60) / 60)))
            minutos = str(horas_horario[rango_hora][hora] % 60)
            if minutos == "0":
                hora_completa = hora_entera + ":" + minutos + "0"
            else:
                hora_completa = hora_entera + ":" + minutos
            horas_con_formato.append(hora_completa)

    # Hacemos que quede una lista de listas
    lista_temporal = []
    lista_temporal_2 = []
    for hora in horas_con_formato:
        lista_temporal.append(hora)
        if len(lista_temporal) == 2:
            lista_temporal_2.append(lista_temporal)
            lista_temporal = []
    horas_con_formato = lista_temporal_2

    return horas_horario, semana_horario, horas_con_formato,\
        indice_dias_estudio


# Se ejecuta la función orden() solo si se ejecuta desde el mismo
# no así se llama desde otro archivo
if __name__ == "__main__":
    orden()
