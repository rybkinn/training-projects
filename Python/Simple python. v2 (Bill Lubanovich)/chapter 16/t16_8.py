"""
Используйте модуль sqlalchemy, чтобы подключиться к базе данных
sqlite3 books.db, которую вы создали в упражнении 16.4.
Как и в упражнении 16.6, считайте и выведите на экран столбец
title таблицы book в алфавитном порядке.
"""
import sqlalchemy as sa

engine = sa.create_engine('sqlite:///books.db')
conn = engine.connect()

rows = conn.execute('SELECT title FROM books ORDER BY title ASC')

for item in rows:
    print(item[0])
