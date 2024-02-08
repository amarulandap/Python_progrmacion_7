"""Introducción a la POO"""

from ValidacionDeDatos import ValidarEntero

class articulo():

    # Definimos el método constructor.
    def  __init__(self, codigo, cantidad, precio):
        self.codigo = codigo
        self.cantidad = cantidad
        self.precio = precio


    # Definir el método para mostrar la cantidad actual.
    def cantidadActual(self):
        print("Cantidad actual: ",self.cantidad)


    # Definir el método para mostrar el precio del artículo.
    def precioArticulo(self):
        print("Precio: ",self.precio)


    # Definir el método para vender un artículo.
    def venderArticulo(self):
        while True:
            cantidadAVender = ValidarEntero("Cantidad: ", "Error, ingrese una cantidad correcta.")

            if cantidadAVender > self.cantidad:
                print("Error, ingrese una cantidad correcta.")
                continue

            else:
                self.cantidad -= cantidadAVender

            break


    # Definir el método para comprtar un artículo.
    def comprarArticulo(self):
        while True:
            cantidadAComprar = ValidarEntero("Cantidad: ", "Error, ingrese una cantidad correcta.")

            if cantidadAComprar >= self.cantidad:
                print("Error, ingrese una cantidad correcta.")
                continue

            else:
                self.cantidad += cantidadAComprar

            break
