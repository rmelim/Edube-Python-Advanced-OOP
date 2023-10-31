"""
meta.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Imagina que te han dado la tarea de limpiar el código de un sistema desarrollado en Python: 
el código debe tratarse como código heredado.
* El sistema fue creado por un grupo de voluntarios que trabajaron sin reglas claras de 
"codificación limpia".
* El sistema adolece de un problema: no sabemos en qué orden se crean las clases, por lo que 
provoca múltiples problemas de dependencia.

* Su tarea es preparar una metaclase que sea responsable de:
    * Equipar todas las clases recién instanciadas con marcas de tiempo, consiste en un atributo 
    de clase denominado "instantiation_time".
    * Equipar todas las clases recién instanciadas con el método "get_instantiation_time()". 
    El método debe devolver el valor del atributo de clase "instantiation_time".

La metaclase debe tener su propia variable de clase (una lista) que contenga una lista de los 
nombres de las clases instanciadas por la metaclase (consejo: agregue el nombre de la clase 
en el método __new__).

    * Su metaclase debe usarse para crear algunas clases heredadas distintas.
    * Crear objetos basados en las clases.
    * Enumere los nombres de clase de los que se crea una instancia en la metaclase.
"""

import time


def get_instantiation_time(self):
    return self.instantiation_time


class MetaTime(type):
    class_list = []

    def __new__(mcs, name, bases, dictionary):
        mcs.class_list.append(name)
        dictionary["get_instantiation_time"] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, dictionary)
        obj.instantiation_time = time.ctime(time.time())
        return obj


class MyClass1(metaclass=MetaTime):
    time.sleep(1)


class MyClass2(metaclass=MetaTime):
    time.sleep(2)


obj1 = MyClass1()
print(obj1.get_instantiation_time())


obj2 = MyClass2()
print(obj2.get_instantiation_time())

print(MetaTime.class_list)
