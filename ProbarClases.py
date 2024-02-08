"""Programa para probar las diferentes clases creadas"""

from ClaseArticulo import articulo
from ClasePila import pila

# probar la clase articulo.

articulo1 = articulo(123, 50, 4500)                           # Instanciamos un objeto de la clase artículo.
print("Cantidad disponible: ",articulo1.cantidad," Precio: $",articulo1.precio)      # Imprimimos la cantidad de artículos disponibles y su precio
articulo1.venderArticulo()                                                          # Vender 20 artículos.
articulo1.cantidadActual()                                                          # cantidad disponible.
articulo1.comprarArticulo()                                                         # Comprar 5 artículos.
articulo1.cantidadActual()                                                          # Disponer de 35 artículos.


# Probar la clase pila.

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




