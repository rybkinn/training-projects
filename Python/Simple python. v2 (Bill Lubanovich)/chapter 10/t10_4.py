"""Создайте класс Element, имеющий атрибуты объекта name, symbol и number.
Создайте объект этого класса со значениями 'Hydrogen', 'H' и 1."""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


example = Element('Hydrogen', 'H', 1)

print(example.name)
print(example.symbol)
print(example.number)
