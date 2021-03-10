"""Присвойте значение 5 переменной guess_me. Используйте цикл for для того,
чтобы проитерировать с помощью переменной number по диапазону range(10).
Если значение переменной number меньше, чем значение guess_me,
выведите на экран сообщение 'too low'.
Если оно равно значению guess_me — выведите сообщение 'found it!', а затем выйдите из цикла.
Если значение переменной number больше, чем guess_me,
выведите на экран сообщение 'oops' и выйдите из цикла."""

guess_me = 6

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break
    elif number > guess_me:
        print('oops')
        break
