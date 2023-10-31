"""
luxury_watch.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Crear una clase que represente un reloj de lujo.
* La clase debe permitirle contener un número de relojes creados en la variable de clase 
"watches_created". El número se puede recuperar utilizando un método de clase denominado 
"get_number_of_watches_created".
* La clase puede permitirle crear un reloj con un grabado dedicado (texto). Como esta es 
una opción adicional, el reloj con el grabado debe crearse utilizando un constructor 
alternativo (un método de clase), ya que el método regular "__init__" no debe permitir 
ordenar grabados.
* El método regular "__init__" solo debe aumentar el valor de la variable de clase apropiada.

El texto que se pretende grabar debe seguir algunas restricciones:
* No debe tener más de 40 caracteres.
* Debe consistir en caracteres alfanuméricos, por lo que no se permiten caracteres de espacio.
* Si el texto no cumple con las restricciones, debe generarse una excepción.

Antes de grabar el texto deseado, el texto debe validarse contra restricciones utilizando un 
método estático dedicado.

Pruebas a realizar:
* Crea un reloj sin grabado.
* Crear un reloj con el texto correcto para grabar.
* Intenta crear un reloj con texto incorrecto, como 'foo@baz.com'. Controlar la excepción.
* Después de crear cada reloj, llame al método de clase para ver si se ha aumentado la 
variable de contador.
"""


class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def dedicate_engraving(cls, text):
        if cls.validate_text(text):
            _watch = cls()
            _watch.engraving = text
            return _watch

    @staticmethod
    def validate_text(text=""):
        if len(text) > 40:
            raise ValueError("text must be at least 40 characters")
        if not text.isalpha():
            raise ValueError("text must be a valid alpha character")
        return True


# Pruebas del código
# ----------------------------------------------------------------
print(f"Relojes creados: {LuxuryWatch.get_number_of_watches_created()}")
# Sin texto grabado
watch1 = LuxuryWatch()
print(f"Relojes creados: {LuxuryWatch.get_number_of_watches_created()}")
# ----------------------------------------------------------------
# Con texto grabado correcto
watch2 = LuxuryWatch.dedicate_engraving("Supercalifriagilisticoespialidoso")
print(f"Se grabó el texto: {watch2.engraving} en el reloj")
print(f"Relojes creados: {LuxuryWatch.get_number_of_watches_created()}")
# ----------------------------------------------------------------
# Con texto grabado incorrecto - controlando excepción
try:
    watch3 = LuxuryWatch.dedicate_engraving("foo@baz.com")
except ValueError as e:
    print("Exception error:", e)

print(f"Se han creado un total de {LuxuryWatch.get_number_of_watches_created()} relojes")
