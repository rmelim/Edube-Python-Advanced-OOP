"""
time_interval.py -- Elaboradopor Rui Duarte dos Santos Melim

Escenario:
* Crear una clase que represente un intervalo de tiempo.
* la clase debe implementar su propio método para sumar y restar en objetos de clase de 
intervalo de tiempo.
* La clase debe implementar su propio método para multiplicar objetos de clase de intervalo 
de tiempo por un valor de tipo entero.
* El método __init__ debe basarse en palabras clave para permitir la inicialización precisa 
y conveniente del objeto, pero limitarlo a parámetros de horas, minutos y segundos.
* El método __str__ debe devolver una cadena HH:MM:SS, donde HH representa horas, MM representa 
minutos y SS representa los atributos segundos del objeto intervalo de tiempo.
* Comprobar el tipo de argumento y, en caso de discrepancia, generar una excepción TypeError.

Sugerencia #1:
Justo antes de hacer los cálculos, conviertir cada intervalo de tiempo en un número correspondiente 
de segundos para simplificar el algoritmo. Para sumar y restar, se puede usar un método interno, 
ya que la resta es solo una adición negativa.

Sugerencia #2:
Se puede utilizar la instrucción assert para validar si el resultado del método __str__ aplicado a
un objeto de intervalo de tiempo es igual al valor esperado.

Datos de prueba:
El primer intervalo de tiempo (FTI) es horas = 21, minutos = 58, segundos = 50
El segundo intervalo de tiempo (ITS) es horas = 1, minutos = 45, segundos = 22
El resultado esperado de la adición (FTI + ITS) es 23:44:12
El resultado esperado de la resta (FTI - ITS) es 20:13:28
El resultado esperado de la multiplicación (FTI * 2) es 43:57:40
"""


class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        for i in [hours, minutes, seconds]:
            if not isinstance(i, int):
                raise TypeError("Los argumentos 'hours', 'minutes' y 'seconds' deben ser enteros")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._interval_seconds = (hours * 3600) + (minutes * 60) + seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("El argumento debe ser un objeto TimeInterval")
        return self._convert_seconds(self._interval_seconds + other._interval_seconds)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("El argumento debe ser un objeto TimeInterval")
        other = other.__mul__(-1)
        return self.__add__(other)

    def __mul__(self, value=1):
        if not isinstance(value, int):
            raise TypeError("El argumento debe ser un valor entero")
        return self._convert_seconds(self._interval_seconds * value)

    def _convert_seconds(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        return TimeInterval(hours, minutes, seconds)


# Prueba del algoritmo
fti = TimeInterval(hours=21, minutes=58, seconds=50)
its = TimeInterval(hours=1, minutes=45, seconds=22)

print(fti + its)
print(fti - its)
print(fti * 2)
