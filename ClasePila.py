"""Clase para un contenedor de datos tipo Pila (primero en entrar, último en salir)"""

class pila():

    # Definir el constructor.
    def __init__(self):
        self.lista = [ ]

    # Validar si la lista está vacia.
    def listaVacia(self):
        vacia = False

        if len(self.lista) == 0:
            vacia = True

        return vacia


    # Agregar un elemento al tope de la pila.
    def agregar(self, nuevoDato):
        self.lista.append(nuevoDato)


    # Eliminar el elemento del tope de la pila.
    def eliminar(self):

        vacia = self.listaVacia()

        if vacia:
            print("Pila vacia")
        else:
            self.lista.pop()                             # eliminamos el último elemento de la lista.


    # Obtener el elemento del tope de la pila.
    def obtenerElemento(self):

        vacia = self.listaVacia()

        if vacia:
            print("Pila vacia")
        else:
            tope = self.lista[-1]

        return tope


    # Imprimir la pila.
    def imprimirPila(self):
        print(self.lista)