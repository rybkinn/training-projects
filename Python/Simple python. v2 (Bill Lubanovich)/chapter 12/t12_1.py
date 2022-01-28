"""
Создайте строку Unicode с именем mystery и присвойте ей значение'\U0001f4a9'.
Выведите на экран значение строки mystery.
Выведите на экран значение переменной mystery и ее имя Unicode.
"""
import unicodedata

mystery = '\U0001f4a9'
print('\U0001f4a9')
print(mystery, unicodedata.name(mystery))

