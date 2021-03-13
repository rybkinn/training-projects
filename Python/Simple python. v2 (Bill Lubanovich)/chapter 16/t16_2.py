"""
Используйте модуль csv и его метод DictReader, чтобы считать содержимое файла
books.csv в переменную books. Выведите на экран значения переменной books.
Обработал ли метод DictReader кавычки и запятые в заголовке второй книги?
"""
import csv

with open('books.csv', 'rt') as fout:
    books = csv.DictReader(fout)
    for book in books:
        print(book)
