"""
Autores: Sebastián González; Bastián Guerrero; Roberto Galleguillos;
         Ignacio Gomez.
Grupo: 1
Nombre de proyecto: organizador_digital
Sección: 0-C-4
Profesor de Laboratorio: Luis Rios
Profesor de Cátedra: Leonel Gajardo

Descripción del Programa: Este programa se estructura en multiples
archivos en las que cada uno tiene una función especifica. El archivo
main.py es el archivo principal que se encarga de la interfaz del menu
del usuario principalmente.
Luego se encontrará con tres directorios, el primero "lib" en el que
se encontrará archivos principalmente de las interfaces de las
subventanas encargados de la interfaz grafica de usuario (gui).
El segundo directorio siendo "proc" se encontrará archivos encargados
del procesamiento de datos. Y el tercer directorio siendo "data" se encontraran
archivos encargados de leer y escribir con el fin de almacenar los
datos ingresados por el usuario.

Manual de instalación: Para el presente programa se utilizaron varios
módulos externos para asegurar un correcto funcionamiento del mismo y
obtener una solución al problema planteado.
Como requisito previo debe tener instalado python en su dispositivo
terminal.
Para comenzar pulse la tecla windows, seguido de esto escriba cmd y
pulse en la opción donde dice Símbolo del Sistema (asumiendo que tiene
el idioma español configurado en su sistema operativo). 
Luego de esto escriba los siguientes comandos (en orden):

pip install tkinter
pip install tkcalendar
pip install pandas
pip install openpyxl
pip install numpy
pip install xlrd
pip install xlsxwriter

Una vez realizado esto ya puede cerrar la ventana del Símbolo del
Sistema. Se recomienda después de haber realizado esto reiniciar el
equipo para un correcto funcionamiento del programa.
Además, cabe destacar que solo el presente archivo main.py es
ejecutable.
"""
# Bloque de importaciones
import tkinter as tk
from lib.preguntas import interface
from lib.horario import tabla
from lib.calendario import Calendario
from lib.help import ayuda
from lib.sientes import Sientes
from data.archivos import borrar_archivo


# Bloque de definiciones
# Bloque de definición de funciones


def principal():
    """
    Esta función se encarga de la interfaz grafica del menú principal.
    Esta función no tiene entradas, solo se encarga de lo ya mencionado.
    """
    # Etiqueta de bienvenida
    presentacion_etiqueta = tk.Label(
        menu_principal,
        text="Bienvenid@ a Organizador digital, nos"
        " adaptamos rápidamente a ti :D!\n ¿Qué desea "
        "hacer?")

    # Se posiciona la etiqueta usando grid
    presentacion_etiqueta.grid(row=0, column=0, columnspan=10)

    # Botones

    # El boton creado de preguntas_boton lleva al usuario a la sección
    # de preguntas.
    preguntas_boton = tk.Button(
        menu_principal, text="Comenzar o volver \n"
        " a responder las \n preguntas", padx=12,
        pady=12, command=lambda:
        interface(menu_principal))
    # Los siguientes botones solo estarán habilitados una vez el
    # usuario conteste las preguntas
    verhorario_boton = tk.Button(
        menu_principal, text="Ver mi horario", padx=12,
        pady=12, command=lambda: tabla(menu_principal))
    sientes_boton = tk.Button(
        menu_principal, text="¿Cómo te sientes?", padx=12,
        pady=12, command=lambda: Sientes(menu_principal))
    # Este boton estará disponible siempre.
    uso_boton = tk.Button(
        menu_principal,
        text="¿Cómo se usa \n esta aplicación?", padx=12,
        pady=12, command=lambda: ayuda(menu_principal))
    # Este boton se habilitará al igual que verhorario_boton y
    # sientes_boton solo cuando se contesten las preguntas
    calendario_boton = tk.Button(
        menu_principal,
        text="Ver mi calendario", padx=12, pady=12,
        command=lambda: Calendario(menu_principal))
    # Este boton siempre estará habilitado y borra los datos del
    # usuario una vez conteste las preguntas y use el programa.
    borrar_datos_boton = tk.Button(
        menu_principal, text="Borrar mis datos",
        padx=12,
        pady=12,
        command=lambda: borrar_archivo())

    # Se usa grid para botones para poner estos widgets en
    # pantalla.
    preguntas_boton.grid(row=3, column=2)
    verhorario_boton.grid(row=3, column=4)
    calendario_boton.grid(row=3, column=6)
    sientes_boton.grid(row=4, column=2)
    uso_boton.grid(row=4, column=4)
    borrar_datos_boton.grid(row=4, column=6)


# Bloque principal


if __name__ == "__main__":
    # Entrada
    # Creamos la ventana
    menu_principal = tk.Tk()

    # Procesamiento
    # Dimensión de ventana
    menu_principal.title("organizador_digital")
    # Invocamos la función encargada de la interfaz
    principal()

    # Salida
    # Muestra todo en pantalla y responde a la entrada del usuario hasta
    # que el programa se termina (Propio de tkinter)
    menu_principal.mainloop()
