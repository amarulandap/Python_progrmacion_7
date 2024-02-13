"""Programa para probar las diferentes clases creadas"""

from ClaseArticulo import articulo
from ClasePila import pila
from ClaseCola import cola
from ClaseEmpleado import empleado
from GuiConPoo import boton
from IngresoYVerificacionDeDatos import validacion
from tkinter import *

# probar la clase articulo.

articulo1 = articulo(123, 50, 4500)                           # Instanciamos un objeto de la clase artículo.
print("Cantidad disponible: ",articulo1.cantidad," Precio: $",articulo1.precio)      # Imprimimos la cantidad de artículos disponibles y su precio
articulo1.venderArticulo()                                                          # Vender 20 artículos.
articulo1.cantidadActual()                                                          # cantidad disponible.
articulo1.comprarArticulo()                                                         # Comprar 5 artículos.
articulo1.cantidadActual()                                                          # Disponer de 35 artículos.


# Probar la clase pila.

print("\n")
pila1 = pila()
pila1.agregar(1)
pila1.imprimirPila()
pila1.agregar(3)
pila1.imprimirPila()
pila1.agregar(5)
pila1.imprimirPila()
pila1.agregar(7)                                        # Agregar 4 elementos a la pila, los vamos mostrando a medida que se agregan
pila1.imprimirPila()

pila1.eliminar()
pila1.imprimirPila()
pila1.eliminar()
pila1.imprimirPila()                                    # Eliminamos dos elementos e imprimimos. Mostrar los elementos [1, 3]
tope = pila1.obtenerElemento()                          # Obtenemos el tope.
print("Tope: ",tope)                                    # 3.


# Probar la clase cola.

print("\n")
cola1 = cola()
cola1.agregar(34)
cola1.imprimirCola()
cola1.agregar(53)
cola1.imprimirCola()
cola1.agregar(79)
cola1.imprimirCola()
cola1.agregar(25)
cola1.imprimirCola()
primerElemento = cola1.obtenerElemento()
print("Primer elemento: ",primerElemento)
cola1.eliminar()
primerElemento = cola1.obtenerElemento()
print("Primer elemento: ",primerElemento)


# probar la clase empleado.

print("\n")
empleado1 = empleado(123, 2000000, 21000, 10, "casado", 2)
empleado1.detallesDePago()


# Probar la clase para crear los botones.

marco = Tk()

marco.title(" PRUEBA BOTÓN")
marco.geometry("300x200")

botonPrueba = boton(marco)

marco.mainloop()


# probar la calse para validar un dato.

marco1 = Tk()

marco1.title("VALIDAR VALOR INGRESADO")
marco1.geometry("400x300")

validarDato = validacion(marco1)

marco1.mainloop()



