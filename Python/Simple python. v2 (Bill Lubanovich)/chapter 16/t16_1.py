"""
Сохраните следующие несколько строк в файл books.csv.
Обратите внимание на то, что, если поля разделены запятыми,
вам нужно заключить в кавычки поле, содержащее запятую:
author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
"""

sp = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

with open('books.csv', 'wt') as fout:
    fout.write(sp)
