"""
Используйте ZeroMQ, чтобы публиковать стихотворение из
упражнения 12.4 (пример 12.1) по одному слову за раз.
Напишите потребитель ZeroMQ, который будет выводить на экран каждое слово,
начинающееся с гласной. Напишите другой потребитель, который станет
выводить все слова, состоящие из пяти букв. Знаки препинания игнорируйте.
"""
import string
import zmq
from time import sleep

host = '127.0.0.1'
port = 6789

ctx = zmq.Context()

pub = ctx.socket(zmq.PUB)
pub.bind(f'tcp://{host}:{port}')

sleep(1)

with open('mammoth.txt', 'rt') as poem:
    words = poem.read()
for word in words.split():
    word = word.strip(string.punctuation)
    data = word.encode('utf-8')
    if word.startswith(('a', 'e', 'i', 'o', 'u', 'A', 'e', 'i', 'o', 'u')):
        print('vowels', ' - ', data.decode())
        pub.send_multipart([b'vowels', data])
    if len(word) == 5:
        print('five', ' - ', data.decode())
        pub.send_multipart([b'five', data])
