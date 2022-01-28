"""
Используя кодировку UTF-8, декодируйте переменную pop_bytes в строку pop_string.
Выведите на экран значение переменной pop_string.
Равно ли оно значению переменной mystery?
"""
mystery = '\U0001f4a9'
pop_bytes = mystery.encode('utf-8')

pop_string = pop_bytes.decode('utf-8')
print(pop_string)
print(pop_string == mystery)
