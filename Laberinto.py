"""Busqueda de la salida en un laberinto"""

from numpy import *
from ClasePila import pila

# Definimos la matriz que contiene el laberinto.
matrizLaberinto = [[0,1,1,1,1,1,1,1],
                   [1,0,0,0,1,0,0,1],
                   [1,1,1,0,1,1,1,1],
                   [1,0,0,1,1,1,1,1],
                   [1,0,1,0,1,0,1,1],
                   [1,0,1,1,0,1,0,1],
                   [1,0,1,0,0,0,0,1],
                   [1,1,1,1,1,1,1,0]]
laberinto = array(matrizLaberinto)
print("laberinto: \n", laberinto)

# Obtenemos las dimensiones del laberinto.
[filasLaberinto, columnasLaberinto] = laberinto.shape

# Definir las listas para actualizar las coordenadas al rededor de una casilla.
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

# Definir la matriz para registrar con 1 las casillas visitadas.
visitadas = zeros([filasLaberinto, columnasLaberinto], int)

# Definir la pila para guardar la ruta.
ruta = pila()

# Definimos la zelda inicial.
zelda = [0,0]

# Agregamos a la ruta la posición inicial-
ruta.agregar(zelda)
salida = False

# Recorrer el laberinto.
while not ruta.listaVacia() and not salida:
    [x,y] = ruta.obtenerElemento()                  # Asignar el tope a las coordenadas de la ruta.

    if x == filasLaberinto - 1 and y == columnasLaberinto - 1:
        salida = True
        break

    ruta.eliminar()
    nuevo = True

    while nuevo:
        nuevo = False

        for i in range(8):
            rutax = x + dx[i]
            rutay = y + dy[i]

            if rutax > 0 and rutax < filasLaberinto and rutay > 0 and rutay < columnasLaberinto and laberinto[rutax][rutay] == 0 and visitadas[rutax][rutay]:
                zelda = [rutax, rutay]
                ruta.agregar(zelda)
                nuevo = True
                x = rutax
                y = rutay
                visitadas[rutax][rutay] = 1
                break


if salida:
    print("Ruta de slida en reversa")
    while not ruta.listaVacia():
        [x,y] = ruta.obtenerElemento()
        print("x: ",x," y: ",y)
        ruta.eliminar()
else:
    print("No hay ruta de salida.")
