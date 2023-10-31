"""
automotive.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
Imagína que eres un fanático de los automóviles y puedes construir un automóvil a partir de un 
conjunto limitado de componentes.

Su tarea es:
* Defina clases que representen:
    * Neumáticos (como un paquete que necesita un automóvil para funcionar)
        * Métodos disponibles: get_pressure(), pump()
        * Atributo disponible: size
    * Motor
        * Métodos disponibles: start(), stop(), get_state()
        * Atributo disponible: fuel_type
    * Vehículo
        * Método disponible: __init__(vin, engine, tires)
        * Atributo disponible: vin

* En función de las clases definidas anteriormente, cree los siguientes objetos:
    * Dos juegos de neumáticos: de ciudad (tamaño: 15) y todoterreno (tamaño: 18)
    * Dos motores: motor eléctrico, motor de gasolina

* Cree una instancia de dos objetos que representen coches:
    * El primero es un coche urbano, construido con un motor eléctrico y neumáticos urbanos
    * El segundo es un coche todoterreno construido con un motor de gasolina y neumáticos 
    todoterreno

* Juega con los coches llamando a los métodos responsables de la interacción con los componentes.
"""


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = 0

    def get_pressure(self):
        return f"Presión: {self.pressure}"

    def pump(self, value):
        self.pressure = value


class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        self.state = "Apagado"

    def star(self):
        self.state = "Encendido"

    def stop(self):
        self.state = "Apagado"

    def get_state(self):
        return f"Combustible {self.fuel_type}, Estado: {self.state}"


class Vehicle:
    def __init__(self, vin, engine, tires):
        self.vin = vin
        self.engine = engine
        self.tires = tires


city_tires = Tires(15)
off_road_tires = Tires(18)

electric_engine = Engine("Electrico")
gasoline_engine = Engine("Gasolina")


city_car = Vehicle("ABC268", electric_engine, city_tires)
atv_car = Vehicle("XYZ135", gasoline_engine, off_road_tires)

# Pruebas del código
print("\nVehículo para la ciudad. Situación actual:")
print(f"Motor: {city_car.engine.get_state()}. Neumáticos: {city_car.tires.get_pressure()}")
print("Iniciando Vehículo.")
city_car.engine.star()
city_car.tires.pump(30)
print(f"Motor: {city_car.engine.get_state()}. Neumáticos: {city_car.tires.get_pressure()}")
city_car.engine.stop()

print("\nVehículo todo terreno. Situación actual:")
print(f"Motor: {atv_car.engine.get_state()}. Neumáticos: {atv_car.tires.get_pressure()}")
print("Iniciando Vehículo.")
atv_car.engine.star()
atv_car.tires.pump(40)
print(f"Motor: {atv_car.engine.get_state()}. Neumáticos: {atv_car.tires.get_pressure()}")
atv_car.engine.stop()
