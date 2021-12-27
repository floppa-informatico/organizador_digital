import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, VERTICAL, Y

def barra_de_desplazamiento(preguntas):
    # Crear un Frame principal donde se contendrá todo
    main_frame = tk.Frame(preguntas)
    main_frame.pack(fill = BOTH, expand = True)

    # Crear un Canvas
    canvas_1 = tk.Canvas(main_frame)
    canvas_1.pack(side = LEFT, fill = BOTH, expand = True)

    # Agregar Scrollbar al Canvas
    my_scrollbar = tk.Scrollbar(main_frame, orient = VERTICAL, command = canvas_1.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    # Configurar el Canvas para tener el scrollbar
    canvas_1.configure(yscrollcommand = my_scrollbar.set)
    canvas_1.bind("<Configure>", lambda e: canvas_1.configure(scrollregion = canvas_1.bbox("all")))

    # Crear otro Frame dentro del Canvas
    second_frame = tk.Frame(canvas_1)

    # Agregar el nuevo Frame a la ventana en el Canvas
    canvas_1.create_window((0,0), window = second_frame, anchor="nw")
    return second_frame
