"""
Создайте дочерний класс Motherboard, который наследуется от классов: CPU, GPU,
Memory.
В свою очередь CPU наследуется от классов: AMD и Intell,
GPU от классов NVidia, GeForce.

Создайте экземпляр класса Motherboard и наполните ее конкретным содержимым
(локальным свойствам этого объекта присвойте определенные значения).Определите
вспомогательные методы в базовых классах и выведите итоговую информацию
в консоль с помощью метода showinfo() класса Motherboard.
"""


class AMD:
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class Intell:
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class NVidia:
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class GeForce:
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class CPU(AMD, Intell):
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class GPU(NVidia, GeForce):
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class Memory:
    def __init__(self):
        print(f'print class {__class__.__name__}')
        super().__init__()


class Motherboard(CPU, GPU, Memory):
    def __init__(self, socket, pci, sata):
        self.socket = socket
        self.pci = pci
        self.sata = sata
        print(f'print class {__class__.__name__}')
        super().__init__()

    def showinfo(self):
        print(f'\n'
              f'socket: {self.socket}\n'
              f'pci: {self.pci}\n'
              f'sata: {self.sata}')


ASUS = Motherboard(1433, 2, 6)
ASUS.showinfo()
