"""Создайте еще один класс, который, конечно же, называется Thing3.
В этот раз присвойте значение 'xyz' атрибуту объекта letters.
Выведите на экран значение атрибута letters.
Понадобилось ли вам создавать объект класса, чтобы сделать это?"""


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


example = Thing3()
print(example.letters)
