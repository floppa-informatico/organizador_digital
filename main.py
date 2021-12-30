"""
Autores: Grupo 1
Nombre de proyecto: organizador_digital
Sección: 0-C-4
Profesor de Laboratorio: Luis Rios
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
Queda pendiente tomar los datos del archivo "datos.txt" ubicado dentro
del directorio "data", poder terminar de organizarlos en un csv, y de 
esta forma a través de pandas y de numpy dejarlo plasmado en el archivo
encargado de la interfaz del horario "horario.py" ubicado en el
directorio de "lib".
Además a través de la pregunta de estado animico "¿como te sientes?",
generar un efecto real en el horario, que solamente pide la respuesta.
Por ultimo, agregarle eventos al calendario.
"""
import tkinter as tk
from lib.preguntas import interface
from lib.horario import tabla
from lib.calendario import Calendario
from lib.help import ayuda
from lib.sientes import Sientes
from data.archivos import borrar_archivo

# Bloque por definición
def principal():
    """
    Esta función se encarga de la interfaz grafica del menú principal.
    Esta función no tiene entradas, solo se encarga de lo ya mencionado
    """
    # Etiqueta
    presentacion_etiqueta = tk.Label(menu_principal, text = "Bienvenid@ a " 
            "Organizador digital, nos adaptamos rápidamente a ti :D!\n"
            "¿Qué desea hacer?")

    # Se posiciona la etiqueta usando grid
    presentacion_etiqueta.grid(row = 0, column = 0, columnspan = 10)

    # Botones
    preguntas_boton = tk.Button(menu_principal, text = "Comenzar o volver \n"
                                " a responder las \n preguntas", padx= 12, 
                                pady = 12, command = 
                                lambda: interface(menu_principal))
    verhorario_boton = tk.Button(menu_principal, text = "Ver mi horario", 
                                padx= 12, pady = 12, command = 
                                lambda: tabla(menu_principal))
    sientes_boton = tk.Button(menu_principal, text = "¿Cómo te sientes?", 
                                padx= 12, pady = 12, command =
                                lambda: Sientes(menu_principal))
    uso_boton = tk.Button(menu_principal, text = "¿Cómo se usa \n esta"
                                " aplicación?", padx= 12, pady = 12, 
                                command = lambda: ayuda(menu_principal))
    calendario_boton = tk.Button(menu_principal, text = "Ver mi calendario", 
                                padx= 12, pady = 12, command = 
                                lambda: Calendario(menu_principal))
    borrar_datos_boton = tk.Button(menu_principal, text = "Borrar datos", 
                                padx= 12, pady = 12, command = 
                                lambda: borrar_archivo())                                        

    # Se usa grid para botones
    preguntas_boton.grid(row = 3, column = 2)
    verhorario_boton.grid(row = 3, column = 4)
    calendario_boton.grid(row = 3, column = 6)
    sientes_boton.grid(row = 4, column = 2)
    uso_boton.grid(row = 4, column = 4)
    borrar_datos_boton.grid(row = 4, column = 6)

# Bloque principal
# Creamos la ventana
menu_principal = tk.Tk()
# Dimensión de ventana
menu_principal.title("organizador_digital")

# Invocamos la función encargada de la interfaz
if __name__ == "__main__":
    principal()

# Muestra todo en pantalla y responde a la entrada del usuario hasta 
# que el programa se termina
menu_principal.mainloop()
