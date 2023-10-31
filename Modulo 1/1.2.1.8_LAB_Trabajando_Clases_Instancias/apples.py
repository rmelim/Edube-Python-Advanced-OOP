"""
apples.py -- Elaborado por Rui Duarte dos Santos Melim

Imagine que recibe una tarea de una aplicación que supervisa el proceso de envasado de 
manzanas antes de que las manzanas se envíen a una tienda. El dueño de una tienda ha 
pedido 1000 manzanas, pero el límite de peso total no puede exceder las 300 unidades.

Escriba un código que cree objetos que representen manzanas siempre que se cumplan ambas 
limitaciones. Cuando se supera cualquier limitación, se detiene el proceso de empaquetado y la 
aplicación debe imprimir el número de objetos de clase de manzana creados y el peso total.

La aplicación debe realizar un seguimiento de dos parámetros:

1.- el número de manzanas procesadas, almacenadas como una variable de clase.
2.- el peso total de las manzanas transformadas; almacenado como una variable de clase. 

Supongamos que el peso de cada manzana es aleatorio y puede variar entre 0.2 y 0.5 de una 
unidad de peso imaginaria; utilice una función random.uniform(lower, upper) para crear un número 
aleatorio entre los valores flotantes inferior y superior.
"""

import random


class Apple:
    counter = 0

    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        Apple.counter += 1


class PackApple(Apple):
    total_weight = 0

    def __init__(self):
        super().__init__()
        PackApple.total_weight += self.weight


for i in range(1000):
    apple = PackApple()
    if apple.total_weight >= 300:
        break

print("Total de manzanas empacadas:", apple.counter)
print("Peso total de manzanas empacadas:", apple.total_weight)
