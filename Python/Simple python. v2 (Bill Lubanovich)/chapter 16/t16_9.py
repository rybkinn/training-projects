"""
Установите сервер Redis и библиотеку Python redis
(с помощью команды pip install redis) на свой компьютер.
Создайте хеш redis с именем test, содержащий поля
count(1) и name('Fester Bestertester'). Выведите все поля хеша test.
"""
import redis
conn = redis.Redis()
conn.delete('test')

conn.hset('test', 'count', '1')
conn.hset('test', 'name', 'Fester Bestertester')


print(conn.hgetall('test'))
