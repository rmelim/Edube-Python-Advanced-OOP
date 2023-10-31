"""
timestamp.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Cree un decorador de funciones que imprima una marca de tiempo, en una forma como 
año-mes-día hora:minuto:segundos, por ejemplo, 2019-11-05 08:33:22
* Cree algunas funciones ordinarias que realicen algunas tareas simples, como sumar o 
multiplicar dos números.
* Aplique su decorador a esas funciones para asegurarse de que se pueda monitorear el 
tiempo de ejecución de las funciones.
"""

from datetime import datetime


def execute_time(deco_function):
    def print_time(*args):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return deco_function(*args)

    return print_time


@execute_time
def sum_numbers(num1, num2):
    return num1 + num2


@execute_time
def mult_numbers(num1, num2):
    return num1 * num2


print(sum_numbers(4, 8))
print()
print(mult_numbers(2, 5))
