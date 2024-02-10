"""Programa para simular una cola de clientes."""

from ValidacionDeDatos import *
from ClaseCola import cola
from random import *

# Ingresar la cantidad de minutos de la simulación.
tiempoSimulacion = ValidarEntero("Mínutos para la simulación (sin segundos): ","Error, ingrese una cantidad correcta.")

# Ingresar la probabilidad de ingreso de un cliente.
probabilidadIngreso = ValidarReal("Probabilidad de ingreso: ","Error, ingrese una cantidad correcta.")

# Ingresar el tiempo máximo de atención en mínutos.
tiempoAtencion = ValidarEntero("Tiempo de atención: ","Error, ingrese una cantidad correcta.")

# Instanciar la cola para almacenar los tiempos de atención de los clientes.
colaTiempos = cola()

# Inicializamos los tiempos.
tiempoReloj = 0                                 # Contador para el proceso de simulación.
tiempoFrente = 0                                # Tiempo del cliente en la primera posición de la cola.

while tiempoReloj < tiempoSimulacion:
    probabilidadLlegada = random()              # probabilidad de llegada de un cliente al frente.

    if probabilidadLlegada < probabilidadIngreso:
        atencion = randint(1, tiempoAtencion)       # Duración de la atención del cliente.
        colaTiempos.agregar(atencion)                  # Agregamos a la cola de tiempos.

    if tiempoFrente <= 0:
        if not colaTiempos.colaVacia():                # El cliente del frente terminó.
            tiempoFrente = colaTiempos.obtenerElemento()    # Iniciamos el tiempo del frente.
            colaTiempos.eliminar()
    else:
        tiempoFrente -= 1
        tiempoReloj += 1

numeroClientes = 0
while not colaTiempos.colaVacia():
    colaTiempos.eliminar()
    numeroClientes += 1
print("cantidad de clientes que quedaron: ",numeroClientes)
