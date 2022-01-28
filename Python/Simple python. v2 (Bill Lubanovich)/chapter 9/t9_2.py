"""Определите функцию генератора get_odds(),
которая возвращает нечетные числа из диапазона range(10).
Используйте цикл for, чтобы найти и вывести третье возвращенное значение."""


def get_odds():
    for numb in range(10):
        if numb % 2 == 1:
            yield numb


gen = get_odds()
for n in gen:
    print(n)
