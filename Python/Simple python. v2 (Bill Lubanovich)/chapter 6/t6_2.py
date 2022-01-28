"""Присвойте значение 7 переменной guess_me и значение 1 переменной number.
Напишите цикл while, который сравнивает переменные number и guess_me.
Выведите строку 'too low', если значение переменной start меньше значения переменной guess_me.
Если значение переменной number равно значению переменной guess_me,
выведите строку 'found it!' и выйдите из цикла.
Если значение переменной number больше значения переменной guess_me,
выведите строку 'oops' и выйдите из цикла.
Увеличьте значение переменной number на выходе из цикла."""

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
    number += 1
