"""
mfd_abstract.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
* Crear un dispositivo multifunción (MFD) que puede escanear e imprimir documentos.
* El sistema consta de un escáner y una impresora.
* Su tarea es crear plantillas para ello y entregar las implementaciones.

* Cree una clase abstracta que represente un Scanner que aplique los métodos siguientes:
    * scan_document: devuelve una cadena que indica que el documento ha sido escaneado.
    * get_scanner_status: devuelve información sobre el escáner (resolución máx., número de serial)

* Cree una clase abstracta que represente una Impresora que aplique los métodos siguientes:
    * print_document: devuelve una cadena que indica que el documento se ha impreso.
    * get_printer_status: devuelve información sobre la impresora (resolución máx., número serial)

* Cree clases MFD1, MFD2 y MFD3 que hereden las clases abstractas responsables del escaneado y la 
impresión:
    * MFD1: debe ser un dispositivo barato, hecho de una impresora barata y un escáner barato, 
    por lo que las capacidades del dispositivo (resolución) deben ser bajas.
    * MFD2: debe ser un dispositivo de precio medio que permita operaciones adicionales como el 
    historial de operaciones de impresión, y la resolución es mejor que el dispositivo de menor 
    precio.
    * MFD3: debe ser un dispositivo premium que permita operaciones adicionales como el historial 
    de operaciones de impresión y la máquina de fax.

* Cree instancias de MFD1, MFD2 y MFD3 para demostrar sus habilidades. Todos los dispositivos deben 
ser capaces de servir conjuntos de características genéricas.
"""

import abc


class Scanner(abc.ABC):
    def scan_document(self):
        return "Documento escaneado"

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):
    def print_document(self):
        return "Documento impreso"

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def __init__(self, max_resolution=0, serial=""):
        self.max_resolution = max_resolution
        self.serial = serial

    def get_scanner_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"

    def get_printer_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"


class MFD2(Scanner, Printer):
    def __init__(self, max_resolution=0, serial=""):
        self.max_resolution = max_resolution
        self.serial = serial

    def get_scanner_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"

    def get_printer_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"

    def historial(self):
        print("Historial de impresiones")


class MFD3(Scanner, Printer):
    def __init__(self, max_resolution=0, serial=""):
        self.max_resolution = max_resolution
        self.serial = serial

    def get_scanner_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"

    def get_printer_status(self):
        return f"Resolución Máxima: {self.max_resolution} / Número serial: {self.serial}"

    def historial(self):
        print("Historial de impresiones")

    def print_fax(self):
        return "El fax ha sido impreso"

    def send_fax(self):
        return "El fax ha sido enviado"


# Pruebas del código
mfd_lower = MFD1(max_resolution=150, serial="AXJ854789")
print(mfd_lower.scan_document())
print(mfd_lower.print_document())
print(mfd_lower.get_scanner_status())

mfd_medium = MFD2(max_resolution=600, serial="XG-7413-89")
print(mfd_medium.scan_document())
print(mfd_medium.print_document())
print(mfd_medium.get_scanner_status())
mfd_medium.historial()

mfd_high = MFD3(max_resolution=1200, serial="854-YND-11524/82")
print(mfd_high.scan_document())
print(mfd_high.print_document())
print(mfd_high.get_scanner_status())
print(mfd_high.send_fax())
mfd_high.historial()
