"""
Считайте данные из файла books.csv и добавьте их в таблицу book.
"""
import csv
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()

with open('books.csv', 'rt') as fout:
    books = csv.DictReader(fout)
    for book in books:
        curs.execute('INSERT INTO books VALUES(?, ?, ?)', (book['title'], book['author'], book['year']))

conn.commit()
curs.close()
conn.close()
