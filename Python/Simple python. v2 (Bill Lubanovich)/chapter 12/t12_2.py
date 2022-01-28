"""
Закодируйте строку mystery, на этот раз с использованием кодировки UTF-8,
в переменную типа bytes с именем pop_bytes.
Выведите на экран значение переменной pop_bytes.
"""

mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')
print(pop_bytes)
