"""Используйте списковое включение, чтобы создать список с именем even,
в котором будут содержаться четные числа в промежутке range(10)."""

even = [number for number in range(10) if number % 2 == 0]

print(even)
