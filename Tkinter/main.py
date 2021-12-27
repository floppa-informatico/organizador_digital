"""
Este es el archivo principal que se usará 
"""
import tkinter as tk
from files.preguntas import interface

# Bloque por definición
def principal():
    """
    Esta función se encarga de la interfaz grafica del menú principal.
    """
    # Etiqueta
    presentacion_etiqueta = tk.Label(menu_principal, text = "Bienvenid@ a " 
            "Organizador digital, nos adaptamos rápidamente a ti :D!\n"
            "¿Qué desea hacer?")

    # Se posiciona la etiqueta usando grid
    presentacion_etiqueta.grid(row = 0, column = 0, columnspan = 10)

    # Botones
    preguntas_boton = tk.Button(menu_principal, text = "Comenzar o volver \n a"
                        " responder las \n preguntas", padx= 12, pady = 12,
                        command = lambda: interface(menu_principal))
    verhorario_boton = tk.Button(menu_principal, text = "Ver mi horario", 
                            padx= 12, pady = 12)
    modhorario_boton = tk.Button(menu_principal, text = "Modificar mi horario", 
                            padx= 12, pady = 12)
    sientes_boton = tk.Button(menu_principal, text = "¿Cómo te sientes?", 
                            padx= 12, pady = 12)
    uso_boton = tk.Button(menu_principal, text = "¿Cómo se usa \n esta"
                                        " aplicación?", padx= 12, pady = 12)

    # Se usa grid para botones
    preguntas_boton.grid(row = 3, column = 2)
    verhorario_boton.grid(row = 3, column = 4)
    modhorario_boton.grid(row = 3, column = 6)
    sientes_boton.grid(row = 4, column = 2)
    uso_boton.grid(row = 4, column = 4)

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
