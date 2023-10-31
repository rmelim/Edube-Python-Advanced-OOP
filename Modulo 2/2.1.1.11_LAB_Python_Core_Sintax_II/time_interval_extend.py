"""
time_interval_extend.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Ampliar la implementación de clase preparada en el laboratorio 2.1.1.11 para admitir la suma y 
resta de enteros a objetos de intervalo de tiempo.
* Agregar un entero a un objeto de intervalo de tiempo significa agregar segundos.
* Restar un entero de un objeto de intervalo de tiempo significa quitar segundos.

sugerencia:
En el caso de que un método especial reciba un argumento de tipo entero, en lugar de un objeto de 
intervalo de tiempo, cree un nuevo objeto de intervalo de tiempo basado en el valor entero.

Datos de prueba:
El intervalo de tiempo (TTI) es horas = 21, minutos = 58, segundos = 50
El resultado esperado de la adición (TTI + 62) es 21:59:52
El resultado esperado de la resta (ITT - 62) es 21:57:48
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
        if isinstance(other, int):
            other = TimeInterval(seconds=other)
        elif not isinstance(other, TimeInterval):
            raise TypeError("El argumento debe ser un objeto TimeInterval o un valor entero")
        return self._convert_seconds(self._interval_seconds + other._interval_seconds)

    def __sub__(self, other):
        if isinstance(other, int):
            other = TimeInterval(seconds=other)
        elif not isinstance(other, TimeInterval):
            raise TypeError("El argumento debe ser un objeto TimeInterval o un valor entero")
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
tti = TimeInterval(hours=21, minutes=58, seconds=50)

print(tti + 62)
print(tti - 62)
