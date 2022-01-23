# Bloque de importaciones
import tkinter as tk
from tkinter import messagebox
from datetime import date
import tkcalendar as calendar
import datetime
from lib.preguntas import retornar
import os


# Bloque de definiciones
# Bloque de definición de funciones

def Calendario(ventana_principal):
    """
    Esta función es la encargada de crear la subventana para el
    calendario que tendrá acceso el usuario.
    Esta función tiene como entrada la ventana del menú, siendo
    este un dato propio de tkinter.
    Esta función tiene como salida la subventana calendari0 siendo este
    un tipo de dato propio de tkinter.
    """
    # Leer txt para comprobar que el archivo tenga datos o no
    if not(os.path.exists("./data/datos.txt"))\
            and not(os.path.exists("./data/datos.xlsx")):
        messagebox.showerror(
            "Error", "¡Primero debes completar las preguntas!")
    else:
        # Crear subventana
        calendari0 = tk.Toplevel(ventana_principal)
        # Crear titulo
        calendari0.title("organizador_digital")
        # Obtener fecha actual
        tiempo = datetime.datetime.now()
        dia = int(tiempo.strftime("%d"))
        mes = int(tiempo.strftime("%m"))
        year = int(tiempo.strftime("%Y"))
        # Creamos un frame donde se pondrá el calendario y el título.
        marco = tk.Frame(calendari0)
        marco.grid(row=0, column=2, columnspan=4, rowspan=2, pady=20)
        # Poner título
        titulo = tk.Label(
            marco,
            font="Arial 28 bold underline",
            bg="orange",
            text="Mi calendario")
        # Poner titulo en pantalla
        titulo.pack(fill="both", expand=True)
        # Poner instrucciones en pantalla
        instrucciones = tk.Label(
            calendari0,
            font="Arial 12",
            text="Aqui puede agregar sus citas y cosas importantes\n"
            "Seleccione el día en el calendario y escriba abajo\n"
            "lo que quiera agregar a esa fecha.")
        # Se pone en pantalla instrucciones
        instrucciones.grid(row=2, column=5)

        # Entrada para poder introducir eventos al calendario
        respuesta = tk.Entry(calendari0)
        respuesta_1 = respuesta
        # Se pone en pantalla la entrada
        respuesta.grid(row=3, column=5)

        # Crear calendario
        mindate = datetime.date(year=year, month=mes, day=dia)
        cal = calendar.Calendar(marco, selectmode="day", mindate=mindate, year=year,
                                mouth=mes, day=dia)
        cal.pack(fill="both", expand=True)

        # Se ponen los eventos guardados del calendario
        lista_iterador = escribir_eventos(cal, calendari0)

        # Se envia respuesta al pulsar enter
        respuesta.bind("<Return>", lambda event, calendari0=calendari0: guarda_datos_calendario(
            event, calendari0, cal, respuesta_1, lista_iterador))

        # Boton para volver
        boton_volver = tk.Button(
            calendari0,
            text="Volver al menú", padx=20, pady=10,
            command=lambda:
            retornar(ventana_principal, calendari0))
        # Se usa grid para poner el botón
        for i_para_etiqueta in range(2, 4):
            etiqueta_vacia = tk.Label(calendari0, text="").grid(
                row=i_para_etiqueta + 32, column=6)
        boton_volver.grid(row=36, column=6)

        # Cerrar ventana principal
        ventana_principal.withdraw()


def retornar(ventana_principal, calendar):
    """
    Esta función tiene el propósito de cerrar la subventana
    y volver al menú.
    Tiene como entrada ventana_principal y calendar siendo
    estos tipos de datos propios de tkinter.
    """
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    calendar.destroy()


def guarda_datos_calendario(event, calendari0, cal, respuesta_1, lista_iterador):
    """
    Esta función se encarga de cuando el usuario introduza el nombre
    para el evento, guarde el nombre y la fecha seleccionada para de
    esta forma guardarlo también en un .txt llamado eventos.txt.
    Esta función tiene como entrada event siendo un parametro del
    método bind proporcionado por tkinter, calendari0, cal, y
    respuesta_1 tipos de datos propios de tkinter, y lista_iterador
    siendo este de tipo list.
    Esta función tiene como salida eventos.txt siendo este de tipo
    archivo.
    """
    # Se obtiene la fecha que marcó en el calendario
    respuesta = respuesta_1.get()
    fecha = cal.selection_get()
    # Se forma el string que se escribirá en el archivo
    linea = respuesta + "," + str(fecha) + "\n"
    # Se guarda la respuesta con su respectiva fecha marcada
    # en el calendario en eventos .txt
    with open("./data/eventos.txt", "a") as archivo:
        archivo.write(linea)
    # Escribe el evento en el calendario
    escribir_nuevo_evento(cal, calendari0, respuesta, lista_iterador, linea)


def escribir_nuevo_evento(cal, calendari0, respuesta, lista_iterador, linea):
    """
    Esta función se encarga de escribir el nuevo evento introducido por
    el usuario en el calendario. 
    Esta función tiene como entrada cal y calendari0 siendo estos de
    tipo de dato propio de tkinter, respuesta siendo de tipo string,
    lista_iterador siendo de tipo list, y linea siendo tipo string.
    """
    # Se agrega un nuevo indice a lista_iterador
    if len(lista_iterador) != 0:
        indice = lista_iterador[-1] + 1
        lista_iterador.append(indice)
    # Se obtiene el nombre del evento
    evento_nombre = f"evento_{indice}"
    # Se separa en una lista
    linea_0 = linea.split(",")
    # Se separa el tiempo para poder ubicar el
    # calendario en la fecha pedida
    tiempo = linea_0[-1].split("-")
    # Se obtiene la fecha
    fecha = datetime.date(year=int(tiempo[0]), month=int(
        tiempo[1]), day=int(tiempo[2]))
    # Se marca el evento en el calendario
    cal.calevent_create(fecha, linea_0[0], evento_nombre)
    # Se marca con color rojo el dia pedido
    cal.tag_config(f"evento_{indice}", background="red", foreground="yellow")
    # Dia actual
    today = date.today()
    # Se obtiene texto para etiqueta
    display = display_etiqueta(fecha, today, respuesta)
    # Se crea boton y etiqueta
    dias = tk.Label(calendari0, text=display)
    dias.grid(row=3+indice, column=0)
    eliminar = tk.Button(calendari0, text="x", command=lambda: eliminar_evento_reciente(
        dias, eliminar, evento_nombre, cal, linea))
    eliminar.grid(row=3+indice, column=1)


def eliminar_evento_reciente(dias, eliminar, evento_nombre, cal, linea):
    """
    Esta función es invocada en el caso de que el usuario elimine el
    evento recientemente agregado al calendario. Esta función tiene
    como entrada dias y eliminar siendo estos de tipo de dato propio
    de tkinter, evento_nombre siendo este de tipo string, cal siendo
    de tipo de dato propio de tkinter, y linea siendo este de tipo
    string.
    Esta función tiene como salida eventos.txt, siendo este de tipo
    archivo.
    """
    # Se obtienen las demas lineas
    with open("./data/eventos.txt", "r") as archivo:
        lineas = archivo.readlines()
    # Se elimina la etiqueta
    dias.destroy()
    # Se elimina el boton para eliminar
    eliminar.destroy()
    # Se marca con color rojo el dia pedido
    cal.tag_config(evento_nombre, background="white", foreground="black")
    # Se elimina evento del calendario
    cal.calevent_remove(evento_nombre)
    # Se abre el archivo en modo escritura
    with open("./data/eventos.txt", "w") as archivo:
        # Se remueve el evento
        lineas.remove(linea)
        # Se vuelven a escribir los demas eventos que no han sido eliminados
        for linea_0 in lineas:
            archivo.write(linea_0)


def display_etiqueta(d1, d2, evento):
    """
    Esta función se encarga de formar los mensajes que visualizará el
    usuario para indicarle cuantos días faltan para que se concrete el
    evento.
    Esta función tiene como entrada d1 y d2 siendo estos de tipo
    datetime, y evento siendo este de tipo string.
    Esta función tiene como salida display siendo de tipo string.
    """
    # Se obtiene la diferencia de las dos fechas para indicar cuanto
    # falta para la fecha indicada en el evento
    tb = str(d1-d2)
    nod = tb.split(" ")
    # Se hace la estructura para la etiqueta
    display = "Faltan %s dias para %s" % (nod[0], evento)
    return display


def escribir_eventos(cal, calendari0):
    """
    Esta función se encarga de escribir los eventos almacenados en
    eventos.txt una vez abierto la subventana calendari0.
    Esta función tiene como entrada cal y calendari0 siendo estos
    tipos de datos propios de tkinter.
    Esta función tiene como salida lista_iterador siendo este de tipo
    list.
    """
    # Se comprueba de que si existe eventos .txt
    if os.path.exists("./data/eventos.txt"):
        # Se obtienen todos las demas lineas
        archivo = open("./data/eventos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        # Lee eventos .txt
        archivo = open("./data/eventos.txt", "r")
        iterador = 0
        lista_iterador = []
        # Elimina el evento si existe, para evitar que se duplique
        cal.calevent_remove()
        # Se comienza a leer linea por linea
        for linea in archivo:
            # Se obtiene el nombre del evento
            evento_nombre = f"evento_{iterador}"
            # Se quitan los saltos de linea
            linea_0 = linea.strip()
            # Se separa en una lista
            linea_0 = linea_0.split(",")
            # Se separa el tiempo para poder ubicar el
            # calendario en la fecha pedida
            tiempo = linea_0[-1].split("-")
            # Se obtiene la fecha
            fecha = datetime.date(year=int(tiempo[0]), month=int(
                tiempo[1]), day=int(tiempo[2]))
            # Se marca el evento en el calendario
            cal.calevent_create(fecha, linea_0[0], evento_nombre)
            # Dia actual
            today = date.today()
            # Se pone en pantalla cuantas horas faltan para
            # x dia puesto como evento
            dias_faltantes(linea_0[0], fecha, today,
                           iterador, evento_nombre, lineas, linea, archivo, calendari0, cal)
            # Se marca con color rojo el dia pedido
            cal.tag_config(f"evento_{iterador}",
                           background="red", foreground="yellow")
            # Agregar iterador a lista_iterador
            lista_iterador.append(iterador)
            iterador += 1
        archivo.close()
        return lista_iterador


def dias_faltantes(evento, d1, d2, iterador, evento_nombre, lineas, linea, archivo, calendari0, cal):
    """
    Esta función tiene el propósito de escribir las etiquetas que
    visualizará el usario para saber los días faltantes para un
    determinado evento.
    Esta función tiene como entrada evento siendo este de tipo string,
    d1 y d2 siendo datos de tipo datetime, iterador siendo de tipo int,
    evento_nombre siendo este de tipo string, lineas siendo de tipo
    list, linea siendo de tipo string, archivo siendo de tipo archivo,
    calendari0 y cal siendo tipos de datos propios de tkinter.
    """
    # Se obtiene la diferencia de las dos fechas para indicar cuanto
    # falta para la fecha indicada en el evento
    tb = str(d1-d2)
    nod = tb.split(" ")
    # Se hace la estructura para la etiqueta
    display = "Faltan %s dias para %s" % (nod[0], evento)
    # Se crea la etiqueta
    dias = tk.Label(calendari0, text=display)
    dias.grid(row=3+iterador, column=0)
    eliminar = tk.Button(calendari0, text="x", command=lambda: eliminar_evento(
        dias, eliminar, evento_nombre, lineas, linea, archivo, cal))
    eliminar.grid(row=3+iterador, column=1)


def eliminar_evento(dias, eliminar, evento_nombre, lineas, linea, archivo, cal):
    """
    Esta función es invocada si el usuario pulsa el botón de eliminar
    un determinado evento.
    Esta función tiene como entrada dias y eliminar siendo tipos de
    datos propios de tkinter, evento_nombre siendo de tipo string,
    lineas siendo de tipo list, linea siendo de tipo string, archivo
    siendo de tipo archivo, y cal siendo tipo de dato propio de
    tkinter.
    Esta función tiene como salida eventos.txt siendo este de tipo
    archivo.
    """
    # Se elimina la etiqueta
    dias.destroy()
    # Se elimina el boton para eliminar
    eliminar.destroy()
    # Cierra archivo
    archivo.close()
    # Se marca con color rojo el dia pedido
    cal.tag_config(evento_nombre, background="white", foreground="black")
    # Se elimina evento del calendario
    cal.calevent_remove(evento_nombre)
    # Se abre el archivo en modo escritura
    with open("./data/eventos.txt", "w") as archivo:
        # Se remueve el evento
        lineas.remove(linea)
        # Se vuelven a escribir los demas eventos que no han sido eliminados
        for linea_0 in lineas:
            archivo.write(linea_0)
    archivo = open("./data/eventos.txt", "r")
