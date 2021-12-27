import tkinter as tk

def interface(ventana_principal):
    # Crear subventana
    preguntas = tk.Tk()

    # Boton para volver
    boton_volver = tk.Button(preguntas, text = "Volver al menú", command = lambda: retornar(ventana_principal,preguntas))
    # Se usa grid para poner el botón
    boton_volver.grid(row = 10, column = 10)

    # Cerrar ventana principal
    ventana_principal.withdraw()
    preguntas.mainloop()

def retornar(ventana_principal,preguntas):
    # Vuelve a abrir la ventana principal
    ventana_principal.deiconify()
    # Cierra la subventana
    preguntas.destroy()
