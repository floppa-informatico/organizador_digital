import tkinter as tk
window=tk.Tk()
window.title("FT Files")
window.geometry("500x300")

texto=tk.Label(window,text="Introduce un numero de serie:")
texto.pack()
#NumSerie=StringVar()
serialEntry=tk.Entry(window)
serialEntry.pack()

def newWindow(event):
    print("the new window is open")
    new_window = tk.Toplevel(window)

    new_label = tk.Label(new_window)
    new_label.config(text="El codigo de serie es: " + serialEntry.get())
    new_label.place(x=30,y=30)

    window.iconify()

serialEntry.bind("<Return>", newWindow)

window.mainloop()