"""
Считайте и выведите на экран столбец title таблицы book в алфавитном порядке.
"""
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()

title = curs.execute('SELECT title FROM books ORDER BY title ASC').fetchall()

for item in title:
    print(item[0])

curs.close()
conn.close()
