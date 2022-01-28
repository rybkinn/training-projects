"""
Используйте ZeroMQ, чтобы публиковать стихотворение из
упражнения 12.4 (пример 12.1) по одному слову за раз.
Напишите потребитель ZeroMQ, который будет выводить на экран каждое слово,
начинающееся с гласной. Напишите другой потребитель, который станет
выводить все слова, состоящие из пяти букв. Знаки препинания игнорируйте.
"""
import string
import zmq

host = '127.0.0.1'
port = 6789

ctx = zmq.Context()

sub = ctx.socket(zmq.SUB)
sub.connect(f'tcp://{host}:{port}')

sub.setsockopt(zmq.SUBSCRIBE, b'vowels')
sub.setsockopt(zmq.SUBSCRIBE, b'five')

while True:
    topic, word = sub.recv_multipart()
    print(topic, word)

