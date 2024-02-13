""" Clase para ingresar y validar un dato """

from tkinter import *

class validacion(Frame):

    # Constructor.
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.crearWidgets()


    def crearWidgets(self):
        self.instruccion = Label(self, "Ingrese la contraseña: ")
        self.instruccion.grid(row = 1, column = 1, columnspan = 2, sticky = W)
        self.contraseña = Entry(self)
        self.contraseña.grid(row = 3, column = 3, sticky = W)
        self.botonEnviar = Button(self, text = 'Ingrese', command = self.verificar)
        self.botonEnviar.grid(row = 5, column = 3, sticky = W)
        self.texto = Text(self, width = 35, height = 5, wrap = WORD)
        self.texto.grid(row = 7, column = 1, columnspan = 2, sticky = W)


    def verificar(self):
        contenido = self.contraseña.get()
        if contenido == 'secreto':
            mensaje = "Acceso permitido"
        else:
            mensaje = "Acceso denegado"

        self.texto.delete(0.0, END)
        self.texto.insert(0.0, mensaje)



