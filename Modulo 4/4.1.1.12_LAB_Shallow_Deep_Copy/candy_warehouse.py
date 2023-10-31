"""
candy_warehouse.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
Imagina que te han contratado para ayudar a administrar un almacén de dulces.

La tarea:
1.- Tu tarea es escribir un código que preparará una propuesta de precios reducidos para los 
caramelos cuyo peso total supere las 300 unidades de peso (no nos importa si son kilogramos 
o libras)
2.- Su entrada es una lista de diccionarios; Cada diccionario representa un tipo de caramelo. 
Cada tipo de caramelo contiene una clave titulada 'peso' (weight), que debería llevarte a los 
detalles del peso total del manjar dado. La entrada se presenta en el editor.
3.- Prepare una copia de la lista de fuentes (esto debe hacerse con una sola línea) y luego repita 
sobre ella para reducir el precio de cada manjar en un 20% si su peso supera el valor de 300.
4.- Presentar una lista original de golosinas y una lista que contenga las propuestas.
5.- Compruebe si su código funciona correctamente al copiar y modificar los detalles del artículo 
de dulces.

Nota:
La mayoría del código aquí escrito es copia fiel del ejercicio de laboratorio expuesto
en el curso de Python Institute suministrado por Edube.org. El código añadido se indicará
explícitamente con un comentario "# Código agregado".
"""

from copy import deepcopy  # Código agregado

warehouse = list()
warehouse.append({"name": "Lolly Pop", "price": 0.4, "weight": 133})
warehouse.append({"name": "Licorice", "price": 0.1, "weight": 251})
warehouse.append({"name": "Chocolate", "price": 1, "weight": 601})
warehouse.append({"name": "Sours", "price": 0.01, "weight": 513})
warehouse.append({"name": "Hard candies", "price": 0.3, "weight": 433})

print("Source list of candies")
for item in warehouse:
    print(item)

# Código agregado
print()
warehouse2 = deepcopy(warehouse)
for item in warehouse2:
    if item["weight"] > 300:
        item["price"] -= item["price"] * 0.2

print("Proposal price list of candies")
for item in warehouse2:
    print(item)
