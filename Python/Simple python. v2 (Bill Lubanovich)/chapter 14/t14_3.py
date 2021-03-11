"""
Присвойте строку This is a test of the emergency text system переменной
test1 и запишите эту переменную в файл с именем test.txt.
"""

test1 = 'This is a test of the emergency text system'
with open('test.txt', 'w') as file:
    file.write(test1)
