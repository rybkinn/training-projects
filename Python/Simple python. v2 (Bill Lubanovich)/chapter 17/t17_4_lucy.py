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
import datetime

conn = redis.Redis()
timeout = 5
conveyor = 'chocolates'

while True:
    time.sleep(0.5)
    msg = conn.blpop(conveyor, timeout)
    remaining = conn.llen(conveyor)
    if msg is not None:
        piece = msg[1].decode('utf-8')
        print('Lucy got a', piece, 'at', datetime.datetime.utcnow(),
              'only', remaining, 'left')
    else:
        print('No candy on the conveyor!')
