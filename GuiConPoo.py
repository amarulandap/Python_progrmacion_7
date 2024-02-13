"""Interfaz gráfica de usuario con POO"""

# Aplicación para crear un botón con POO.

from tkinter import *

class boton(Frame):

    # Constructor.
    def __init__(self, master):
        Frame.__init__(self, master)            # Invocamos el constructor de la clase frame.
        self.grid()
        self.crearWidgets()


    # Método crear widgets.
    def crearWidgets(self):
        self.boton1 = Button(self, text = "Mensaje")
        self.boton1.grid()
        # A través del método configure de la clase Button puedo darle valor al texto de los botones.
        # self.boton1.configure(text = "mensaje")
        # self.boton1['text'] = 'mensaje'


