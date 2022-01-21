from tkinter import messagebox
import os


# Bloque por definición


def escribir_archivo(study_days, day, days, sientes):
    """
    Esta función se encarga una vez trabajado los datos para poder
    ordenarlos, los deja en un .txt para llevar estos resultados al
    archivo horario.py.
    Esta función tiene como entrada study_days,day, y days, los tres
    siendo de tipo list.
    Esta función tiene como salida datos.txt siendo este de tipo
    archivo.
    """
    with open("./data/datos.txt", "w") as archivo:
        archivo.write(str(study_days))
        archivo.write("\n")
        archivo.write(str(day))
        archivo.write("\n")
        archivo.write(str(days))
        archivo.write("\n")
        archivo.write(str(sientes))


def borrar_archivo(nombre_archivo):
    """
    Esta función borra lo que estaba escrito en datos.txt. Con el fin
    de evitar cualquier error que se pueda producir durante el programa
    Esta funcion tiene como entrada archivo siendo este de tipo string,
    tiene como salida datos.txt siendo de tipo archivo y un mensaje
    informativo siendo este un tipo de dato propio de tkinter
    """
    if os.path.exists("./data/datos.txt"):
        os.remove("./data/datos.txt")
    if os.path.exists("./data/datos.xlsx"):
        os.remove("./data/datos.xlsx")
    if nombre_archivo == "principal":
        messagebox.showinfo("Se ha completado",
                            "¡Se ha borrado la información éxito!")


def leer_archivo_1():
    """
    Esta funcion tiene el proposito de leer lo que se escribio en el
    archivo para poder trabajar estas listas en horario.py.
    Esta función tiene como salida study_days,day,days, siendo estos
    tres de tipo list.
    """
    with open("./data/datos.txt", "r") as archivo:
        lista_temporal = []
        for i in archivo:
            lista_temporal.append(i)
        study_days = lista_temporal[0]
        day = lista_temporal[1]
        days = lista_temporal[2]
    return study_days, day, days
