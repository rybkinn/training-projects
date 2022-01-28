"""
Замените пробелы на указанные символы.
Напишите метод для замены всех пробелов в строке на '%20'.
Игнорируйте любые дополнительные пробелы в начале или конце строки.
"""


class MyClass:
    def __init__(self, string=str):
        self.string = string

    def replacement_space(self):
        self.string = self.string.strip().replace(' ', '%20')


p1 = MyClass('  ch e ck   ')
print(p1.string)
p1.replacement_space()
print(p1.string)
