"""
mfd.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* La tarea consiste en crear una clase de dispositivo multifunción (MFD) que consta de métodos 
responsables del escaneo, la impresión y el envío de documentos por fax.
* Los métodos se entregan mediante las siguientes clases:
    ** scan(), impartido por la clase Scanner.
    ** print(), impartido por la clase Printer.
    ** send() y print(), entregado por la clase Fax.
* Cada método debe imprimir un mensaje que indique su propósito y origen, como:
    ** 'print() método de la clase Printer'
    ** 'send() método de la clase Fax'
* Crear una clase MFD_SPF ('SPF' significa 'Scanner', 'Printer', 'Fax'), luego instanciarla.
* Crear una clase MFD_SFP ('SFP' significa 'Scanner', 'Fax', 'Printer'), luego instanciarla.
* En cada objeto llame a los métodos:scan(), print(), send().
* Observe las diferencias de salida. ¿Se utilizó la clase Printer cada vez?
"""


class Scanner:
    def scan(self):
        print("scan(), método de la clase Scanner.")


class Printer:
    def print(self):
        print("print(), método de la clase Printer")


class Fax:
    def print(self):
        print("print(), método de la clase Fax")

    def send(self):
        print("send(), método de la clase Fax")


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


mfd_spf_obj = MFD_SPF()
mfd_sfp_obj = MFD_SFP()

print("Utilizando la clase MFD_SPF")
mfd_spf_obj.scan()
mfd_spf_obj.print()
mfd_spf_obj.send()
print()

print("Utilizando la clase MFd_SFP")
mfd_sfp_obj.scan()
mfd_sfp_obj.print()
mfd_sfp_obj.send()
print()
