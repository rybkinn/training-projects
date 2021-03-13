"""
Используйте модуль sqlite3, чтобы создать базу данных SQLite books.db
и таблицу books, содержащую следующие поля: title (текст),
author (текст) и year (целое число).
"""
import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()

curs.execute('''CREATE TABLE books(
    title text,
    author text,
    year INT);
''')

curs.close()
conn.close()
