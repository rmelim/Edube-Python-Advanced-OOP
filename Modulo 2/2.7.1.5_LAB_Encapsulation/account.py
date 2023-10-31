"""
account.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Implemente una clase que represente una excepción de cuenta.
* Implemente una clase que represente una sola cuenta bancaria.
* Esta clase debe controlar el acceso a los atributos de número de cuenta y saldo de cuenta mediante
la implementación de las propiedades:
* Debería ser posible leer solo el número de cuenta, no cambiarlo. En caso de que alguien intente 
cambiar el número de cuenta, active una alarma activando una excepción.
* No debería ser posible establecer un saldo negativo. En caso de que alguien intente establecer un 
saldo negativo, active una alarma activando una excepción.
* Cuando la operación bancaria (depósito o retiro) es superior a 100.000, debe imprimir un mensaje
 adicional en la salida estándar (pantalla) para fines de auditoría.
* No debería ser posible eliminar una cuenta siempre que el saldo no sea cero.


Pon a prueba el comportamiento de tu clase de la siguiente manera:
* Establecer el saldo en 1000.
* Tratando de establecer el balance en -200.
* Intentar establecer un nuevo valor para el número de cuenta.
* Tratando de depositar 1.000.000
* Intentar eliminar el atributo de cuenta que contiene un saldo distinto de cero.
"""


class AccountException(Exception):
    pass


class BankAccount:
    def __init__(self, number):
        self.__number = number
        self.__balance = 0

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        raise AccountException("No se puede cambiar los numeros de cuenta.")

    @number.deleter
    def number(self):
        if self.__balance > 0:
            raise AccountException("No pueden eliminarse cuentas con saldo positivo.")
        self.__number = None

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise AccountException("El saldo no puede ser negativo")
        self.__balance = value

    def deposit(self, amount):
        if amount >= 100000:
            print(f"Alerta de auditoría. Se ha depositado la cantidad de {amount:,.2f}")
        self.__balance += amount

    def withdraw(self, amount):
        if amount >= 100000:
            print(f"Alerta de auditoría. Se ha retirado la cantidad de {amount:,.2f}")
        self.__balance -= amount


# Pruebas del código
account = BankAccount("01040062740620021749")

try:
    account.balance = 1000
except AccountException as e:
    print("Error --->", e)

try:
    account.balance = -200
except AccountException as e:
    print("Error --->", e)

try:
    account.number = "999999999999999999"
except AccountException as e:
    print("Error --->", e)

account.deposit(1000000)

try:
    del account.number
except AccountException as e:
    print("Error --->", e)
