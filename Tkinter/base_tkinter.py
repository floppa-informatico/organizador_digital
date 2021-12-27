import tkinter

# Crear una ventana
ventana = tkinter.Tk()

# Cambiar tamaño de pantalla
ventana.geometry("400x300")

# Estiquetas

# Crear etiqueta, en donde se va a poner esta etiqueta, en donde va a vivir
# etiqueta = tkinter.Label(ventana, text = "hola mundo", bg = "pink")
# Poner algo en pantalla, como argumento poner side es poner el lugar donde se pondrá la etiqueta
# etiqueta.pack(side = tkinter.RIGHT)
# Poder estirar el texto se usa como argumento fill para x
# etiqueta.pack(fill = tkinter.X)
# Estirar texto por el eje y
# etiqueta.pack(fill = tkinter.Y, expand = True)
# Estirar texto por toda la pantalla
# etiqueta.pack(fill = tkinter.BOTH, expand = True)

# Botones

# Agregar función para funcionalidad del boton
#def saludo(nombre):
#    print("hola")

# Crear boton, en donde se va a poner el boton, el texto, el tamaño en x e y, y conecta función con boton.
# Pasando argumentos se le agrega la palabra lambda con los parentesis correspondientes de la función
# boton1 = tkinter.Button(ventana, text = "Presiona", padx = 40, pady = 50, command = lambda: saludo())
# Se pone en pantalla
# boton1.pack()
# Introducir texto
# cajaTexto = tkinter.Entry(ventana, font = "Helvetica 20")
# Se pone en pantalla
# cajaTexto.pack()

"""
ejemplo practico

# Introducir texto
cajaTexto = tkinter.Entry(ventana, font = "Helvetica 20")
# Se pone en pantalla
cajaTexto.pack()

etiqueta = tkinter.Label(ventana)
etiqueta.pack()


def texto_caja():
    text20 = cajaTexto.get()
    etiqueta["text"] = text20


boton1 = tkinter.Button(ventana, text = "click", command = texto_caja)
boton1.pack()
"""

# Método grid divide la ventana en columnas y filas (acordarse de matrices)
boton1 = tkinter.Button(ventana, text = "boton1", width = 20, height = 5)
boton2 = tkinter.Button(ventana, text = "boton2", width = 20, height = 5)
boton3 = tkinter.Button(ventana, text = "boton3", width = 20, height = 5)

# Usamos grid
boton1.grid(row = 0, column = 0)
boton2.grid(row = 1, column = 1)
boton3.grid(row = 2, column = 2)

# Lleva el registro de todo lo que sucede en el programa
ventana.mainloop()
