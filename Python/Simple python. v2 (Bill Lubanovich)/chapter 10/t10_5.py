"""Создайте словарь со следующими ключами и значениями:
'name': 'Hydrogen', 'symbol': 'H', 'number': 1.
Далее создайте объект с именем hydrogen класса Element с помощью этого словаря.
"""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


d = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**d)

print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
