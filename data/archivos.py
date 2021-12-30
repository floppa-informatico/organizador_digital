# Bloque por definición
def escribir_archivo(study_days,day,days):
    """
    Esta función se encarga una vez trabajado los datos para poder
    ordenarlos, los deja en un .txt para llevar estos resultados al 
    archivo horario.py.
    Esta función tiene como entrada study_days,day, y days, los tres
    siendo de tipo list.
    """
    with open("./data/datos.txt","w") as archivo:
        archivo.write(str(study_days))
        archivo.write("\n")
        archivo.write(str(day))
        archivo.write("\n")
        archivo.write(str(days))


def borrar_archivo():
    """
    Esta función borra lo que estaba escrito en datos.txt. Con el fin
    de evitar cualquier error que se pueda producir durante el programa
    Esta funcion no tiene entrada y ni salida
    """
    with open("./data/datos.txt","w") as archivo:
        archivo.write("")


def leer_archivo_1():
    """
    Esta funcion tiene el proposito de leer lo que se escribio en el
    archivo para poder trabajar estas listas en horario.py.
    Esta función tiene como salida study_days,day,days, siendo estos
    tres de tipo list.
    """
    with open("./data/datos.txt","r") as archivo:
        lista_temporal = []
        for i in archivo:
            lista_temporal.append(i)
        study_days = lista_temporal[0]
        day = lista_temporal[1]
        days = lista_temporal[2]
    return study_days,day,days


def leer_archivo_2():
    """
    Esta funcion tiene el proposito de leer el archivo y verificar si
    el archivo .txt está vacio o no.
    Esta funcion tiene como salida una lista temporal, siendo esta
    de tipo list.
    """
    with open("./data/datos.txt","r") as archivo:
        lista_temporal = []
        for i in archivo:
            lista_temporal.append(i)
    return lista_temporal
