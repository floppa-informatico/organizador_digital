def etiqueta_y_boton(lineas, lista_display, lista_iterador):
    for iterador in lista_iterador:
        # Se crea una etiqueta
        dias = tk.Label(calendari0, text=lista_display[iterador])
        dias.grid(row=3+iterador, column=0)
        # Se obtiene el nombre del evento
        evento_nombre = f"evento_{iterador}"
        # Se obtiene la linea
        linea = lineas[iterador]
        # Botón para eliminar el evento
        eliminar = tk.Button(calendari0, text="x", command=lambda: eliminar_evento(
            dias, eliminar, evento_nombre, lineas, linea))
        eliminar.grid(row=3+iterador, column=1)