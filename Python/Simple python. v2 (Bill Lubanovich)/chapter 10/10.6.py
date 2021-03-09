"""Для класса Element определите метод с именем dump(),
который выводит на экран значения атрибутов объекта (name, symbol и number).
Создайте объект hydrogen из этого нового определения и используйте метод dump(),
чтобы вывести на экран его атрибуты."""


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)


hydrogen = Element('MyName', 'Q', 44)
hydrogen.dump()
