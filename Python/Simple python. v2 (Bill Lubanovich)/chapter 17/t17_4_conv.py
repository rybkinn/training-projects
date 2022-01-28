"""
Возможно, вы видели эпизод телесериала I Love Lucy, в котором Люси и Этель
работают на шоколадной фабрике. Парочка стала отставать,
когда линия конвейера, направлявшая к ним на обработку конфеты,
еще более ускорилась. Напишите симуляцию, которая отправляет разные
типы конфет в список Redis, и клиент Lucy, делающий блокирующие
выталкивания из списка. Ей нужно 0,5 секунды, чтобы обработать одну конфету.
Выведите на экран время и тип каждой конфеты, которую получит Lucy,
а также количество необработанных конфет.
"""
import redis
import time
import random

conn = redis.Redis()
candy = ['KitKat', 'Cadbury', 'Rococo', 'Thorntons', 'Snickers']
conveyor = 'chocolates'

while True:
    seconds = random.random()
    time.sleep(seconds)
    piece = random.choice(candy)
    conn.rpush(conveyor, piece)
