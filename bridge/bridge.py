from abc import ABC, abstractmethod
from typing import ClassVar


class Printer(ABC):
    def print(self, message):
        pass


class StdPrinter(Printer):
    def print(self, message):
        print(message)


class FilePrinter(Printer):
    def print(self, message):
        with open('file.txt', 'a') as f:
            print(message, file=f)


class PrinterUser(ABC):
    def __init__(self, printer: ClassVar[Printer]):
        self.printer = printer

    @abstractmethod
    def print(self, message):
        pass


class PrinterUserMultiplierBy2(PrinterUser):
    def __init__(self, printer):
        super().__init__(printer=printer)

    def print(self, message):
        self.printer.print(message * 2)


class PrinterUserMultiplierBy3(PrinterUser):
    def __init__(self, printer):
        super().__init__(printer=printer)

    def print(self, message):
        self.printer.print(message * 3)


printer_user_x3_stdout = PrinterUserMultiplierBy3(printer=StdPrinter())
printer_user_x2_stdout = PrinterUserMultiplierBy2(printer=StdPrinter())

printer_user_x3_file = PrinterUserMultiplierBy3(printer=FilePrinter())
printer_user_x2_file = PrinterUserMultiplierBy2(printer=FilePrinter())

printer_user_x3_stdout.print(message='X3std')
printer_user_x2_stdout.print(message='X2std')
printer_user_x3_file.print(message='X2file')
printer_user_x2_file.print(message='X2file')
