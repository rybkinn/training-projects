"""Определите три класса: Laser, Claw и SmartPhone.
Каждый из них имеет только один метод — does().
Он возвращает значения 'disintegrate' (для Laser), 'crush' (для Claw) или
'ring' (для SmartPhone).
Далее определите класс Robot, который содержит по одному объекту каждого из
этих классов.
Определите метод does() для класса Robot, который выводит на экран все,
что делают его компоненты."""


class Laser:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f'All work:\n' \
               f'{self.laser.does()}\n' \
               f'{self.claw.does()}\n' \
               f'{self.smartphone.does()}'


r = Robot()
print(r.does())
