""" Introducción a Tkinter"""

from tkinter import *

tk = Tk()                   # Abrir el contenido de la interfaz gráfica, instanciando un objeto de la clase tkinter.

marco = Frame(tk, relief = RIDGE, borderwidth = 2)
marco.pack(fill = BOTH, expand = 1)
tk.title("SALUDO")
tk.geometry('300x200')
mensaje = Label(marco, text = "BIENVENIDO EL MUNDO DE TKINTER")
mensaje.pack(fill = X, expand = 1)
boton = Button(marco, text = 'SALIR', command = tk.destroy)
boton.pack(side = BOTTOM)

tk.mainloop()               # Cerrar el contenido de la interfaz.