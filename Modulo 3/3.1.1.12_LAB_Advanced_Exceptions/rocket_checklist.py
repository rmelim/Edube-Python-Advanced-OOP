"""
rocket_checklist.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Intente ampliar el script de la lista de comprobación para controlar más comprobaciones 
diferentes, todas notificadas como excepciones RocketNotReady.
* Agregue sus propias comprobaciones para: baterías y circuitos.

Nota:
La mayoría del código aquí escrito es copia fiel del ejercicio de laboratorio expuesto
en el curso de Python Institute suministrado por Edube.org. El código añadido se indicará
explícitamente con un comentario "# add your own implementation".
"""


class RocketNotReadyError(Exception):
    pass


def personnel_check():
    try:
        print("\tThe captain's name is", crew[0])
        print("\tThe pilot's name is", crew[1])
        print("\tThe mechanic's name is", crew[2])
        print("\tThe navigator's name is", crew[3])
    except IndexError as e:
        raise RocketNotReadyError("Crew is incomplete") from e


def fuel_check():
    try:
        print("Fuel tank is full in {}%".format(100 / 0))
    except ZeroDivisionError as e:
        raise RocketNotReadyError("Problem with fuel gauge") from e


def batteries_check():
    # add your own implementation
    try:
        print(f"Batteries charged to {int('battery')}%")
    except ValueError as e:
        raise RocketNotReadyError("Battery charging problems") from e


def circuits_check():
    # add your own implementation
    try:
        print(f"Circuit status: {circuits}. Circuits ready")
    except NameError as e:
        raise RocketNotReadyError("Problems with circuits") from e


crew = ["John", "Mary", "Mike"]
fuel = 100
battery = 10
circuit = True
check_list = [personnel_check, fuel_check, batteries_check, circuits_check]

print("Final check procedure")

for check in check_list:
    try:
        check()
    except RocketNotReadyError as f:
        print('RocketNotReady exception: "{}", caused by "{}"'.format(f, f.__cause__))