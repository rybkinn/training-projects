"""Вызовите функцию print(hydrogen).
В определении класса Element измените имя метода dump на __str__,
создайте новый объект hydrogen и затем снова вызовите метод print(hydrogen)."""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'{self.name}, {self.symbol}, {self.number}'


hydrogen = Element('MyName', 'Q', 44)

print(hydrogen)
