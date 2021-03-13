"""
Считайте и выведите на экран все столбцы таблицы book в порядке публикации.
"""
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()

column = curs.execute('SELECT * FROM books ORDER BY year ASC').fetchall()

for item in column:
    print(item[0], item[1], item[2])

curs.close()
conn.close()
