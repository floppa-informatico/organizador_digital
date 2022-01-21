import tkinter as tk

# Bloque por definición


def ayuda(ventana_principal):
    """
    Esta función es la encargada de crear la subventana de la sección
    de ayuda.
    Esta función tiene como entrada la ventana del menú prinicipal
    siendo este dato propio de tkinter.
    """
    # Crear subventana
    # Procesamiento
    ventana_ayuda = tk.Toplevel(ventana_principal)
    # Crear titulo
    ventana_ayuda.title("organizador_digital")

    # Salida
    # Crear etiqueta para información de ayuda
    etiqueta = tk.Label(
        ventana_ayuda,
        text="Para comenzar, usted debe completar las preguntas que"
        " se realizará a usted para personalizar toda la \napp"
        " acorde a sus necesidades. El cual se le pide por favor"
        " respetar la estructura pedida, de lo contario\nle dará"
        " error. Una vez que complete las preguntas usted tendrá"
        " acceso a su horario, y calendario.\nTambién usted podrá"
        " acceder a la sección del “¿como te sientes?” en el que se"
        " le re acomodará los\nhorarios de estudios en caso de que se"
        " encuentre estresado, agustiado, etc.\n""\n""\n"
        "Esta app esta diseñada para ser totalmente adaptable a sus"
        " necesidades, dandole tempo para también\ntener tiempo para"
        " el ocio, descansar, entre otros.")
    # Poner etiqueta en pantalla
    etiqueta.grid(column=1, row=0)

    # Boton para volver
    for i_para_etiqueta in range(1, 3):
        etiqueta_vacia = tk.Label(ventana_ayuda, text="").grid(
            row=i_para_etiqueta + 1, column=2)
    boton_volver = tk.Button(
        ventana_ayuda,
        text="Volver al menú", padx=20, pady=10,
        command=lambda:
        retornar(ventana_principal, ventana_ayuda))
    boton_volver.grid(row=4, column=2)

    # Cerrar ventana principal
    ventana_principal.withdraw()


def retornar(ventana_principal, ventana_ayuda):
    """
    Esta función tiene el propósito de cerrar la subventana
    y volver al menú.
    """
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    ventana_ayuda.destroy()
