"""
delicacy.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
La tarea expuesta en el LAB 4.1.1.12 fue muy fácil. Ahora vamos a reelaborar un poco el código:

* Introduzca la clase Delicacy para representar un manjar genérico. Los objetos de esta clase 
reemplazarán a los diccionarios del LAB 4.1.1.12. Atributos sugeridos: name, price, weight.
* La clase debe implementar el método __str__() para representar cada estado del objeto.
* Experimente con los métodos deepcopy() y copy() y para ver la diferencia en la forma en que 
cada método copia los objetos.
"""

from copy import deepcopy, copy


class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"Name: {self.name} - Price: {self.price} - Weight: {self.weight}"


warehouse = []

warehouse.append(Delicacy(name="Lolly Pop", price=0.4, weight=133))
warehouse.append(Delicacy(name="Licorice", price=0.1, weight=251))
warehouse.append(Delicacy(name="Chocolate", price=1, weight=601))
warehouse.append(Delicacy(name="Sours", price=0.01, weight=513))
warehouse.append(Delicacy(name="Hard candies", price=0.3, weight=433))

# Using deepcopy()
warehouse_deep = deepcopy(warehouse)
for item in warehouse_deep:
    if item.weight > 300:
        item.price *= 0.8

print("*" * 10, "Source list of candies", "*" * 10)
for item in warehouse:
    print(item)

print("*" * 10, "Proposal price list of candies", "*" * 10)
for item in warehouse_deep:
    print(item)

# Using copy()
warehouse_copy = copy(warehouse)
for item in warehouse_copy:
    if item.weight < 300:
        item.weight += 100

print("*" * 10, "New source list of candies", "*" * 10)
for item in warehouse:
    print(item)

print("*" * 10, "Modifying the weights", "*" * 10)
for item in warehouse_copy:
    print(item)
