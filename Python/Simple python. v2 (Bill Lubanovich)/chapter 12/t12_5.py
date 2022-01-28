"""
Импортируйте модуль re, чтобы использовать функции регулярных выражений
в Python. Примените функцию re.findall() для вывода на экран всех слов,
начинающихся с буквы с.
"""
import re
import t12_4

result = re.findall(r'\bc\w*', t12_4.mammoth)

print(result)
