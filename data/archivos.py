def escribir_archivo(study_days,day,days):
    with open("organizador_digital/data/datos.txt","w") as archivo:
        archivo.write(str(study_days))
        archivo.write("\n")
        archivo.write(str(day))
        archivo.write("\n")
        archivo.write(str(days))
    return True


def borrar_archivo():
    with open("organizador_digital/data/datos.txt","w") as archivo:
        archivo.write("")
    return True


def leer_archivo():
    with open("organizador_digital/data/datos.txt","r") as archivo:
        lista_temporal = []
        for i in archivo:
            lista_temporal.append(i)
        study_days = lista_temporal[0]
        day = lista_temporal[1]
        days = [2]
    return study_days,day,days
