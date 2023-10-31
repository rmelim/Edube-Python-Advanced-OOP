"""
mobile_phone.py -- Elaborado por Rui Duarte dos Santos Melim

Crear una clase que represente un teléfono móvil. La clase debe implementar los siguientes métodos:

1.- __init__ espera que se pase un número como argumento; Este método almacena el número en una 
variable de instancia self.number

2.- turn_on() debe devolver el mensaje 'El teléfono móvil {número} está encendido'. 
Las llaves se utilizan para marcar el lugar para insertar la variable numérica del objeto.

3.- turn_off() debe devolver el mensaje 'El teléfono móvil está apagado'.

4.- call(number) debe devolver el mensaje 'Llamando a {número}'. Las llaves se utilizan para marcar 
el lugar para insertar la variable numérica del objeto.

* Crear dos objetos que representen dos teléfonos móviles diferentes y asignarles números de 
teléfono aleatorios.
* Implemente una secuencia de llamadas a métodos en los objetos para activarlos, llame a cualquier número.
* Imprimir los resultados de los métodos;
* Apaga ambos móviles.
"""


class MobilePhone:
    def __init__(self, number):
        self.number = number

    def turn_on(self):
        return f"El teléfono móvil {self.number} está encendido"

    def turn_off(self):
        return "El teléfono móvil está apagado"

    def call(self, number):
        return f"Llamando a {number}"


phone1 = MobilePhone("555-4528903")
phone2 = MobilePhone("555-2332268")

print(phone1.turn_on())
print(phone2.turn_on())

print(phone1.call("999-4587896"))

print(phone1.turn_off())
print(phone2.turn_off())
