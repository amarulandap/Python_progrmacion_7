"""Clase para una estructura de datos tipo cola(primero en ingresar, primero en salir)"""

class cola():

    # Método constructor.
    def __init__(self):
        self.lista = [ ]


    # Método para agregar un elemento al final de la cola(Poner).
    def agregar(self, nuevoDato):
        self.lista.append(nuevoDato)


    # Método para validar si la cola esta vacía.
    def colaVacia(self):

        vacia = False

        if len(self.lista) == 0:
            vacia = True

        return vacia


    # Método para eliminar el elemento del frente de la cola.
    def eliminar(self):

        vacia = self.colaVacia()

        if vacia:
            print("la cola esta vacía.")
        else:
            del self.lista[0]


    # Método para obtener el elemento del frente de la cola.
    def obtenerElemento(self):

        vacia= self.colaVacia()

        if vacia:
            print("la cola esta vacía.")
        else:
            primerElemento = self.lista[0]

        return primerElemento


    # Método para imprimir la cola.
    def imprimirCola(self):
        print(self.lista)

