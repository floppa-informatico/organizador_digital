# Bloque de definiciones
# Bloque de definición de funciones


def duplicar(lista):
    """
    Esta función tiene el propósito de duplicar la lista, ordenarla,
    y borrar las horas del inicio y del final con el objetivo de poder
    darle formato en la función formato_listas.
    Esta función tiene como entrada lista siendo este de tipo list y
    tiene como salida lista siendo este de tipo list.
    """
    # Ahora duplicamos las horas a excepción de las horas de los
    # extremos para que quede de la siguiente forma x:xx - x:xx
    lista *= 2
    # Se ordena la lista
    lista.sort()
    # Se elimina el primer y el último elemento
    lista.pop(0)
    lista.pop(-1)
    return lista


def formato_listas_de_listas(lista):
    """
    Esta función tiene el propósito de generar una lista de listas para
    lista.
    Esta función tiene como entrada lista, siendo de tipo list.
    Esta función tiene como salida lista, siendo de tipo list.
    """
    # Se crean listas temporales
    lista_temporal = []
    lista_temporal_1 = []
    lista_temporal_2 = []
    # Luego se da formato a la lista
    for dia in lista:
        for hora in dia:
            # Se agrega la hora a la lista temporal
            lista_temporal.append(hora)
            # Si el largo de la lista temporal es igual a dos significa
            # que ya tiene el formato esperado
            if len(lista_temporal) == 2:
                # Se agrega la lista temporal a la lista temporal_1
                # representando el día en especifico.
                lista_temporal_1.append(lista_temporal)
                # Se vacía la lista temporal para seguir con el formato
                lista_temporal = []
        # Si el largo de la lista temporal es igual al largo de la
        # lista correspondiente al día, agrega la lista_temporal_1
        # a lista_temporal_2
        if len(lista_temporal_1) == len(dia) / 2:
            lista_temporal_2.append(lista_temporal_1)
            lista_temporal_1 = []
    # Al tener la lista_temporal_2 la lista ya con el formato
    # solicitado se le asigna esta lista la lista original.
    lista = lista_temporal_2
    return lista


def eliminar_repetidos_lista_de_listas(lista):
    """
    Esta función teien el propósito de eliminar los elementos que se
    repitan de la lista de listas siendo este representado por lista.
    Esta función tiene como entrada lista, siendo de tipo list.
    Esta función tiene como salida lista, siendo de tipo list.
    """
    # Se recorre la lista eliminando elementos repetidos
    for dia in lista:
        for hora in dia:
            # Si la hora se encuentra mas de una vez en la lista
            # será eliminado
            while dia.count(hora) > 1:
                # Se elimina la hora de la lista
                dia.remove(hora)
        # Se ordena la lista de los dias
        dia.sort()
    # Una vez eliminado los días repetidos, se duplica la lista
    # y se elimina la repeticiones de los extremos
    for dia in range(len(lista)):
        # Se duplica la lista
        lista[dia] *= 2
        # Se ordena la lista
        lista[dia].sort()
        if len(lista[dia]) != 0:
            # Elimina el primer elemento
            lista[dia].pop(0)
            # Elimina el último elemento
            lista[dia].pop(-1)
    return lista


def eliminar_repetidos_listas(lista):
    """
    Esta función tiene como propósito eliminar elementos repetidos en
    la lista llamada lista.
    Esta función tiene como entrada lista, siendo de tipo list.
    Esta función tiene como salida lista, siendo de tipo list.
    """
    # Se verifica que no hayan horas repetidas
    for elemento in lista:
        # Si se encuentra mas de una vez en la lista es por
        # que esta repetido
        while lista.count(elemento) > 1:
            lista.remove(elemento)
    return lista


def formato_listas(lista):
    """
    Esta función está encargada de dar un formato [xx,xx] de manera que
    se pueda trabajar con estas horas en el archivo escribir_xlsx.py
    Esta función tiene como entrada lista siendo este de tipo list.
    Y tiene como salida lista siendo de tipo list.
    """
    # Se crean listas temporales
    lista_temporal = []
    lista_temporal_2 = []
    # Se recorre la lista
    for hora in lista:
        lista_temporal.append(hora)
        # Se forman bloques de dos horas
        if len(lista_temporal) == 2:
            # Se hace una lista de listas
            lista_temporal_2.append(lista_temporal)
            # Se vacia la lista_temporal para seguir formando bloques
            lista_temporal = []
    # Una vez dado el formato deseado almacenado en lista_temporal_2 se
    # asigna este a la lista
    lista = lista_temporal_2
    return lista


def eliminar_bloques_inexistentes(lista, semana):
    """
    Esta función tiene el propósito de eliminar en caso de que el
    programa genere algun bloque que no exista dentro de semana,
    para de esta forma evitar errores dentro del programa.
    Esta función tiene como entrada lista y semana siendo ambos de tipo
    list.
    Esta función teien como salida lista, siendo de tipo list.
    """
    # Elimina de la lista horas sobrantes, que no están en semana
    for dia in lista:
        for horas in dia:
            if horas not in semana:
                dia.remove(horas)
    return lista


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
    archivo = open("./data/datos.txt", "w")
    archivo.write(str(dias_especificos))
    archivo.write("\n")
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
    semana_solo_horario = semana_horario
    semana_solo_horario = str(semana_solo_horario)
    semana_solo_horario_2 = semana_solo_horario

    # Se elimina si hay días repetidos.
    dias_especificos = eliminar_repetidos_listas(dias_especificos)

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
    for clases in range(len(semana_horario)):
        for hora in range(0, int(len(semana_horario[clases])), 2):
            elemento_anterior = int(semana_horario[clases][hora])

            # Se suma la hora anterior con el correspondiente
            # tiempo destinado al ocio
            elemento_siguiente = int(semana_horario[clases][hora + 1])
            # Se agregan las horas que están entre estas
            comprobar.append(elemento_anterior)
            comprobar.append(elemento_siguiente)
            comprobar.sort()
            for clase in comprobar[
                    comprobar.index(elemento_anterior):
                    comprobar.index(elemento_siguiente)]:
                semana_horario[clases].append(clase)
    semana_horario = eliminar_repetidos_lista_de_listas(semana_horario)

    # Obtenemos los horas que están entre las horas pedidas.
    lista_horas_clases = []
    lista_temporal = []
    for dia in range(len(semana_horario)):
        for hora in semana_horario[dia]:
            # Se suma la hora anterior con el correspondiente
            # tiempo destinado al ocio
            # Se agregan las horas que están entre estas
            lista_temporal.append(hora)
        lista_horas_clases.append(lista_temporal)
        lista_temporal = []

    # Se le agregan las horas de ocio a las horas de la semana
    comprobar = horas_horario
    for ocio in range(4, 6):
        if ocio == 4 or ocio == 5:
            # Se ordena la lista
            semana_horario[ocio].sort()
            elemento_anterior = int(semana_horario[ocio][-1])
            # Se suma la hora anterior con el correspondiente
            # tiempo destinado al ocio
            hora_ocio = semana_horario[ocio][-1] + dias_con_horas[-2]
            semana_horario[ocio].append(hora_ocio)
            # Se agregan las horas que están entre estas
            comprobar.append(hora_ocio)
            comprobar.append(elemento_anterior)
            comprobar.sort()
            for ocio_i in comprobar[
                    comprobar.index(elemento_anterior):
                    comprobar.index(hora_ocio)]:
                semana_horario[ocio].append(ocio_i)

    # Se obtienen las horas de ocio por separado para usarlo en
    # escribir_xlsx.py
    lista_horas_ocio = []
    lista_temporal = []
    for dia in range(len(semana_horario)):
        for hora in semana_horario[dia]:
            # Si la hora no se encuentra dentro de semana_solo_horario
            # es por que es la hora de estudio.
            if hora not in lista_horas_clases[dia]:
                lista_temporal.append(hora)
        # Se agrega la hora anterior para poder los bloques de horario
        # de ocio.
        if dia == 4 or dia == 5:
            lista_temporal.append(eval(semana_solo_horario_2)[dia][-1])
        # Se hace una lista de listas para poder organizar los tiempos
        # por día
        lista_horas_ocio.append(lista_temporal)
        lista_temporal = []
    # Se agregan las horas de estudio a los días de la semana
    lista_estudio = []
    guardar_lista = []
    comprobar = horas_horario
    for dias_estudio in indice_dias_estudio:
        if estado_animico == "mal":
            # Comprueba si no se ha dividido antes el tiempo
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
                    # Se agregan elementos a la lista
                    lista_estudio.append(int(nuevo_tiempo_0))
                    lista_estudio.append(int(tiempo_de_descanso))
                    lista_estudio.append(int(nuevo_tiempo_1))
                    for hora_estudio in lista_estudio:
                        # Ordena la lista
                        semana_horario[dias_estudio].sort()
                        elemento_anterior = int(
                            semana_horario[dias_estudio][-1])
                        # Se agregan estos dos anteriores a la lista
                        # semana_horario
                        hora = int(
                            semana_horario[dias_estudio][-1]) + \
                            int(hora_estudio)
                        semana_horario[dias_estudio].append(hora)
                        # Se agregan las horas que están entre estas
                        comprobar.append(hora)
                        comprobar.append(elemento_anterior)
                        comprobar.sort()
                        for estudio in comprobar[
                                comprobar.index(elemento_anterior):
                                comprobar.index(hora)]:
                            semana_horario[dias_estudio].append(estudio)
                    lista_estudio = []
            # Si se ha dividido antes el tiempo
            else:
                # Recorre la lista para poder dividir nuevamente el
                # tiempo
                if dias_con_horas[0][0] >= 40:
                    for estudio in range(len(dias_con_horas[0])):
                        if estudio % 2 == 0:
                            if dias_con_horas[0][estudio] >= 40:
                                # Divide el tiempo de estudios en dos.
                                nuevo_tiempo_0 = dias_con_horas[0][estudio] \
                                    / 2
                                nuevo_tiempo_1 = round(nuevo_tiempo_0)

                                # Hace una proporcion de 1:5 usada en
                                # técnica pomodoro
                                # Al ser dos tiempos iguales, solo se
                                # ocupará uno para
                                # determinar los tiempos de descanso.
                                tiempo_de_descanso = round(
                                    (nuevo_tiempo_1 * 1) / 5)
                                # Se agrega este nuevo tiempo de
                                # estudio a lista_estudio
                                lista_estudio.append(int(nuevo_tiempo_0))
                                lista_estudio.append(int(tiempo_de_descanso))
                                lista_estudio.append(int(nuevo_tiempo_1))
                        elif estudio % 2 != 0:
                            lista_estudio.append(dias_con_horas[0][estudio])
                    # Se agrega este nuevo tiempo de estudio a lista_estudio
                    for hora_estudio in lista_estudio:
                        # Ordena la lista
                        semana_horario[dias_estudio].sort()
                        elemento_anterior = int(
                            semana_horario[dias_estudio][-1])
                        # Se agregan estos dos anteriores a la lista
                        # semana_horario
                        hora = int(
                            semana_horario[dias_estudio][-1]) + \
                            int(hora_estudio)
                        semana_horario[dias_estudio].append(hora)
                        # Se agregan las horas que están entre estas
                        comprobar.append(hora)
                        comprobar.append(elemento_anterior)
                        comprobar.sort()
                        # Se recorre la lista comprobar para agregar
                        # todos los tiempos que esta entre los tiempos
                        # de estudio a la lista
                        for estudio in comprobar[
                                comprobar.index(elemento_anterior):
                                comprobar.index(hora)]:
                            semana_horario[dias_estudio].append(estudio)
                    lista_estudio = []

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
                for estudio in comprobar[
                        comprobar.index(elemento_anterior):
                        comprobar.index(hora_0)]:
                    semana_horario[dias_estudio].append(estudio)
    # Se agrega este nuevo tiempo de estudio a
    # lista_estudio
    if estado_animico == "mal":
        if dias_con_horas[0] >= 40:
            guardar_lista.append(int(nuevo_tiempo_0))
            guardar_lista.append(int(tiempo_de_descanso))
            guardar_lista.append(int(nuevo_tiempo_1))
            # Se agrega esta lista al elemento [0] de
            # dias_con_horas
            dias_con_horas[0] = lista_estudio
        elif dias_con_horas[0][0] >= 40:
            for estudio in range(len(dias_con_horas[0])):
                if estudio % 2 == 0:
                    if dias_con_horas[0][estudio] >= 20:
                        dias_con_horas[0][estudio] = int(nuevo_tiempo_0)
                        dias_con_horas[0].insert(dias_con_horas[0].index(
                            dias_con_horas[0][estudio]),
                            int(tiempo_de_descanso))
                        dias_con_horas[0].insert(dias_con_horas[0].index(
                            tiempo_de_descanso), int(nuevo_tiempo_1))

    # Se guarda la division hecha al horario de estudios al usar el
    # boton como te sientes.
    archivo.write(str(dias_con_horas))
    archivo.write("\n")
    archivo.write(str(semana_para_escribir))
    archivo.write("\n")
    archivo.write(str(estado_animico))
    archivo.close()
    # Separamos las horas de estudio para el archivo
    # escribir_xlsx.py
    lista_horas_estudio = []
    lista_temporal = []
    for dia in range(len(semana_horario)):
        for hora in semana_horario[dia]:
            # Si la hora no se encuentra dentro de semana_solo_horario
            # es por que es la hora de estudio.
            if hora not in lista_horas_clases[dia] and \
                    hora not in lista_horas_ocio[dia]:
                lista_temporal.append(hora)
        # Se agrega la hora anterior a la lista
        if dia in indice_dias_estudio:
            lista_temporal.append(semana_horario[dia][-len(lista_temporal)])
        lista_horas_estudio.append(lista_temporal)
        lista_temporal = []

    # Se le agregan las horas de familia a las horas de la semana
    comprobar = horas_horario
    for agregar_dia in range(len(semana_horario)):
        hora_familia = 1380 - dias_con_horas[-1]
        semana_horario[agregar_dia].append(hora_familia)
        comprobar.append(hora_familia)
        comprobar.sort()
        for familia in comprobar[comprobar.index(hora_familia):]:
            semana_horario[agregar_dia].append(familia)

    # Separamos las horas de familia para el archivo
    # escribir_xlsx.py
    lista_horas_familia = []
    lista_temporal = []
    for dia in range(len(semana_horario)):
        for hora in semana_horario[dia]:
            # Si la hora no se encuentra dentro de semana_solo_horario
            # es por que es la hora de estudio.
            if hora not in lista_horas_clases[dia]\
                    and hora not in lista_horas_ocio[dia]\
                    and hora not in lista_horas_estudio[dia]:
                lista_temporal.append(hora)
        lista_horas_familia.append(lista_temporal)
        lista_temporal = []

    # Se busca en la lista elementos repetidos para eliminarlos
    semana_horario = eliminar_repetidos_lista_de_listas(semana_horario)

    # Hacemos una lista de listas de listas para semana_horario
    semana_horario_2 = semana_horario
    # Se ordena y se da formato a semana_horario
    semana_horario = formato_listas_de_listas(semana_horario)

    # Ubica las horas ubicadas en semana_horario en horas_horario
    # Se recorre la lista semana_horario para poder agregar la lista
    # de listas representando un día entero a la lista lista_temporal
    acumulador = []
    for dia in semana_horario_2:
        acumulador += dia
    horas_horario += acumulador
    horas_horario.sort()

    # Se verifica que no hayan horas repetidas
    horas_horario = eliminar_repetidos_listas(horas_horario)

    # Se duplica la lista para formar bloques
    horas_horario = duplicar(horas_horario)

    # Hacemos que quede una lista de listas
    horas_horario = formato_listas(horas_horario)

    # Elimina de semana_horario horas sobrantes.
    semana_horario = eliminar_bloques_inexistentes(
        semana_horario, horas_horario)

    # Vuelve a pasar los minutos a horas
    horas_con_formato = []
    for rango_hora in range(len(horas_horario)):
        for hora in range(len(horas_horario[rango_hora])):
            hora_entera = str(int(
                (horas_horario[rango_hora][hora] / 60) -
                ((horas_horario[rango_hora][hora] % 60) / 60)))
            minutos = str(horas_horario[rango_hora][hora] % 60)
            if minutos == "0":
                hora_completa = hora_entera + ":" + minutos + "0"
            else:
                hora_completa = hora_entera + ":" + minutos
            horas_con_formato.append(hora_completa)

    # Hacemos que quede una lista de listas para las horas_con_formato
    horas_con_formato = formato_listas(horas_con_formato)

    # Eliminamos las horas repetidas para escribir_xlsx.py
    # Eliminamos horas repetidas para lista_horas_ocio
    lista_horas_ocio = eliminar_repetidos_lista_de_listas(lista_horas_ocio)
    # Eliminamos horas repetidas para lista_horas_estudio
    lista_horas_estudio = eliminar_repetidos_lista_de_listas(
        lista_horas_estudio)
    # Eliminamos horas repetidas para lista_horas_familia
    lista_horas_familia = eliminar_repetidos_lista_de_listas(
        lista_horas_familia)
    # Eliminamos horas repetidas para lista_horas_clases
    lista_horas_clases = eliminar_repetidos_lista_de_listas(
        lista_horas_clases)

    # Damos formatos a las horas para escribir_xlsx.py
    # Damos formato a las horas para lista_horas_ocio
    lista_horas_ocio = formato_listas_de_listas(lista_horas_ocio)
    # Damos formato a las horas para lista_horas_estudio
    lista_horas_estudio = formato_listas_de_listas(lista_horas_estudio)
    # Damos formato a las horas para lista_horas_familia
    lista_horas_familia = formato_listas_de_listas(lista_horas_familia)
    # Damos formato a las horas para lista_horas_clases
    lista_horas_clases = formato_listas_de_listas(lista_horas_clases)

    # Elimina las horas sobrantes
    # Elimina las horas sobrantes de lista_hora_ocio
    lista_horas_ocio = eliminar_bloques_inexistentes(
        lista_horas_ocio, horas_horario)
    # Elimina las horas sobrantes de lista_hora_estudio
    lista_horas_estudio = eliminar_bloques_inexistentes(
        lista_horas_estudio, horas_horario)
    # Elimina las horas sobrantes de lista_horas_familia
    lista_horas_familia = eliminar_bloques_inexistentes(
        lista_horas_familia, horas_horario)
    # Eliminamos horas sobrantes de lista_horas_clases
    lista_horas_clases = eliminar_bloques_inexistentes(
        lista_horas_clases, horas_horario)

    # Se almacenan todas las salidas en una única lista.
    todas_las_salidas = []
    todas_las_salidas.append(horas_horario)
    todas_las_salidas.append(semana_horario)
    todas_las_salidas.append(horas_con_formato)
    todas_las_salidas.append(indice_dias_estudio)
    todas_las_salidas.append(lista_horas_clases)
    todas_las_salidas.append(lista_horas_estudio)
    todas_las_salidas.append(lista_horas_ocio)
    todas_las_salidas.append(lista_horas_familia)

    return todas_las_salidas
