import tkinter as tk
from tkinter import messagebox
import data.archivos as archivos


# Bloque por definición
def Sientes(ventana_principal):
    """
    Esta función es la encargada de crear la subventana para la 
    sección "¿como te sientes?" que tendrá acceso el usuario.
    Esta función tiene como entrada la ventana del menú, siendo
    este un dato propio de tkinter.
    """
    # Leer txt para comprobar que el archivo tenga datos o no
    lista_comprobacion = archivos.leer_archivo_2()
    if lista_comprobacion == []:
        messagebox.showerror("Error","¡Primero debes completar las"
                            " preguntas!")
    else:
        # Se declara la variable respuesta_0 en caso de que el usuario no
        # escriba nada 
        # Crear subventana
        sentir_ventana = tk.Toplevel(ventana_principal)
        # Crear titulo
        sentir_ventana.title("organizador_digital")

        # Crear etiqueta para pregunta
        pregunta_0 = tk.Label(sentir_ventana, text = "¿Como te has sentido?"
                                                " (Escriba bien o mal)")


        # Entrada para introducir texto
        respuesta_0 = tk.Entry(sentir_ventana)

        # Se crea boton
        boton_11 = tk.Button(sentir_ventana, text= "Enviar", padx = 20, 
                    pady = 10, command = lambda: r_1(respuesta_0))

        # Poner los widgets en pantalla
        pregunta_0.grid(column = 0,row = 0)
        respuesta_0.grid(column = 0,row = 1)
        boton_11.grid(column = 0,row = 2)

        # Boton para volver
        for i_para_etiqueta in range(1,3):
            etiqueta_vacia = tk.Label(sentir_ventana, text="").grid(
                            row = i_para_etiqueta + 2, column = 1)

        boton_volver = tk.Button(sentir_ventana, text = "Volver al menú", 
                             padx = 20, pady = 10, command = lambda: 
                             retornar(ventana_principal,sentir_ventana,
                             respuesta_0))
        boton_volver.grid(row = 5, column = 1)

        # Cerrar ventana principal
        ventana_principal.withdraw()


def retornar(ventana_principal,sentir_ventana, respuesta):
    """
    Esta funcion tiene el propósito de cerrar la subventana
    y volver al menu.
    """
    # Verifica si la respuesta del usuario es la respuesta que se pide
    final = False
    if respuesta.lower() == "bien" or respuesta.lower() == "mal":
            final = True
    
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    sentir_ventana.destroy()

    if final:
        # Si es "bien" o "mal", entonces la introduccion de datos ha
        # sido exitoso.
        messagebox.showinfo("Ha sido un éxito","Has introducido el dato"
                            " correctamente")
    else:
        # Informa al usuario que no siguió la estructura propuesta.
        messagebox.showwarning("Advertencia","No ha completado la "
                                "pregunta o no seguiste la estructura"
                                " planteada")


def r_1(respuesta):
    """
    Esta funcion se encarga se obtener la respuesta y poder
    pasarlo de un tipo de dato propio de tkinter a un string, además
    de un primer filtro si es que el dato corresponde a la estructura
    que se pide.
    Esta función tiene como entrada la respuesta al widget "Entry" 
    llamada "respuesta" como parametro formal. Esta función tiene como
    salida el elemento siendo este de tipo string, en donde se retorna
    el elemento si es que cumple con lo ya mencionado.
    """
    # Se obtiene la respuesta y lo pasa a string
    elemento = respuesta.get()
    # Clasifica si es que lo que ingresó el usuario corresponde en una
    # primera instancia a lo pedido
    if elemento == "" or elemento == " ":
        messagebox.showerror("Error","¡Es espacio está vacío!")
    elif elemento[0] == " " and elemento[1] != " ":
        messagebox.showerror("Error","¡Hay un espacio al inicio!")
    else:
        # Si cumple, se retorna el elemento a la función retornar
        return respuesta
